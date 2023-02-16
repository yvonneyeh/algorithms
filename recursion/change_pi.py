'''
❓ PROMPT
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".

Example(s)
changePi("xpix") == "x3.14x"
changePi("pipi") == "3.143.14"
changePi("pip") == "3.14p"


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the string be empty or null?
A: Empty but not null.
Q: Can there be capital letters, special characters, and numbers?
A: There can all kinds of different characters.
Q: What about different capitalizations of "pi" like "PI, Pi, or pI"?
A: Only replace it when it's "pi" in all lower-case.


Create examples & test cases:

empty string
1 char strings
strings without pi occurring
only p or only i in the string
only pi
pi with other characters
multiple pi occurrences


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(L) where L is the length of the string
Space: O(L^2) where L is the length of the string to create a new stack frame for L characters and to create a new L length string from slicing on each frame.


📆 PLAN
High-level outline of approach #:


🛠️ IMPLEMENT
function changePi(word) {
def changePi(word: str) -> str:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''


def changePi(word: str) -> str:

    if len(word) < 2:
        return word

    if word[0:2] == "pi":
        return "3.14" + changePi(word[2:])

    return str(word[0] + changePi(word[1:]))


print(changePi("xpix") == "x3.14x")
print(changePi("pipi") == "3.143.14")
print(changePi("pip") == "3.14p")
print(changePi("pi") == "3.14")
print(changePi("hip") == "hip")
print(changePi("p") == "p")
print(changePi("x") == "x")
print(changePi("") == "")
print(changePi("pixx") == "3.14xx")
print(changePi("xyzzy") == "xyzzy")
