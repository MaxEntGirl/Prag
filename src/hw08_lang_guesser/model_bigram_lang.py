import nltk


class LangBigramModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        #TODO Build a ConditionalFrequencyDistribution of bigram character frequencies in the UDHR corpus conditioned on each language
        #hint: use nltk.ConditionalFreqDist
        pass
        


    def guess_language(self,language_model_cfd, text):
        #TODO Return the guessed language for the given text, score is based on the frequency of bigram characters 
         pass

