# The first chapter of the crackin the coding interview questions
from itertools import permutations

def permutations_method(word):
    perms = [''.join(p) for p in permutations(word)]



# Essentially what is happening is that we are checking if we are given two words if one of the words are a permutation of the other therefore
# we essentially compare all the permutations
