import string

class LeskSimilarity(object):
    def __init__(self, synset1, synset2):
        self.synset1 = synset1
        self.synset2 = synset2
        self.punctuation = string.punctuation

    def get_overlap(self,definition_words1, definition_words2):
        #TODO find overlap in definitions, consider words occuring twice
        pass
    
    def get_max_match(self,definition_words1, definition_words2):
        #TODO calculate maximum matching number (length of shortest definition)
        pass
    
    def get_definition_words(self, synset):
        #TODO find tokens of wordnet definition of synset, ignore punctuation
        pass
    
    def score(self):
        #TODO calculate lesk similarity, use methods defined in the class
        #definition_words1 = ...
        #definition_words2 = ...
        #max_match = ...
        #overlap = ...
        #return overlap/max_match
        pass
