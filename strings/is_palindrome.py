# Given a string, check if it's a palindrome (same read forwards and backwards)

# Are letters case sensitive? If so, convert all to lowercase first

def is_palindrome_reverse(s):
    s = s.lower()
    return s == reversed(s)

def is_palindrome_slice_notation(s):
    return s == s[::-1]

def is_palindrome_(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
# Time complexity: O(n)
# Auxiliary Space: O(1)


# Palindrome permutation:

"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cat", etc.)

I: String
O: Boolean
C: optimize
E: empty string, even and odd chars, spaces between and in front and at end, more than 2 of the same char
time complexity: linear
space complexity: linear
"""

def is_palindrome_permutation_pythonic(phrase):
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1

def is_palindrome_permutation(s):
    
