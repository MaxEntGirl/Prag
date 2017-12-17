from nltk import FreqDist

class Analyzer(object):
    def __init__(self, text):
        self.text = text
        self.token_counts = FreqDist(text)
    
    def numberOfTokens(self):
        # returns number of tokens in the text
        return len(self.text)
    
    def vocabulary(self):
        # returns a list of the vocabulary of the text sorted alphabetically.
        return sorted(set(self.text))
    
    def vocabularySize(self):
        # returns the size of the vocabulary
        return len(self.vocabulary())
    
    def lexicalRichness(self):
        # returns the lexical richness of the text
        return self.numberOfTokens() / self.vocabularySize()
    
    def hapaxes(self):
        # returns all hapaxes of the text'''
        return self.token_counts.hapaxes()
    
    def numberOfHapaxes(self):
        # returns the number of hapaxes in the text'''
        return len(self.hapaxes())
    
    def avWordLength(self):
        # returns the average word length of the text'''
        sum = 0
        for word in self.token_counts:
            sum = sum + len(word)
        return (int(sum / self.vocabularySize()))

    def topSuffixes(self):
        # returns the 10 most frequent 2-letter suffixes in words'''
        # restrict to words of length 5 or more
        freq = {}
        listsuf = []
        for word in self.vocabulary():
            if len(word) >= 5:
                if word[-2:] in freq:
                    freq[word[-2:]] = freq[word[-2:]] + 1
                else:
                    freq[word[-2:]] = 1

        for key, value in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            listsuf.append(key)

        return listsuf[:10]

    def topPrefixes(self):
        # returns the 10 most frequent 2-letter prefixes in words'''
        # restrict to words of length 5 or more
        freq = {}
        listpre = []
        for word in self.vocabulary():
            if len(word) >= 5:
                if word[:2] in freq:
                    freq[word[:2]] = freq[word[:2]] + 1
                else:
                    freq[word[:2]] = 1

        for key, value in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            listpre.append(key)

        return listpre[:10]
    
    def tokensTypical(self):
        # returns first 5 tokens of the (alphabetically sorted) vocabulary
        # that contain both often seen prefixes and suffixes in the text. Hint: use topPrefixes()
        # and topSuffixes() methods
        toppre = self.topPrefixes()
        topsuf = self.topSuffixes()
        listtoken = []
        for token in self.vocabulary():
            if token[:2] in toppre and token[-2:] in topsuf:
                listtoken.append(token)
        return (listtoken[:5])
        
        
        
        
        
        
        

