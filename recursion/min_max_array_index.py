'''
❓ PROMPT
Given an array, write 2 recursive functions to find the index of the minimum and maximum element in an array. If there's a tie-breaker, return the first occurrence.

Example(s)
findMinIndex([12, 1234, 45, 67, 1]) == 4
findMinIndex([10, 20, 30]) == 0
findMinIndex([8, 6, 7, 5, 3, 7]) == 4

findMaxIndex([12, 1234, 45, 67, 1]) == 1
findMaxIndex([10, 20, 30]) == 2
findMaxIndex([8, 6, 7, 5, 3, 7]) == 0


🔎 EXPLORE
State your assumptions & discoveries:
Q: Can the array be empty?
A: No there will always be at least 1 element to avoid having to throw an exception.

Create examples & test cases:
# 1 element array
# strictly increasing array
# strictly decreasing array
# array with some duplicates
# array with all duplicates
# array with negative values

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(n) where n is the length of the array. O(n2) If using splicing.
Space: O(n) to store a call stack frame for each array index. O(n2) If using splicing.


📆 PLAN
High-level outline of approach #:


🛠️ IMPLEMENT
function findMinIndex(array) {
function findMaxIndex(array) {
def findMinIndex(arr: list[int]) -> int:
def findMaxIndex(arr: list[int]) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def findMinIndex(arr: list[int]) -> int:
    if not arr:
        return -1



def findMaxIndex(arr: list[int]) -> int:

    if not arr:
        return -1
