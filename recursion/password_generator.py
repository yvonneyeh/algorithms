'''
❓ PROMPT
Given a set of characters, a minimum length, and a maximum length, generate all strings that can be created using characters from the set between those lengths inclusively.

This algorithm requires a large time and space complexity to enumerate all the possibilities. You should be able to get this to either time out or run out of memory even on rather small lengths.

Example(s)
generatePasswords(["a"], 2, 4) == [
  "aa",
  "aaa",
  "aaaa",
]

generatePasswords(["a", "b", "c"], 2, 3) == [
  "aa","aaa","aab","aac",
  "ab","aba","abb","abc",
  "ac","aca","acb","acc",
  "ba","baa","bab","bac",
  "bb","bba","bbb","bbc",
  "bc","bca","bcb","bcc",
  "ca","caa","cab","cac",
  "cb","cba","cbb","cbc",
  "cc","cca","ccb","ccc"
]


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the characters list contain duplicates?
A: No, all the characters will be unique for simplicity of not having duplicate outputs.

Q: Can the min length be greater than the max length?
A: No, worst case the min and max lengths are equal.

Q: Can the min and max length be negative or zero?
A: They can both be zero.



Create examples & test cases:

min & max length are the same
min < max length
zero characters
less characters than min length
same number of characters as max length
more characters than max length

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(LmaxLength) where L is the length of the character array
Space: O(LmaxLength) there are L characters to select at each index and there are maxLength indices to store the results. The recursive call stack grows to O(L) frames at most


📆 PLAN
High-level outline of approach #:

The base case is when the length of the password exceeds the max length.
Generated passwords should be saved when the length is between the min and max lengths.
Each recursive step adds one character at a time by looping through the possible characters before recursing to the next index.
When the recursion unwinds, remove the character at the current index so the next loop iteration appends a different character at that index.


🛠️ IMPLEMENT
function generatePasswords(validCharacters, minLength, maxLength) {
def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int) -> list[str]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int) -> list[str]:
  passwords = []
  letters = []

  def make_permutations():

    if len(letters) > maxLength:
      return

    if len(letters) >= minLength and len(letters) <= maxLength:
      passwords.append("".join(letters))

    for i in range(len(validCharacters)):
      letters.append(validCharacters[i])
      make_permutations()
      letters.pop()

  make_permutations()

  return passwords





print(generatePasswords(["a","b","c","d"], 0, 0) == [""])
print(generatePasswords(["a","b","c","d"], 0, 1) == ["","a","b","c","d"])
print(generatePasswords(["a","b","c","d"], 1, 1) == ["a","b","c","d"])
print(generatePasswords(["a","b"], 3, 3) == ["aaa","aab","aba","abb","baa","bab","bba","bbb"])
print(generatePasswords(["a"], 2, 4) == ["aa","aaa","aaaa"])
print(generatePasswords(["a"], 2, 4) == ["aa","aaa","aaaa"])
print(generatePasswords(["a","b","c"], 2, 3) == ["aa","aaa","aab","aac","ab","aba","abb","abc",
  "ac","aca","acb","acc","ba","baa","bab","bac","bb","bba","bbb","bbc",
  "bc","bca","bcb","bcc","ca","caa","cab","cac","cb","cba","cbb","cbc",
  "cc","cca","ccb","ccc"])
print(generatePasswords(["a","b","c","d"], 2, 3) == ["aa","aaa","aab","aac","aad","ab","aba","abb",
  "abc","abd","ac","aca","acb","acc","acd","ad","ada","adb","adc",
  "add","ba","baa","bab","bac","bad","bb","bba","bbb","bbc","bbd",
  "bc","bca","bcb","bcc","bcd","bd","bda","bdb","bdc","bdd","ca",
  "caa","cab","cac","cad","cb","cba","cbb","cbc","cbd","cc","cca",
  "ccb","ccc","ccd","cd","cda","cdb","cdc","cdd","da","daa","dab",
  "dac","dad","db","dba","dbb","dbc","dbd","dc","dca","dcb","dcc",
  "dcd","dd","dda","ddb","ddc","ddd"])

print(len(generatePasswords(["a","b","c","d"], 3, 4)) == 320)
print(len(generatePasswords(["a","b","c","d"], 3, 5)) == 1344)
