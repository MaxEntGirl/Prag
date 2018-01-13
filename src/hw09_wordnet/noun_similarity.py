import nltk
from nltk.corpus import wordnet as wn


def get_similarity_scores(pairs):

    #  1. iterate over all combinations of synsets formed by the synsets of the words in the word pair
    #  2. determine the maximum similarity score between synsets
    #  3. save a pair and their score in tuple "max_line"
    #  4. return results in order of decreasing similarity
    # in form ("word1-word2", similarity_value) e.g. ('car-automobile', 1.0)
    # save each tuple with pair and score in "results"


    results = []

    # iterate over all word pairs
    for pair in pairs:
        word1 = wn.synsets(pair[0])
        word2 = wn.synsets(pair[1])
        #print(word1)
        #print(word2)

        max_score = 0.0
        max_line = () #should look like ('food-fruit', 0.1)


        for synset1 in word1:
            for synset2 in word2:
                similarity_value = synset1.path_similarity(synset2)

                if similarity_value is not None:
                    if similarity_value > max_score:
                        max_score = similarity_value
                        max_line = (pair[0] + '-' + pair[1], max_score)
        results.append(max_line)

    return (sorted(results, key=lambda x: x[1], reverse = True))





# this is the ordering that was established experimentally by (Miller & Charles, 1998)
pairs = [('car', 'automobile'), ('gem', 'jewel'), ('journey', 'voyage'),
         ('boy', 'lad'), ('coast', 'shore'), ('asylum', 'madhouse'), ('magician', 'wizard'),
         ('midday', 'noon'), ('furnace', 'stove'), ('food', 'fruit'), ('bird', 'cock'),
         ('bird', 'crane'), ('tool', 'implement'), ('brother', 'monk'), ('lad', 'brother'),
         ('crane', 'implement'), ('journey', 'car'), ('monk', 'oracle'), ('cemetery', 'woodland'),
         ('food', 'rooster'), ('coast', 'hill'), ('forest', 'graveyard'), ('shore', 'woodland'),
         ('monk', 'slave'), ('coast', 'forest'), ('lad', 'wizard'), ('chord', 'smile'), ('glass', 'magician'),
         ('rooster', 'voyage'), ('noon', 'string')]


results = get_similarity_scores(pairs)
