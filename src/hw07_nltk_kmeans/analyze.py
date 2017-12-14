from nltk import FreqDist

class Analyzer(object):
    def __init__(self, text):
        self.text = text
        self.token_counts = FreqDist(text)
    
    def numberOfTokens(self):
        #TODO returns number of tokens in the text 
        pass
    
    def vocabulary(self):
        #TODO returns a list of the vocabulary of the text sorted alphabetically.
        pass
    
    def vocabularySize(self):
        #TODO returns the size of the vocabulary
        pass
    
    def lexicalRichness(self):
        #TODO returns the lexical richness of the text
        pass
    
    def hapaxes(self):
        #TODO returns all hapaxes of the text'''
        pass
    
    def numberOfHapaxes(self):
        #TODO returns the number of hapaxes in the text'''
        pass
    
    def avWordLength(self):
        #TODO returns the average word length of the text'''
        pass

    def topSuffixes(self):
        #TODO returns the 10 most frequent 2-letter suffixes in words'''
        #restrict to words of length 5 or more
        pass
    
    def topPrefixes(self):
        #TODO returns the 10 most frequent 2-letter prefixes in words'''
        #restrict to words of length 5 or more
        pass
    
    def tokensTypical(self):
        #TODO returns first 5 tokens of the (alphabetically sorted) vocabulary 
        #that contain both often seen prefixes and suffixes in the text. Hint: use topPrefixes()
        #and topSuffixes() methods
        pass
        
    
        
        
        
        
        
        
        
        

