from unittest import TestCase
from hw06_knn.classification import DocumentCollection, KNNClassifier, TextDocument

dir_train= "../data/20news-bydate/20news-bydate-train/"
dir_test = "../data/20news-bydate/20news-bydate-test/"


doc_collection_train = DocumentCollection.from_dir(dir_train)
classifier = KNNClassifier(doc_collection_train,n_neighbors=4)

class ClassificationTest(TestCase):
    print("Preparing tests...")

    def test_01_choose_neighbor(self):

        winner = classifier.choose_one(['rec.sport.hockey', 'rec.sport.baseball', 'rec.motorcycles','rec.sport.hockey'])
        winner2 = classifier.choose_one(['rec.sport.hockey', 'rec.sport.baseball','rec.sport.baseball','rec.sport.hockey'])
        self.assertEqual(winner,'rec.sport.hockey')
        self.assertEqual(winner2,'rec.sport.baseball')


    def test_02a_calc_sims(self):
        test_doc = TextDocument.from_file(dir_test+'alt.atheism/53068','alt.atheism')
        pred_similarities=[(1.1364237808503724e-05, 'comp.windows.x'), (1.491533681154529e-05, 'comp.sys.mac.hardware')]
        train_docs = classifier.doc_collection.docid_to_doc.values()
        similarities = sorted(classifier.calculate_similarities(test_doc,train_docs))[:2]
        
        for i in similarities: #check format
            self.assertTrue(len(i) == 2)
            self.assertTrue(type(i) == tuple)
            self.assertTrue(type(i[0]) == float)
            self.assertTrue(type(i[1]) == str)

        for i in range(len(pred_similarities)):
            self.assertTrue(pred_similarities[i][0] == similarities[i][0])
            self.assertTrue(pred_similarities[i][1] == similarities[i][1])


    def test_02b_order_near_to_far(self):
        test_similarities=([(0.2,"c"),(0.5,"b"),(0.7,"a")],
                        [(0.3,"a"),(0.6,"b"),(0.4,"c")])

        self.assertEqual([(0.7,"a"),(0.5,"b"),(0.2,"c")],classifier.order_nearest_to_farthest(test_similarities[0]))
        self.assertEqual([(0.6,"b"),(0.4,"c"),(0.3,"a")],classifier.order_nearest_to_farthest(test_similarities[1]))


    def test_02c_labels_k_closest(self):
        sorted_lists=([(0.9,"sci.space"),(0.7,"talk.politics.guns"),(0.5,"sci.crypt"),(0.3,"sci.med"),(0.3,"alt.atheism")],
                      [(0.9,"sci.space"),(0.7,"comp.windows.x"),])

        res1=classifier.labels_k_closest(sorted_lists[0])
        res2=classifier.labels_k_closest(sorted_lists[1])

        for result in (res1,res2):
            self.assertTrue(len(result) <= classifier.n_neighbors)
            for x in result:
                self.assertTrue(type(x) == str)
        self.assertEqual(res1,["sci.space","talk.politics.guns","sci.crypt","sci.med"])
        self.assertEqual(res2,["sci.space","comp.windows.x"])

    def test_02d_append(self):
        predicted_labels=['rec.sport.hockey', 'rec.sport.baseball', 'rec.motorcycles','rec.sport.hockey']
        results=[]
        classifier.append_pred_label(results,predicted_labels)
        self.assertEqual(results,["rec.sport.hockey"])

    def test_03_accuracy(self):

        test_files = [(dir_test+'alt.atheism/53272','alt.atheism'),(dir_test+'sci.med/59225','sci.med'),
                      (dir_test+'comp.graphics/38758','comp.graphics'),(dir_test+'rec.autos/103007','rec.autos')]

        predicted_labels = classifier.classify(test_files)
        gold_labels = [cat for _,cat in test_files]
        accuracy = classifier.get_accuracy(gold_labels, predicted_labels)
        self.assertEqual(accuracy,75)

