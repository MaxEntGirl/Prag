from unittest import TestCase

from hw05_perceptron.utils.documents import TextDocument, DocumentCollection
from hw05_perceptron.utils.data import Dataset, DataInstance
from hw05_perceptron.perceptron import PerceptronClassifier
from hw05_perceptron.sentiment import nltk_movie_review_accuracy

# Ham mails: True (positive data)
# Spam mails: False (negative data)
train_docs_1 = [TextDocument(sample[0], sample[1], sample[2]) for sample in
                [("highly boring boring boring", "doc1", False),
                 ("boring boring", "doc2", False),
                 ("highly", "doc3", True),
                 ("highly highly highly boring", "doc4", True)]]

train_docs_2 = [TextDocument(sample[0], sample[1], sample[2]) for sample in
                [("highly boring boring boring", "doc1", False),
                 ("boring boring", "doc2", False),
                 ("highly", "doc3", True),
                 ("green eggs", "doc4", True)]]

# This is used to test accuracy. A correctly implemented classifier should NOT reach 100% here.
dev_docs = [TextDocument(sample[0], sample[1], sample[2]) for sample in
            [("highly highly highly", "doc12", True),
             ("highly highly boring", "doc13", True),
             ("highly boring highly boring highly", "doc14", False)]]

# A correctly implemented classifier will reach 100% accuracy here
pred_docs_1 = [TextDocument(sample[0], sample[1], sample[2]) for sample in
               [("highly", "doc18", True),
                ("boring", "doc19", False),
                ("highly highly boring", "doc20", True),
                ("highly highly boring boring", "doc21", False),
                ("unknown", "doc22", False)]]

pred_docs_2 = [TextDocument(sample[0], sample[1], sample[2]) for sample in
               [("highly", "doc23", True),
                ("boring", "doc24", False),
                ("highly boring", "doc25", False),
                ("highly highly boring", "doc26", False),
                ("boring boring boring", "doc27", False)]]

# No update needed
no_update_docs = [TextDocument(sample[0], sample[1], sample[2]) for sample in
                  [("highly highly boring", "doc18", True),
                   ("boring", "doc23", False),
                   ("highly boring", "doc24", False)]]

# Do update
do_update_docs = [TextDocument(sample[0], sample[1], sample[2]) for sample in
                  [("highly", "doc25", False),
                   ("boring", "doc26", True),
                   ("highly highly boring", "doc27", False)]]


