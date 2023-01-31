'''
❓ PROMPT
Given a target integer *X*, iterate from *X* to 1 and return a list of sequences where each starts with the current iteration and goes down to 1. Each iteration should decrement the array size and values until it reaches 1.

[
  [X, ..., 5, 4, 3, 2, 1],
  ...
  ...
  ...
  [5, 4, 3, 2, 1],
  [4, 3, 2, 1],
  [3, 2, 1],
  [2, 1],
  [1]
]

Example(s)
generateSequence(2) == [[2,1], [1]]
generateSequence(3) == [[3,2,1], [2,1], [1]]


🔎 EXPLORE
State your assumptions & discoveries:
- target can't be negative
- value = 0 -> should return empty matrix


Create examples & test cases:

Test considerations
target == 0
target == 1
target is odd
target is even


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(X^2) to iterate X times from 1 to X
Space: O(X^2) to store up to X elements X times in the matrix


📆 PLAN
High-level outline of approach #:

- nested array as result
- for loop from X to 1


🛠️ IMPLEMENT
function generateSequence(target) {
def generateSequence(target: int) -> list[list[int]]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def generateSequence(target: int) -> list[list[int]]:
    result = []
    x = target

    while target > 0:
        current = []
        for x in range(target, 0, -1):
            current.append(x)
        result.append(current)
        target -= 1

    return result

print(generateSequence(10))
print(generateSequence(0) == [[]] or generateSequence(0) == [])
print(generateSequence(1) == [[1]])
print(generateSequence(2) == [[2,1], [1]])
print(generateSequence(3) == [[3,2,1], [2,1], [1]])
print(generateSequence(4) == [[4,3,2,1], [3,2,1], [2,1], [1]])
