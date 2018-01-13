import nltk
from nltk.corpus import wordnet as wn

def average_polysemy(part_of_speech):

    # 1. aggregate all lemmas in wordnet that have the given POS (hint: use nltk.corpus.wordnet.all_lemma_names)
    # 2. sum the number of meanings of each lemma (restricted to the given POS)
    # 3. return the average polysemy of a given POS

    all_lemmas = set(wn.all_lemma_names(part_of_speech))
    #print(len(all_lemmas))

    meanings_length = 0
    for lemma in all_lemmas:
        meanings = wn.synsets(lemma, part_of_speech)
        meanings_length = meanings_length + len(meanings)

    return meanings_length / len(all_lemmas)

    #print(meanings)


if  __name__ =='__main__':
    print("average polysemy of nouns:",      average_polysemy('n')) 
    print("average polysemy of verbs:",      average_polysemy('v')) 
    print("average polysemy of adjectives:", average_polysemy('a')) 
    print("average polysemy of adverbs:",    average_polysemy('r')) 
