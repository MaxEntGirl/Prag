from unittest import TestCase
import nltk
from hw10_crawling.homographs import *

import warnings

#run with python3 -m unittest -v hw10_crawling/test_homographs.py



class WordnetTest(TestCase):
    
    def setUp(self):
        warnings.simplefilter("ignore")
        self.tagged_text = nltk.pos_tag(inaugural.words("2009-Obama.txt"));
        self.test_tagged_text =[('I', 'PRP'), ('play', 'VB'), ('here', 'RB'), ('in', 'IN'),
                                ('the', 'DT'), ('future', 'NN'), ('humbled', 'VBN'), ('by', 'IN'),
                                ('the', 'DT'), ('future', 'JJ'), ('play', 'NN')]

    def test_01_fill_dict(self):
        wordTagsDict = fill_dict(self.test_tagged_text) 
        self.assertEqual(wordTagsDict["future"], {'JJ', 'NN'})
        self.assertEqual(len(wordTagsDict),8)
        
    def test_02_filter_dict(self):
        wordTagsDict = fill_dict(self.test_tagged_text)
        filter_dict(wordTagsDict)
        self.assertEqual(len(wordTagsDict),2)
        
    def test_03_filter_dict_nominalization(self):
        wordTagsDict = fill_dict(self.test_tagged_text)
        filter_dict_nominalization(wordTagsDict)
        self.assertEqual(list(wordTagsDict.keys()),['play'])
        self.assertEqual(len(wordTagsDict),1)
        
    def test_04_homographs(self):
        homographs = find_homographs(self.tagged_text)
        self.assertTrue("American" in homographs)
        self.assertTrue("work" in homographs)
        self.assertTrue("play" in homographs) 
                



