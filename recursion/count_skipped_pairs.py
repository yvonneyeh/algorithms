'''
❓ PROMPT
We'll say that a "skipped pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 skipped pairs -- 2 for A and 1 for x. Recursively compute the number of skipped pairs in the given string.

Example(s)
countSkippedPairs("axa") == 1
countSkippedPairs("axax") == 2
countSkippedPairs("aaa") == 1


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the string be empty or null?
A: Empty but not null.
Q: Can there be capital letters, special characters, and numbers?
A: There can all kinds of different characters.

Create examples & test cases:

empty string
single character string
2-character string
3-character strings
strings with alternating characters
strings with overlapping pairs
strings of all the same character
repeated 2-character strings
mixture of adjacent, random, and alternating characters


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(L) where L is the length of the string
Space: O(L) where L is the length of the string when using an index or O(L^2) when slicing new strings


📆 PLAN
High-level outline of approach #:

The base case is when the input is less than 3 characters.



🛠️ IMPLEMENT
function countSkippedPairs(word) {
def countSkippedPairs(word: str) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

# creating new strings

def countSkippedPairs(word: str) -> int:
    if len(word) <= 2:
        return 0

    if word[0] == word[2]:
        return countSkippedPairs(word[1:]) + 1

    return countSkippedPairs(word[1:])

# index, in place

def countSkippedPairs(word: str) -> int:

    def count(word, index = 0):
        if len(word) <= index + 2:
            return 0

        if word[index] == word[index+2]:
            return count(word, index + 1) + 1

        return count(word, index+1)

    return count(word)


print(countSkippedPairs("axa") == 1)
print(countSkippedPairs("axax") == 2)
print(countSkippedPairs("axbx") == 1)
print(countSkippedPairs("hi") == 0)
print(countSkippedPairs("hihih") == 3)
print(countSkippedPairs("ihihhh") == 3)
print(countSkippedPairs("ihjxhh") == 0)
print(countSkippedPairs("") == 0)
print(countSkippedPairs("a") == 0)
print(countSkippedPairs("aa") == 0)
print(countSkippedPairs("aaa") == 1)


print(countSkippedPairs("axa") == 1)
print(countSkippedPairs("axax") == 2)
print(countSkippedPairs("axbx") == 1)
print(countSkippedPairs("hi") == 0)
print(countSkippedPairs("hihih") == 3)
print(countSkippedPairs("ihihhh") == 3)
print(countSkippedPairs("ihjxhh") == 0)
print(countSkippedPairs("") == 0)
print(countSkippedPairs("a") == 0)
print(countSkippedPairs("aa") == 0)
print(countSkippedPairs("aaa") == 1)
