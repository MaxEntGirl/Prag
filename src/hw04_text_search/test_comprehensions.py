import unittest
from hw04_text_search.comprehensions_solution import *

class TestComprehensions(unittest.TestCase):

    def setUp(self):
        self.orig = [1,2,5,7,6,3,9,0,5,4,3,4,7,2,5,4,7,6,8,5,0]
        self.wordlist = "diese Übungsaufgabe behandelt Comprehensions in Python und ist gar nicht so schwer".split()

    def testIncrease(self):
        self.assertEqual(increase(self.orig[:4]), [3,4,7,9])

    def testUnevenSquares(self):
        self.assertEqual(unevenSquares(self.orig[:4]), [1,25,49])

    def testElevated(self):
        self.assertEqual(elevated(self.orig[:4]), [1,10,25,49])

    def testCube_dict(self):
        self.assertEqual(cube_dict(self.orig[:4]), {1:1, 8:2, 125:5, 343:7})

    def testNoun_len(self):
        self.assertEqual(noun_len(self.wordlist[:4]), {'Übungsaufgabe':13, 'Comprehensions':14})

