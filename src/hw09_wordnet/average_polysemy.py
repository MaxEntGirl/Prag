import nltk

def average_polysemy(part_of_speech):

    #TODO 1. aggregate all lemmas in wordnet that have the given POS (hint: use nltk.corpus.wordnet.all_lemma_names)
    #TODO 2. sum the number of meanings of each lemma (restricted to the given POS)
    #TODO 3. return the average polysemy of a given POS
    pass

if  __name__ =='__main__':
    print("average polysemy of nouns:",      average_polysemy('n')) 
    print("average polysemy of verbs:",      average_polysemy('v')) 
    print("average polysemy of adjectives:", average_polysemy('a')) 
    print("average polysemy of adverbs:",    average_polysemy('r')) 
