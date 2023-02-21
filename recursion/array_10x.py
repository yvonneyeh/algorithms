'''
❓ PROMPT
Given an array of ints, compute recursively if there's a value immediately followed by that value times 10 somewhere in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

Example(s)
array10x([1, 2, 20], 0) == True
array10x([3, 30], 0) == True
array10x([3], 0) == False


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can I assume the input array will be valid?
A: It can be empty but not null.
Q: Can I assume the input array will be only integers?
A: Yes
Q: Can I assume the input array will be only positive?
A: The values can be any integer number: positive, negative, or zero.


Create examples & test cases:

empty array
array with 1 element
array with 2 single digit elements
array with 2 elements first is 10x the second
array with 2 elements second is 10x the first
array with multiple elements and desired pair somewhere in the middle
array with multiple elements but the 10x value is far away

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(n) where n is the length of the array
Space: O(n) to store a call stack frame for each array index


📆 PLAN
High-level outline of approach #:

Time: O(n) where n is the length of the array
Space: O(n) to store a call stack frame for each array index


🛠️ IMPLEMENT
function array10x(nums, index) {
def array10x(nums: list[int], index: int) -> bool:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def array10x(nums: list[int], index: int) -> bool:
  if index >= len(nums) - 1:
    return False

  return nums[index + 1] == 10 * nums[index] or array10x(nums, index + 1)

print(array10x([1, 2, 20], 0) == True)
print(array10x([3, 30], 0) == True)
print(array10x([3], 0) == False)
print(array10x([], 0) == False)
print(array10x([3, 3, 30, 4], 0) == True)
print(array10x([2, 19, 4], 0) == False)
print(array10x([20, 2, 21], 0) == False)
print(array10x([20, 2, 21, 210], 0) == True)
print(array10x([2, 200, 2000], 0) == True)
print(array10x([0, 0], 0) == True)
print(array10x([1, 2, 3, 4, 5, 6], 0) == False)
print(array10x([1, 2, 3, 4, 5, 50, 6], 0) == True)
print(array10x([1, 2, 3, 4, 5, 51, 6], 0) == False)
print(array10x([1, 2, 3, 4, 4, 50, 500, 6], 0) == True)
