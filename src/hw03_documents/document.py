from nltk import FreqDist, word_tokenize
def normalized_tokens(text):
    """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
    # return list with lower-case tokens.
    text = text.lower()
    return word_tokenize(text)

class TextDocument:
    def __init__(self, text, id=None):
        """ This creates a from a string and an identifier. """
        self.text = text
        self.word_to_count = FreqDist(normalized_tokens(text)) #Create dictionary from words to counts.
        self.id = id

    @classmethod
    def from_file(cls, filename):
        """ This creates a TextDokument by reading a file. """
        # read text from filename
        file = open(filename)
        text = file.read()
        file.close()
        return cls(text, filename)

    def __str__(self):
        """ This returns a short string representation, which is at most 25 characters long.
        If the original text is longer than 25 characters, the last 3 characters of the short string should be '...'.
        """
        # Implement correct return statement.
        if len(self.text) <= 24:
            return self.text[0:24]
        else :
            return self.text[0:22] + '...'

    def word_overlap(self, other_doc):
        """ This returns the number of words that occur in both of the documents (self and other_doc) at the same time.
        Every word should be considered only once, irrespective of how often it occurs in either document (i.e. we
        consider word *types*).
        """
         # Implement correct return statement.
        count = 0
        for key in self.word_to_count:
            if key in other_doc.word_to_count:
                count += 1
        return count