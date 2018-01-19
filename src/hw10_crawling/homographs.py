import nltk
from nltk.corpus import inaugural
from collections import defaultdict

def fill_dict(tagged_text):
    #TODO store mapping between words and all the possible POS of this word, use defaultdict

    d = defaultdict(set)
    for word, pos in tagged_text:
        d[word].add(pos)
    return d

def filter_dict(word_dict_h):
    # TODO delete entry, if not a homograph

    for word in dict(word_dict_h).keys():
        if len(word_dict_h[word]) < 2:
            del word_dict_h[word]
    return word_dict_h

def filter_dict_nominalization(word_dict):
    # TODO delete entry, if not a homograph of possible instances of nominalization
    # or denominalization, restricted to the cases where a verb is used as a noun or the other way round.

    for word in dict(word_dict).keys():
        if 'NN' and 'VB' not in word_dict[word]:
            del word_dict[word]
    return word_dict

def find_homographs(tagged_text):
    #TODO return a dictionary to a given tagged text, which hold homographs'''

    dic = fill_dict(tagged_text)
    return filter_dict(dic)









