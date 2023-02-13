'''
❓ PROMPT
Given a string that contains exactly 1 pair of parentheses, compute recursively a new string made of only the parentheses and their contents, so "xyz(abc)123" yields "(abc)".

Example(s)
parenBit("xyz(abc)123") == "(abc)"
parenBit("x(hello)") == "(hello)"
parenBit("(xy)1") == "(xy)"


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the input be an empty string or null?
A: Empty but not null
Q: Can there be nothing inside the parentheses?
A: Yes

Create examples & test cases:

empty string
only the () parentheses
empty ( parentheses with content outside
only content inside the parentheses
content both inside and outside the parentheses


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(L) where L is the length of the string
Space: O(L2) where L is the length of the string to create each stack frame and to concatenate and slice a new length L string on each frame


📆 PLAN
High-level outline of approach #:

The base case is when the input has the opening parenthesis at the start and the closing parenthesis at the end.


🛠️ IMPLEMENT
function parenBit(word) {
def parenBit(word: str) -> str:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def parenBit(word: str) -> str:

  if word[0] == '(' and word[len(word) - 1] == ')':
    return word

  if word[0] == '(':
    return parenBit(word[0:len(word) - 1])

  if word[len(word) - 1] == ')':
    return parenBit(word[1:])

  return parenBit(word[1:len(word) - 1])



print(parenBit("xyz(abc)123") == "(abc)")
print(parenBit("x(hello)") == "(hello)")
print(parenBit("(xy)1") == "(xy)")
print(parenBit("not really (possible)") == "(possible)")
print(parenBit("(abc)") == "(abc)")
print(parenBit("(abc)xyz") == "(abc)")
print(parenBit("(abc)x") == "(abc)")
print(parenBit("(x)") == "(x)")
print(parenBit("()") == "()")
print(parenBit("res (ipsa) loquitor") == "(ipsa)")
print(parenBit("hello(not really)there") == "(not really)")
print(parenBit("ab(ab)ab") == "(ab)")
print(parenBit("ab(ab)ab") == "(ab)")
