import nltk


class LangBigramModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        # Build a ConditionalFrequencyDistribution of bigram character frequencies in the UDHR corpus conditioned on each language
        # hint: use nltk.ConditionalFreqDist
        # cfd = nltk.ConditionalFreqDist()
        # for lang in self.languages:
        #    condition = lang
        #    for word in self.words[lang]:
        #        #print (list(nltk.bigrams(word.lower())))
        #        for bigram in nltk.bigrams(word.lower()):
        #            cfd[condition][bigram] += 1

         cfd = nltk.ConditionalFreqDist((lang, bigram)
         for lang in self.languages
         for word in self.words[lang]
         for bigram in nltk.bigrams(word.lower()))

         return cfd


    def guess_language(self,language_model_cfd, text):
        # Return the guessed language for the given text, score is based on the frequency of bigram characters
        max_score = 0

        for language in language_model_cfd.conditions():

            score = 0  # initialized with 0
            for bigram in nltk.bigrams(text):
                score = language_model_cfd[language].freq(bigram) + score

            if score > max_score:  # check if the score is maximal
                max_language = language  # update the max language
                max_score = score  # update the score
        return max_language  # retrieve the language

