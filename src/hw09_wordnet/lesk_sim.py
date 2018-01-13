import string
import nltk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize

class LeskSimilarity(object):
    def __init__(self, synset1, synset2):
        self.synset1 = synset1
        self.synset2 = synset2
        self.punctuation = string.punctuation

    def get_overlap(self,definition_words1, definition_words2):
        # find overlap in definitions, consider words occuring twice

        if len(definition_words2) > len(definition_words1):
            count_overlap = 0
            for token in definition_words1:
                if token in definition_words2:
                    count_overlap += 1

            return count_overlap
        else:
            count_overlap = 0
            for token in definition_words2:
                if token in definition_words1:
                    count_overlap += 1

            return count_overlap

    
    def get_max_match(self,definition_words1, definition_words2):
        # calculate maximum matching number (length of shortest definition)
        if len(definition_words1) > len(definition_words2):
            return len(definition_words2)
        else:
            return len(definition_words1)
    
    def get_definition_words(self, synset):
        # find tokens of wordnet definition of synset, ignore punctuation
        token_list = []
        for token in synset.definition().split(" "):
            if token not in self.punctuation:
                token_list.append(token)

        return token_list
    
    def score(self):
        # calculate lesk similarity, use methods defined in the class
        definition_words1 = self.get_definition_words(self.synset1)
        definition_words2 = self.get_definition_words(self.synset2)
        max_match = self.get_max_match(definition_words1, definition_words2)
        overlap = self.get_overlap(definition_words1, definition_words2)
        return overlap/max_match

