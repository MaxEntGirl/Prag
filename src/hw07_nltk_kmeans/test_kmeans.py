from unittest import TestCase
from hw07_nltk_kmeans.nltk_kmean import Reader
from hw07_nltk_kmeans.nltk_kmean import Kmeans
from nltk.cluster import euclidean_distance
#python3 -m unittest -v hw07_nltk_kmeans/test_kmeans.py

filename = '../data/courses.txt'

class ClusteringTest(TestCase):


    def setUp(self):

        self.reader = Reader(filename)
        self.clusterer = Kmeans(10, euclidean_distance)

    def test_01_courses(self):
        courses = self.reader.courses #returns list of courses
        self.assertEqual(courses[:3], ['Bioinformatik', 'Informatik', 'Mathematik'])

    def test_02_normalize(self):
        word = "(Studienrichtung"
        normalized_word = self.reader.normalize_word(word) #returns list of courses
        self.assertEqual(normalized_word, "studienrichtung")

    def test_03_vocabulary(self):
        words = self.reader.vocabulary
        self.assertEqual(words[:3], ['albanologie', 'allgemeine', 'als'])

    def test_04_vectorspaced(self):
        word_to_vectorspace = self.reader.vectorspaced("Slavische Philologie")
        vocab_size = len(self.reader.vocabulary)

        self.assertEqual(vocab_size, len(word_to_vectorspace))
        self.assertEqual(word_to_vectorspace.tolist(),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,
                                              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    def test_05_cluster(self):
        vectorspaced_data = self.reader.vector_spaced_data

        #clusters are always differrent
        clusters = self.clusterer.nltk_cluster(vectorspaced_data)
        self.assertEqual(len(clusters), len(vectorspaced_data))

