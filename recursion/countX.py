'''
❓ PROMPT
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

Example(s)
countX("xxhixx") == 4
countX("xhixhix") == 3
countX("hi") == 0


🔎 EXPLORE
State your assumptions & discoveries:


Q: Can the string be empty or null?
A: Empty but not null.
Q: Can there be capital letters, special characters, and numbers?
A: There can all kinds of different characters.
Q: How should capital X be handled?
A: Don't count capital Xs.


Create examples & test cases:

empty string
single character strings
string with capitalized X
string with all x's
string with no x's
string with a mixture of x's and other characters


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(L) where L is the length of the string
Space: O(L) where L is the length of the string when using an index or O(L^2) when slicing new strings


📆 PLAN
High-level outline of approach #:
The base case is when the input is an empty string.



🛠️ IMPLEMENT
function countX(word) {
def countX(word: str) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def countX(word: str) -> int:

    if not word:
        return 0

    if word[0] == "x":
        return countX(word[1:]) + 1

    return countX(word[1:])

print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hiX") == 0)
print(countX("XXXhXXX") == 0)
print(countX("x") == 1)
print(countX("") == 0)
print(countX("hihi") == 0)
print(countX("hiAAhi12hi") == 0)
