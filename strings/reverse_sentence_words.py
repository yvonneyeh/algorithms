# Given a sentence, reverse the words of the sentence.
# Example,"i live in a house" becomes "house a in live i"''

# Input: string of words with spaces in between
# output: ``
# edge cases: empty string, string of only spaces

# traverse the string, separate all the words by looking for the spaces
# add words to a new array
# reverse the array
# join the elements in the array separated by a space

def reverse_sentence(sentence):
    if sentence == "":
        return 0
    word_list = sentence.split(" ")
    word_list = word_list[::-1]
    return " ".join(word_list)

    # (word_list.join(" "))

s1 = "i live in a house"
s2 = ""
s3 = "   "
print(reverse_sentence(s1))
print(reverse_sentence(s2))
print(reverse_sentence(s3))

# 151. Reverse Words in a String

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])

    # no built in functions

    def reverse_words(s):
        # @param s, a string
        # @return a string
        # First reverse entire string, then iterate over reversed string
        # and again reverse order of characters within a word. Append each word to words.
        word = ""
        words = ""
        s = s[::-1]
        for j, i in enumerate(s):
            # character is not space, a current word exists,
            # and previous character is space, e.g. i=b in " a b":
            if i != " " and word != "" and s[j-1] == " ":
                # add current word to words and append " " to later add this i
                words += (word + " ")
                word = i
            # character is not space, but it's either first character in string
            # or is part of current word, e.g. i=b in "b", " b" "ab", "a ab "
            elif i != " ":
                word = i + word
            else:
                continue

        words += word

        return(words)

    def reverse_words_2_pointers(self, s: str) -> str:
        res = ""
        s = " " + s + " "
        start = end = -1
        for i in range(len(s) - 2, 0, -1):
            if s[i + 1] == " " and s[i] != " ":
                end = i
            if s[i - 1] == " " and s[i] != " ":
                start = i
                res = res + " " + s[start: end + 1]
        return res[1:]
