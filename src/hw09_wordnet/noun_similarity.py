import nltk


def get_similarity_scores(pairs):
    results = []

    # iterate over all word pairs
    for pair in pairs:

        max_score = 0.0
        max_line = () #should look like ('food-fruit', 0.1)

        #TODO 1. iterate over all combinations of synsets formed by the synsets of the words in the word pair
        #TODO 2. determine the maximum similarity score between synsets
        #TODO 3. save a pair and their score in tuple "max_line"
        #in form ("word1-word2", similarity_value) e.g. ('car-automobile', 1.0)

        #save each tuple with pair and score in "results"
        results.append(max_line)

        
    #TODO 4. return results in order of decreasing similarity
    pass



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
