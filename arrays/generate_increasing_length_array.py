'''
❓ PROMPT
Given a target integer *X*, iterate from 1 to *X* and return a matrix sequence where each array starts with 1 and goes up to the current iteration. Each iteration should increment the array size and values until it reaches *X*.

[
[1],
[1, 2],
[1, 2, 3],
[1, 2, 3, 4],
[1, 2, 3, 4, 5],
...
...
...
[1, 2, 3, ..., X]
]

Example(s)
generateSequence(2) == [[1], [1,2]]
generateSequence(3) == [[1], [1,2], [1,2,3]]


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the target value be negative?
A: No.
Q: If the target value is 0, should I return an empty matrix?
A: Yes.


Create examples & test cases:

target == 0
target == 1
target is odd
target is even


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(X2) to iterate X times from 1 to X
Space: O(X2) to store up to X elements X times in the matrix


📆 PLAN
High-level outline of approach #:

Create an empty results matrix. Create a loop iterating from 1 to X. Inside that loop, create a nested loop that iterates from 1 to the current index, generating an array from 1 to the index. In some languages, you may be able to create a one-liner without a loop. Append this array to the results matrix. Return the results matrix.


🛠️ IMPLEMENT
function generateSequence(target) {
def generateSequence(target: int) -> list[list[int]]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def generateSequence(target: int) -> list[list[int]]:
    result = []

    for sequence in range(1, target + 1):
        current = []
        for i in range(1, sequence + 1):
            current.append(i)
        result.append(current)
    return result

print(generateSequence(0) == [[]] or generateSequence(0) == [])
print(generateSequence(1) == [[1]])
print(generateSequence(2) == [[1], [1,2]])
print(generateSequence(3) == [[1], [1,2], [1,2,3]])
print(generateSequence(4) == [[1], [1,2], [1,2,3], [1,2,3,4]])
