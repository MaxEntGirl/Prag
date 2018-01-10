from unittest import TestCase
from nltk.corpus import wordnet as wn
from hw09_wordnet.noun_similarity import get_similarity_scores
from hw09_wordnet.average_polysemy import average_polysemy
from hw09_wordnet.lesk_sim import LeskSimilarity
import warnings

#run with python3 -m unittest -v hw09_wordnet/test_wordnet.py

class WordnetTest(TestCase):
    
    
    def setUp(self):
        warnings.simplefilter("ignore")
        self.lesk_sim = LeskSimilarity(wn.synset('car.n.01'),wn.synset('wheel.n.01'))
        
    def test_01_noun_similarity(self):
        
        pairs = [('car', 'automobile'), ('gem', 'jewel'), ('journey', 'voyage'),
                 ('boy', 'lad'), ('coast', 'shore'), ('asylum', 'madhouse'), ('magician', 'wizard'),
                 ('midday', 'noon'), ('furnace', 'stove'), ('food', 'fruit'), ('bird', 'cock'),
                 ('bird', 'crane'), ('tool', 'implement'), ('brother', 'monk'), ('lad', 'brother'),
                 ('crane', 'implement'), ('journey', 'car'), ('monk', 'oracle'), ('cemetery', 'woodland'),
                 ('food', 'rooster'), ('coast', 'hill'), ('forest', 'graveyard'), ('shore', 'woodland'),
                 ('monk', 'slave'), ('coast', 'forest'), ('lad', 'wizard'), ('chord', 'smile'), ('glass', 'magician'),
                 ('rooster', 'voyage'), ('noon', 'string')]
        results = get_similarity_scores(pairs)
        self.assertEqual(results[0],('car-automobile', 1.0))
        self.assertEqual(results[4],('journey-voyage', 0.5))
        self.assertEqual(results[-5],('food-fruit', 0.1))

    def test_02_average_polysemy(self):
        self.assertEqual(round(average_polysemy('n'),2),1.26)
        self.assertEqual(round(average_polysemy('v'),2),2.19)
        self.assertEqual(round(average_polysemy('a'),2),1.41)
        self.assertEqual(round(average_polysemy('r'),2),1.25)

    def test_03_definition_words(self):
        definition = self.lesk_sim.get_definition_words(wn.synset('car.n.01'))
        self.assertEqual(definition,['a', 'motor', 'vehicle', 'with', 'four', 'wheels;', 'usually',
                                'propelled', 'by', 'an', 'internal', 'combustion', 'engine'])

    def test_04_max_match(self):
        def1 = ['a', 'motor', 'vehicle', 'with', 'four', 'wheels;', 'usually',
                'propelled', 'by', 'an', 'internal', 'combustion', 'engine']
        def2 = ['a', 'vehicle', 'that', 'takes', 'people', 'to', 'and', 'from', 'hospitals']
        max_match = self.lesk_sim.get_max_match(def1,def2)
        self.assertEqual(max_match,9)

    def test_05_overlap(self):
        def1 = ['a', 'motor', 'vehicle']
        def2 =  ['a', 'vehicle', 'that', 'takes', 'people']

        def_test1 = ['test', 'test', 'test']
        def_test2 =  ['test', 'test']
        
        self.assertEqual(self.lesk_sim.get_overlap(def1,def2), 2)
        self.assertEqual(self.lesk_sim.get_overlap(def_test1,def_test2), 2)
        
    def test_06_lesk_similarity(self):
        similarity = self.lesk_sim.score()
        self.assertEqual(round(similarity,2),0.15)
        
    
