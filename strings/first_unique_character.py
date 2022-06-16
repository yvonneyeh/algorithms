# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

import collections

# Approach 1

# create a dictionary
# check if character exists as a key in the dictionary
# if not, add it
# if yes, increment
# loop through word and check which index is the first unique character

def get_first_unique_character(word):
    frequency = {}
    for character in word:
        if character not in frequency:
            frequency[character] = 1
        else:
            frequency[character] += 1

    print(frequency)

    for i in range(len(word)):
        if frequency[word[i]] == 1:
            return i

print(get_first_unique_character('apple'))

# Approach 2

def get_first_unique_character_with_counter(word):
    # build hash map : character and how often it appears
    count = collections.Counter(word) # ← gives back a dictionary with words occurrence count
                                    #Counter({'a': 1, 'p': 2, 'l': 1, 'e': 1})
    # find the index
    for idx, character in enumerate(word):
        if count[character] == 1:
            return idx
    return -1

print(get_first_unique_character_with_counter('alphabet'))
