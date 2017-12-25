from numpy import array
from nltk.cluster import KMeansClusterer
import string

class Reader:

    def __init__(self, path):
        self.path = path
        self.punctuation = set(string.punctuation)
        self.courses = self.get_lines()
        self.vocabulary = self.get_vocabulary()
        self.vector_spaced_data = self.data_to_vectorspace()

    def get_lines(self):
        # return list of courses from file
        file = open(self.path, 'r')
        courselist = []
        for line in file:
            courselist.append(line.rstrip())
        file.close()
        return courselist


    def normalize_word(self,word):
        # normalize word by lower casing and deleting punctuation from word
        # use set of punctuation symbols self.punctuation
        # print(self.punctuation)
        word = word.lower()
        for punkt in self.punctuation:
            word = word.replace(punkt,'')
        return word

    def get_vocabulary(self):
        # return list of unique words from file and sort them alphabetically
        vacabulary = []
        for line in self.courses:
            for word in line.split(' '):
                word = self.normalize_word(word)
                vacabulary.append(word)
        tokens = set(vacabulary)
        tokens = sorted(tokens)
        return tokens


    def vectorspaced(self,course):
        # represent course by one-hot vector: vector filled with 0s, except for a 1 at the position associated with word in vocabulary
        # length of vector should be equal vocabulary size

        hot_one_vectors = []  # <-- replace
        course = self.normalize_word(course)
        courselist = course.split(' ')
        for fach in self.vocabulary:
            if fach in courselist:
                hot_one_vectors.append(1)
            else:
                hot_one_vectors.append(0)

        return array(hot_one_vectors)

    def data_to_vectorspace(self):
        return [self.vectorspaced(course) for course in self.courses if course]

class Kmeans:
    """performs k-means clustering"""

    def __init__(self, k, dist):
        self.k = k
        self.dist = dist

    def nltk_cluster(self,data):
        # use NLTK KMeansClusterer to cluster the data, return the list of clusters for given data

        clusterer = KMeansClusterer(self.k, self.dist)
        clusters = clusterer.cluster(data, True)
        return clusters



