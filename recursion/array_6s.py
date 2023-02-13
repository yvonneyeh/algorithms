'''
❓ PROMPT
Given an array of ints, compute recursively the number of times that the value 6 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

Example(s)
array6([1, 2, 6], 0) == 1
array6([6, 6], 0) == 2
array6([1, 2, 3, 4], 0) == 0


🔎 EXPLORE
State your assumptions & discoveries:

- ([], 0) returns 0
Q: Can I assume the input array will be valid?
A: It can be empty but not null.
Q: Can I assume the input array will be only integers?
A: Yes
Q: Can I assume the input array will be only positive?
A: The values can be any integer number: positive, negative, or zero.

Create examples & test cases:

empty array
array with 1 element
array with 1 element that's a 6
array with multiple numbers and 1 element that's a 6
array with two 6's elements
array with two 6's elements next to each other
array with all 6's elements


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(n) where n is the length of the array
Space: O(n) to store a call stack frame for each array index


📆 PLAN
High-level outline of approach #:

The base case is when the index matches the length of the array.

If item at index matches, add 1 to the recursive stack


🛠️ IMPLEMENT
function array6(nums, index) {
def array6(nums: list[int], index: int) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def array6(nums: list[int], index: int) -> int:

    if index >= len(nums):
        return 0
    if nums[index] == 6:
        return array6(nums, index + 1) + 1

    return array6(nums, index + 1)

print(array6([1, 2, 6], 0) == 1)
print(array6([6, 6], 0) == 2)
print(array6([1, 2, 3, 4], 0) == 0)
print(array6([1, 6, 3, 6, 6], 0) == 3)
print(array6([6], 0) == 1)
print(array6([1], 0) == 0)
print(array6([], 0) == 0)
print(array6([6, 2, 3, 4, 6, 5], 0) == 2)
print(array6([6, 5, 6], 0) == 2)
