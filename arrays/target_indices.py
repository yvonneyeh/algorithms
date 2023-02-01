'''
❓ PROMPT
Given an array and a target value X, return an array of all indices containing value X.

Example(s)
indicesOfTarget([30,30,30], 30) == [0,1,2]
indicesOfTarget([3, 2, 5, 5, 1], 5) == [2,3]


🔎 EXPLORE
State your assumptions & discoveries:

Q. If the target does not appear in the original array, should I return an empty array?
A. Yes.
Q: Does the output order matter?
A: Yes and no. As long as every index is there only once, then that's fine. However, this problem should be done in the simplest way possible. What order will that put the output in?


Create examples & test cases:

# empty list
# array with 1 element and target is present
# array with 1 element and target isn't present
# array with multiple elements and target is present
# array with multiple elements and target isn't present
# array with multiple elements and target is present multiples times
# array with multiple elements and target is the only value


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N array
Space: O(N) to store up to N indices in the result


📆 PLAN
High-level outline of approach #:

- Enumerate through entire list and append to result array if number matches target


🛠️ IMPLEMENT
function indicesOfTarget(arr, target) {
def indicesOfTarget(arr: list[int], target: int) -> list[int]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def indicesOfTarget(arr: list[int], target: int) -> list[int]:
    result = []

    for i, num in enumerate(arr):
        if num == target:
            result.append(i)

    return result

print(indicesOfTarget([], 1) == [])
print(indicesOfTarget([5], 5) == [0])
print(indicesOfTarget([5], 1) == [])
print(indicesOfTarget([1], 1) == [0])
print(indicesOfTarget([10,20,30], 1) == [])
print(indicesOfTarget([10,20,30], 20) == [1])
print(indicesOfTarget([30,30,30], 30) == [0,1,2])
print(indicesOfTarget([3, 2, 5, 5, 1], 5) == [2,3])
