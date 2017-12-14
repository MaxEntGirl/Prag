from unittest import TestCase
from hw07_nltk_kmeans.analyze import Analyzer
from nltk.corpus import gutenberg
from nltk.text import Text
#run with  python3 -m unittest -v hw07_nltk_kmeans/test_analyzer.py

class AnalyzerTest(TestCase):

    def setUp(self):
        
        text = Text(gutenberg.words("melville-moby_dick.txt"))
        self.analyzer = Analyzer(text)  
        
    def test_01_numberOfTokens(self):
        self.assertEqual(self.analyzer.numberOfTokens(), 260819) 

    def test_02_vocabulary(self):
        true_list = ['zodiac', 'zone', 'zoned', 'zones', 'zoology']
        self.assertEqual(self.analyzer.vocabulary()[-5:],true_list) 
        
    def test_03_size(self):
        self.assertEqual(self.analyzer.vocabularySize(),19317) 
    
    def test_04_richness(self):
        self.assertEqual(int(self.analyzer.lexicalRichness()),13)
        
    def test_05_hapaxes(self):
        hapaxes = ['zig', 'zoned', 'zoology']
        self.assertTrue(sorted(self.analyzer.hapaxes())[-3:], hapaxes) 
        
    def test_06_numberOfHapaxes(self):
        self.assertEqual(self.analyzer.numberOfHapaxes(),9002) 
        
    def test_07_avWordLength(self):
        self.assertEqual(int(self.analyzer.avWordLength()),7)

    def test_08_topSuffixes(self):
        topSuffixes = ['ed', 'ng', 'es', 'ly', 'er', 'on', 'ss', 'le', 'rs', 'ts']
        self.assertEqual(self.analyzer.topSuffixes(),topSuffixes) 
        
    def test_09_topPrefixes(self):
        topPrefixes = ['co', 'in', 're', 'un', 'pr', 'st', 'de', 'di', 'su', 'ma']
        self.assertEqual(self.analyzer.topPrefixes(),topPrefixes) 

    def test_10_tokensTypical(self):
        typical = ['coaches', 'coalescing', 'coasting', 'coasts', 'coated']
        self.assertEqual(self.analyzer.tokensTypical(),typical)
        
     
