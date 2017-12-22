import nltk


class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        # build a ConditionalFrequencyDistribution of character frequencies in the UDHR corpus conditioned on each language
        # hint: use nltk.ConditionalFreqDist

        #cfd = nltk.ConditionalFreqDist()
        #for lang in self.languages:
        #    condition = lang
        #    for word in self.words[lang]:
        #        for charact in word:
        #            cfd[condition][charact.lower()] += 1

        cfd = nltk.ConditionalFreqDist((lang, charact)
        for lang in self.languages
        for word in self.words[lang]
        for charact in word.lower())
      # print(cfd["English"].freq("u"))
        return cfd

    def guess_language(self,language_model_cfd, text):
        """Returns the guessed language for the given text"""
        max_score = 0

        for language in language_model_cfd.conditions():

            score = 0 #initialized with 0
            for char in text:
                score = language_model_cfd[language].freq(char) + score

            # for each language update the score of a given text
            # based on the frequency of characters accessible by language_model_cfd[language].freq(character)

            # identify most likely language for a given text according to the score
            if score > max_score: # check if the score is maximal
                max_language = language # update the max language
                max_score = score # update the score
        return max_language # retrieve the language

