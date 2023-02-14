'''
❓ PROMPT
Given a string and a non-empty substring **sub**, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.

Example(s)
strCopies("catcowcat", "cat", 2) == True
strCopies("catcowcat", "cow", 2) == False
strCopies("catcowcat", "cow", 1) == True


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O()
Space: O()


📆 PLAN
High-level outline of approach #:


🛠️ IMPLEMENT
function strCopies(word, sub, n) {
def strCopies(word: str, sub: str, n: int) -> bool:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

# def strCopies(word: str, sub: str, n: int) -> bool:

#     count = 0

#     if len(word) < len(sub) or len(word) == 0:
#         return 0

#     if word[1:len(sub)] == sub:
#         count = strCopies(word[1:], sub, n) + 1

#     strCopies(word[1:], sub, n)
#     print(count)
#     return count >= n

def strCopies(word: str, sub: str, n: int) -> bool:

    if n == 0:
        return True

    if len(word) < len(sub):
        return False

    if word[0:len(sub)] == sub:
        return strCopies(word[1:], sub, n - 1)

    return strCopies(word[1:], sub, n)


print(strCopies("catcowcat", "cat", 2) == True)
# print(strCopies("catcowcat", "cow", 2) == False)
# print(strCopies("catcowcat", "cow", 1) == True)
# print(strCopies("iiijjj", "i", 3) == True)
# print(strCopies("iiijjj", "i", 4) == False)
# print(strCopies("iiijjj", "ii", 2) == True)
# print(strCopies("iiijjj", "ii", 3) == False)
# print(strCopies("iiijjj", "x", 3) == False)
# print(strCopies("iiijjj", "x", 0) == True)
# print(strCopies("iiiiij", "iii", 3) == True)
# print(strCopies("iiiiij", "iii", 4) == False)
# print(strCopies("ijiiiiij", "iiii", 2) == True)
# print(strCopies("ijiiiiij", "iiii", 3) == False)
# print(strCopies("dogcatdogcat", "dog", 2) == True)
