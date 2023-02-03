"""
1. Reverse Letters in Words

In this variation, keep the order of the words the same, but reverse the letters within each word.

Ex. “Reverse the words in this string” returns “esreveR eht sdrow ni siht gnirts”
"""

def reverse_letters_in_words(words):
    result = []

    for word in words.split():
        result.append(word[::-1])

    return " ".join(result)

    # return " ".join([word[::-1] for word in words.split()])


print(reverse_letters_in_words("Reverse the words in this string"))

"""
2. Rotate words by x

In this variation we will rotating the words by k positions. If k = 1, move all words 1 to the right and the last word should move to the beginning.

Ex. “Rotate the words in this string”, k = 1 returns “string Rotate the words in this”

Ex. “Rotate the words in this string”, k = 2 returns “this string Rotate the words in”

Ex. “Rotate the words in this string”, k = 3 returns “in this string Rotate the words”

Ex. “Rotate the words in this string”, k = 6 returns “Rotate the words in this string”

Ex. “Rotate the words in this string”, k = 7 returns “string Rotate the words in this”
"""

def rotate_words_by_x(words, k):

    if not words:
        return ""

    word_list = words.split()
    i = 0

    while i < len(word_list):
        l = i
        r = i + k + 1

        while l < r:
            word_list[l], word_list[r] = word_list[r], word_list[l]
            l += 1
            r -= 1

        i + k

    return " ".join(word_list)

"""
3. Rotate array

In this variation, you will be receiving an array of Int, where the number 0 represents a word break. Reverse all the elements between the 0s.

Ex. [1, 2, 3, 0, 4, 5, 6] returns [3, 2, 1, 0, 6, 5, 4] (1, 2, 3 and 4, 5, 6 were the two chunks that were reversed)

Ex. [1, 2, 3, 4, 5, 6] returns [6, 5, 4, 3, 2, 1] (since there are no zeroes, the entire array is considered one chunk)

Ex. [1, 0, 2, 0, 3] returns [1, 0, 2, 0, 3] (Since all the chunks size 1, no change happens)


Approach:
- find 0 in array
- get index of 0
"""


def rotate_array(array):

    # pivot = array.index(0)

    pivot = None

    for item in array:
        if item == 0:
            pivot = item

    def rotate(array, l, r):
        while l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    if not pivot:
        rotate(array, 0, len(array) - 1)

    l = 0
    r = pivot - 1
    rotate(array, l, r)

    l = pivot + 1
    r = len(array) - 1
    rotate(array, l, r)

    return array

print(rotate_array([1, 2, 3, 0, 4, 5, 6])) # [3, 2, 1, 0, 6, 5, 4]
print(rotate_array([1, 2, 3, 4, 5, 6])) # [6, 5, 4, 3, 2, 1]
print(rotate_array([1, 0, 2, 0, 3])) # [1, 0, 2, 0, 3]




"""
4. Reverse letters in k chunks

Given an array and a k, reverse letters in this string in k chunks. Assume that the string will be evenly divisible by k.

Ex. “abcdef”, k = 2 returns “badcfe” (there are 3 chunks of length 2 that are reversed)

Ex. “abcdef”, k = 3 returns “cbafed”

Ex. “abcdef”, k = 6 returns “fedcba”

Ex. “abcdefgh”, k = 4 returns “dcbahgfe”
"""

def reverse_letters_groups(letters, k):
    pass
