from unittest import TestCase
from hw08_lang_guesser.model_lang import LangModeler
from hw08_lang_guesser.model_bigram_lang import LangBigramModeler
from nltk.corpus import udhr
#run with  python3 -m unittest -v hw08_lang_guesser/test_lang_guesser.py

class LangGuesserTest(TestCase):

    def setUp(self):
        languages = ['English', 'German_Deutsch', 'French_Francais']

        # udhr corpus contains the Universal Declaration of Human Rights in over 300 languages
        language_base = dict((language, udhr.words(language + '-Latin1')) for language in languages)
        # build the language models
        self.langModeler = LangModeler(languages, language_base)

        self.langBigramModeler = LangBigramModeler(languages, language_base)

    def test_01_models(self):
        language_model_cfd = self.langModeler.build_language_models()
        outcomes = list(language_model_cfd['English'].items())
        
        self.assertTrue(('u', 183) in outcomes) 
        self.assertTrue(('n', 668) in outcomes)
        self.assertTrue(('i', 652) in outcomes)

    def test_02_guess(self):
        text1 = "Peter had been to the office before they arrived."
        text2 = "Si tu finis tes devoirs, je te donnerai des bonbons."
        text3 = "Das ist ein schon recht langes deutsches Beispiel."
        language_model_cfd = self.langModeler.build_language_models()

        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text1), 'German_Deutsch')
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text2), 'French_Francais')
        self.assertEqual(self.langModeler.guess_language(language_model_cfd, text3), 'German_Deutsch')

    def test_03_bigram_models(self):
        language_model_bigram_cfd = self.langBigramModeler.build_language_models()
        outcomes = list(language_model_bigram_cfd['English'].items())
        self.assertTrue((('u', 'n'), 41) in outcomes) 
        self.assertTrue((('n', 'i'), 32) in outcomes)
        self.assertTrue((('i', 'v'), 21) in outcomes)

    def test_04_bigr_bigram_guess(self):
        text1 = "Peter had been to the office before they arrived."
        text2 = "Si tu finis tes devoirs, je te donnerai des bonbons."
        text3 = "Das ist ein schon recht langes deutsches Beispiel."
        language_model_bigram_cfd = self.langBigramModeler.build_language_models()

        self.assertEqual(self.langBigramModeler.guess_language(language_model_bigram_cfd, text1), 'English')
        self.assertEqual(self.langBigramModeler.guess_language(language_model_bigram_cfd, text2), 'French_Francais')
        self.assertEqual(self.langBigramModeler.guess_language(language_model_bigram_cfd, text3), 'German_Deutsch')

