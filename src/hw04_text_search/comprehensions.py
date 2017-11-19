# This exercise contains 5 Tasks to practice a powerful feature of Python: comprehensions.
# With these, multiple-line for-loop constructions can be expressed in expressive one-liners.

orig = [1,2,5,7,6,3,9,0,5,4,3,4,7,2,5,4,7,6,8,5,0]
wordlist = "diese Übungsaufgabe behandelt Comprehensions in Python und ist gar nicht so schwer".split()

def increase(liste):
    # Task 1: Using a list comprehension, increase each value in orig by 2.
    list1 = []
    return(list1)

def unevenSquares(liste):
    # Task 2: Using a list comprehension, create a list that contains the squares of all uneven numbers in orig.
    list2 = []
    return(list2)

def elevated(liste):
    # Task 3: Using a list comprehension, create a list that contains the squares of the uneven numbers
    # and the fivefold (das Fünffache) of the even numbers in orig.
    list3 = []
    return(list3)

def cube_dict(liste):
    # Task 4: Using a dictionary comprehension, create a mapping from the cubes of the values in orig 
    # to the values themselves. 
    cubed = {}
    return(cubed)

def noun_len(liste):
    # Task 5: Using a dictionary comprehension, create a mapping from all elements of wordlist that start
    # with an uppercase letter to their respective length.
    nouns_to_length = {}
    return(nouns_to_length)



if  __name__ =='__main__':
    list1 = increase(orig)
    list1 = unevenSquares(orig)
    list1 = elevated(orig)
    dict1 = cube_dict(orig)
    dict2 = noun_len(wordlist)