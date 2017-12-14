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
        #TODO return list of courses from file
        pass
    def normalize_word(self,word):
        #TODO normalize word by lower casing and deleting punctuation from word
        #TODO use set of punctuation symbols self.punctuation
        pass
    def get_vocabulary(self):
        #TODO return list of unique words from file and sort them alphabetically
        pass

    def vectorspaced(self,course):
        #TODO represent course by one-hot vector: vector filled with 0s, except for a 1 at the position associated with word in vocabulary
        #TODO length of vector should be equal vocabulary size
        hot_one_vectors = [] #<-- TODO: replace 
        return array(hot_one_vectors)

    def data_to_vectorspace(self):
        return [self.vectorspaced(course) for course in self.courses if course]

class Kmeans:
    """performs k-means clustering"""

    def __init__(self, k, dist):
        self.k = k
        self.dist = dist

    def nltk_cluster(self,data):
        #TODO use NLTK KMeansClusterer to cluster the data, return the list of clusters for given data
        pass


