import nltk
from nltk.corpus import inaugural
from collections import defaultdict

def fill_dict(tagged_text):
    #TODO store mapping between words and all the possible POS of this word, use defaultdict
    pass

def filter_dict(word_dict_h):
    for word in dict(word_dict_h).keys():
        #TODO delete entry, if not a homograph
        pass
    

def filter_dict_nominalization(word_dict):
    for word in dict(word_dict).keys():
        #TODO delete entry, if not a homograph of possible instances of nominalization
        #or denominalization, restricted to the cases where a verb is used as a noun or the other way round.
        pass
    

def find_homographs(tagged_text):
    #TODO return a dictionary to a given tagged text, which hold homographs'''
    pass