class PerceptronClassifierTest(TestCase):

    def setUp(self):
        small_collection_train_1 = DocumentCollection.from_document_list(train_docs_1)
        self.small_dataset_train_1 = Dataset.from_document_collection(small_collection_train_1)

        small_collection_train_2 = DocumentCollection.from_document_list(train_docs_2)
        self.small_dataset_train_2 = Dataset.from_document_collection(small_collection_train_2)

        small_collection_dev = DocumentCollection.from_document_list(dev_docs)
        self.small_dataset_dev = Dataset.from_document_collection(small_collection_dev, feature_set=self.small_dataset_train_1.feature_set)

        small_collection_pred_1 = DocumentCollection.from_document_list(pred_docs_1)
        self.small_dataset_pred_test_1 = Dataset.from_document_collection(small_collection_pred_1, feature_set=self.small_dataset_train_1.feature_set)

        small_collection_pred_2 = DocumentCollection.from_document_list(pred_docs_2)
        self.small_dataset_pred_test_2 = Dataset.from_document_collection(small_collection_pred_2, feature_set=self.small_dataset_train_1.feature_set)

        small_collection_no_update = DocumentCollection.from_document_list(no_update_docs)
        self.small_instance_list_no_update = [DataInstance.from_document(doc, self.small_dataset_train_1.feature_set) for doc in small_collection_no_update.all_documents()]

        small_collection_do_update = DocumentCollection.from_document_list(do_update_docs)
        self.small_instance_list_do_update = [DataInstance.from_document(doc, self.small_dataset_train_1.feature_set) for doc in small_collection_do_update.all_documents()]

    def test_01_from_file_01(self):
        """Verify that a classifier can be constructed from a file with weights."""
        classifier = PerceptronClassifier({'highly': 1, 'boring': -1})
        classifier.save('data/ex03_from_file_test.model')
        classifier = PerceptronClassifier.from_file('data/ex03_from_file_test.model')
        if classifier is None:
            self.fail(msg="Constructing classifier from file failed: from_file returned None")
        expected_weights = {'highly': 1, 'boring': -1}
        self.assertEqual(classifier.weights, expected_weights)

    def test_01_from_file_02(self):
        """Verify that a classifier can be constructed from a file with weights."""
        classifier = PerceptronClassifier({'hello': 1, 'bye': -1})
        classifier.save('data/ex03_from_file_test.model')
        classifier = PerceptronClassifier.from_file('data/ex03_from_file_test.model')
        if classifier is None:
            self.fail(msg="Constructing classifier from file failed: from_file returned None")
        expected_weights = {'hello': 1, 'bye': -1}
        self.assertEqual(classifier.weights, expected_weights)

    def test_02_for_dataset_01(self):
        """Verify that a classifier can be constructed with initial weights for a fiven dataset."""
        expected_weights = {'highly': 0, 'boring': 0}
        classifier = PerceptronClassifier.for_dataset(self.small_dataset_train_1)
        if classifier is None:
            self.fail(msg='Constructing classifier for dataset failed: for_dataset returned None')
        self.assertEqual(classifier.weights, expected_weights)

    def test_02_for_dataset_02(self):
        """Verify that a classifier can be constructed with initial weights for a fiven dataset."""
        expected_weights = {'highly': 0, 'boring': 0, 'green': 0, 'eggs': 0}
        classifier = PerceptronClassifier.for_dataset(self.small_dataset_train_2)
        if classifier is None:
            self.fail(msg='Constructing classifier for dataset failed: for_dataset returned None')
        self.assertEqual(classifier.weights, expected_weights)

    def test_03_prediction_01(self):
        """Verify that the predictions of the classifier are as expected."""
        classifier = PerceptronClassifier({'highly': 1, 'boring': -1})
        for instance in self.small_dataset_pred_test_1.instance_list:
            prediction = classifier.prediction(instance.feature_counts)
            self.assertEqual(prediction, instance.label)

    def test_03_prediction_02(self):
        """Verify that the predictions of the classifier are as expected."""
        classifier = PerceptronClassifier({'highly': 1, 'boring': -2})
        for instance in self.small_dataset_pred_test_2.instance_list:
            prediction = classifier.prediction(instance.feature_counts)
            self.assertEqual(prediction, instance.label)

    def test_04_update_01(self):
        """Verify that the perceptron update is performed correctly."""
        classifier = PerceptronClassifier({'highly': 1, 'boring': -1})
        # Test document: ("highly", "doc25", False)
        classifier.update(self.small_instance_list_do_update[0])
        expected_weigths = {'highly': 0, 'boring': -1}
        self.assertEqual(classifier.weights, expected_weigths)

        classifier = PerceptronClassifier({'highly': 1, 'boring': -1})
        # Test document: ("boring", "doc26", True),
        do_update = classifier.update(self.small_instance_list_no_update[0])
        self.assertEqual(False, do_update)

    def test_04_update_02(self):
        """Verify that the perceptron update is performed correctly."""
        classifier = PerceptronClassifier({'highly': 1, 'boring': -1})
        classifier.update(self.small_instance_list_do_update[1])
        expected_weigths = {'highly': 1, 'boring': 0}
        self.assertEqual(classifier.weights, expected_weigths)

        classifier = PerceptronClassifier({'highly': 1, 'boring': -1})
        do_update = classifier.update(self.small_instance_list_no_update[1])
        self.assertEqual(False, do_update)

    def test_05_update_01(self):
        """Accuracy on dev data should be around 82% (at least 77%)"""
        dev_acc, test_acc = nltk_movie_review_accuracy(20)
        self.assertGreater(dev_acc, 0.77)

    def test_05_update_02(self):
        """Accuracy on test data should be around 80% (between 75% and 85%)."""
        dev_acc, test_acc = nltk_movie_review_accuracy(20)
        self.assertGreater(test_acc, 0.75)
        self.assertLess(test_acc, 0.85)
