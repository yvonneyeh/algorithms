'''
❓ PROMPT
Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

Example(s)
pairStars("hello") == "hel*lo"
pairStars("xxyy") == "x*xy*y"
pairStars("aaaa") == "a*a*a*a"


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the string be empty or null?
A: Empty but not null.
Q: Can there be capital letters, special characters, and numbers?
A: There can all kinds of different characters.


Create examples & test cases:

empty string
1-character string
2-character strings
string with no adjacent characters
string with all the same character
string with a mixture of adjacent and non-adjacent characters

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:

Time: O(L) where L is the length of the larger string

Space:
O(L) where L is the length of the larger string to create each stack frame.
O(L2) if slicing the string on each recursive step


📆 PLAN
High-level outline of approach #:

Base case = empty string


🛠️ IMPLEMENT
function pairStars(word) {
def pairStars(word: str) -> str:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

# String slicing
def pairStars(word: str) -> str:
  if len(word) <= 1:
    return word

  if word[0] == word[1]:
    return str(word[0]) + "*" + pairStars(word[1:])

  return str(word[0]) + pairStars(word[1:])

# Without string slicing
def pairStars(word: str, index=0) -> str:
  if index == len(word):
      return ""

  substring = pairStars(word, index + 1)

  if len(substring) > 0 and word[index] == substring[0]:
    return word[index] + "*" + substring

  return word[index] + substring

# Alternative
def pairStars(word: str, index=0) -> str:
  if len(word) <= 1:
    return word

  if index == len(word)-1:
    return word[index]

  if word[index] == word[index+1]:
    return word[index] + "*" + pairStars(word, index + 1)

  return word[index] + pairStars(word, index + 1)


print(pairStars("hello") == "hel*lo")
print(pairStars("xxyy") == "x*xy*y")
print(pairStars("aaaa") == "a*a*a*a")
print(pairStars("aaab") == "a*a*ab")
print(pairStars("aa") == "a*a")
print(pairStars("a") == "a")
print(pairStars("") == "")
print(pairStars("noadjacent") == "noadjacent")
print(pairStars("abba") == "ab*ba")
print(pairStars("abbba") == "ab*b*ba")
