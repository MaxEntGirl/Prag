import copy
import json

from hw05_perceptron.utils.documents import dot

class PerceptronClassifier:
    def __init__(self, weights):
        # string to int
        self.weights = weights

    @classmethod
    def from_file(cls, filename):
        """
        Load model file and construct PerceptronClassifier.
        """
        with open(filename, 'r') as modelfile:
            weights = json.load(modelfile)
            return cls(weights)

    @classmethod
    def for_dataset(cls, dataset): # Exercise 1
        """
        Initialize PerceptronClassifier for dataset. A classifier that
        is constructed with this method still needs to be trained..
        """
        #print(dataset.feature_set)
        #print(dataset.instance_list)

        weights = {feature:0 for feature in dataset.feature_set}

        return cls(weights)


    def prediction(self, counts): # Exercise 2
        """
        Return True if prediction for counts is ham, False if prediction is spam
        counts: Bag of words representation of email
        """
        #print("count:", counts)
        #print(self.weights)
        sum = 0
        for key in counts:
            sum = counts[key] * self.weights[key] + sum
        if sum > 0:
            return True
        else:
            return False

    def update(self, instance): # Exercise 3
        """
        Perform perceptron update, if the wrong label is predicted.
        Return a boolean value indicating whether an update was performed.
        """
        # Exercise 3: Replace with correct calculation of error

        predicted_output = self.prediction(instance.feature_counts)
        #print(predicted_output)
        #print(instance.label)
        if predicted_output == True and instance.label == False:
            error = 1
        elif predicted_output == False and instance.label == True:
            error = -1
        else:
            error = 0

        # Exercise 3: Replace pass with update of feature weights
        #print(error)

        do_update = error !=0
        if do_update:
            for feature, count in instance.feature_counts.items():
                self.weights[feature] = self.weights[feature] - error * count
                #print(feature, count)
        return do_update

    def training_iteration(self, dataset):
        """
        Iterate over each instance of dataset and perform perceptron update.
        Return number of updates that were performed (number of train errors).
        """
        dataset.shuffle()
        for instance in dataset.instance_list:
            self.update(instance)

    def train(self, training_set, development_set, iterations):
        """
        Train classifier and return best development accuracy.
        """
        best_dev_accuracy = 0.0
        best_weights = self.weights
        for i in range(iterations):
            self.training_iteration(training_set)
            train_accuracy = self.test_accuracy(training_set)
            development_accuracy = self.test_accuracy(development_set)
            if development_accuracy > best_dev_accuracy:
                best_dev_accuracy = development_accuracy
                best_weights = self.weights.copy()
            print("Iteration: %d \t Train Accuracy: %.4f \t Dev Accuracy: %.4f \t Best Dev Accuracy: %.4f" % (i, train_accuracy, development_accuracy, best_dev_accuracy))
        self.weights = best_weights
        return best_dev_accuracy

    def test_accuracy(self, dataset):
        """
        Caclculate accuracy of classifier on labelled dataset.
        """
        num_errors = 0
        for instance in dataset.instance_list:
            if self.prediction(instance.feature_counts) != instance.label:
                num_errors += 1
        return 1 - num_errors / len(dataset.instance_list)

    def copy(self):
        """
        Return a copy of weights.
        """
        return PerceptronClassifier(copy.copy(self.weights))

    def features_for_class(self, is_positive_class, topn=10):
        """
        Determine the topn best features for a label (True or False).
        is_positive_class: can be True or False
        """
        high_to_low = True if is_positive_class else False
        return sorted(self.weights.items(), key=lambda x: x[1], reverse=high_to_low)[:topn]

    def save(self, filename):
        """
        Save model weights as JSON file.
        """
        with open(filename, 'w') as modelfile:
            json.dump(self.weights, modelfile)