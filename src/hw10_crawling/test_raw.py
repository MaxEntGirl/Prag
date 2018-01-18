from unittest import TestCase
import nltk
from hw10_crawling.raw import *

import warnings

#run with python3 -m unittest -v hw10_crawling/test_raw.py



class WordnetTest(TestCase):
    
    def setUp(self):
        warnings.simplefilter("ignore")
        self.url = "http://www.scientificamerican.com/article.cfm?id=how-supercomputers-will-yield-a-golden-age-of-materials-science"
        self.text = "Dr. Leeroy Jenkins acquired his Ph.D in 2005; afterwards, he continued his work at MIT for two more years. His approach, by many dubbed 'just-go-ahead-and-don't-wait', revolutionized payment methods, lowering transfer costs to less than .02$ per shipment."
        self.stemtext = "his free time was fully devoted to fishing."
        self.lemmatext = "the decolonization of unknowingly underdeveloped countries is a grievious flaw in the politics of the 70s."


    def test_01_get_text(self):
        paragraphs = get_text(self.url)
        p = 'With supercomputers and the equations of quantum mechanics, scientists are designing new materials atom by atom, before ever running an experiment'
        self.assertEqual(paragraphs[1],p) 

    def test_02_make_text(self): 
        self.assertIsInstance(make_text(self.text), nltk.Text)
        self.assertEqual(make_text(self.text)[:8], ['Dr.', 'Leeroy', 'Jenkins', 'acquired', 'his', 'Ph.D', 'in', '2005'])
        self.assertEqual(len(make_text(self.text)), 46)

    def test_03_stem_porter(self):
        self.assertEqual(stem_porter(self.stemtext.split()), "hi free time wa fulli devot to fishing.".split())

    def test_04_stem_lancaster(self):
        self.assertEqual(stem_lancaster(self.stemtext.split()), "his fre tim was ful devot to fishing.".split())

    def test_05_lower(self):
        self.assertEqual(lower(nltk.Text(self.text.split()))[:8], ['dr.', 'leeroy', 'jenkins', 'acquired', 'his', 'ph.d', 'in', '2005;'])

    def test_06_lemmatize(self):        
        self.assertIsInstance(lemmatize(self.lemmatext.split()), list)
        self.assertEqual(lemmatize(self.lemmatext.split())[:6], "the decolonization of unknowingly underdeveloped country".split())

    def test_07_content(self):
        self.assertEqual(len(self.text.split()), 37)
        self.assertEqual(len(content(self.text.split())), 27)
        



