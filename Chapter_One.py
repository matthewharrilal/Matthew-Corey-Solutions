
'''Given two strings write a method to decide if one is a permutation of the other'''

def compare_two_words(word1, word2):
    word1_dictionary = {}
    word2_dictionary = {}
    for letter in word1:
        word1_dictionary[letter] = word1.count(letter)

    for letter in word2:
        word2_dictionary[letter] = word2.count(letter)

    if word1_dictionary.keys()  == word2_dictionary.keys():
       if word1.count(letter) == word2.count(letter):
           return "The words meet the frequency"
       else:
           return "The words do not meet the frequency"
    else:
        return "The words do not have the same letters"


print(compare_two_words("iceman", "cinema"))