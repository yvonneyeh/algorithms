'''
❓ PROMPT
Finding all pairs is one of the basic patterns that frequently comes up, especially in _brute force_ algorithms. Understanding and proficiently applying this pattern will often jump-start progress on other problems, even if in the end there may be a way to do something more efficiently.

To illustrate this pattern, write a function that takes an array and prints out all of the pairs of elements from the array.

Example(s)
printAllPairs([1,2,3])
(1, 2)
(1, 3)
(2, 3)

printAllPairs([1,2,3,4])
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N^2) to go through the length N array up to N times for each index
Space: O(1) to print the results and not store anything

# What should be printed out when the array is empty or a single element? > Nothing.
# Should the algorithm output duplicate results if the array has duplicate values? > Yes, there's no uniqueness constraint.



📆 PLAN
High-level outline of approach #:
# You'll need two for-loops. The outer one starts at 0 and the inner one starts at one greater than 0 in most cases. If the inner loop starts at 0 you'll end up with duplicate pairs, some in the opposite order. If the inner loop starts at index i, then you'll include pairs of values at the same index. If the inner loop starts at index i+1 then the output will be pairs of values at distinct indices.



🛠️ IMPLEMENT
function printAllPairs(array) {
def printAllPairs(array: list[int]) -> None:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''



# Test considerations
    # empty array
    # 1-element array
    # 2-element array
    # odd-length array
    # even-length array
    # array with duplicates

def printAllPairs(array: list[int]) -> None:
  length = len(array)
  for i in range(length):
    for j in range(i + 1, length):
      print((array[i], array[j]))


printAllPairs([])
# // no output

printAllPairs([5])
# // no output

printAllPairs([1, 2, 3, 4, 5])
# (1, 2)
# (1, 3)
# (1, 4)
# (1, 5)
# (2, 3)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)
# (4, 5)

printAllPairs([5, 8, 5, 8])
# (5, 8)
# (5, 5)
# (5, 8)
# (8, 5)
# (8, 8)
# (5, 8)


# All possible pairs in List
# Using list comprehension + enumerate()

# initializing list
test_list = [1, 7, 4, 3]

# printing original list
print("The original list : " + str(test_list))

# All possible pairs in List
# Using list comprehension + enumerate()
res = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]

# printing result
print("All possible pairs : " + str(res))



# All possible pairs in List
# Using combinations()
from itertools import combinations

# initializing list
test_list = [1, 7, 4, 3]

# printing original list
print("The original list : " + str(test_list))

# All possible pairs in List
# Using combinations()
res = list(combinations(test_list, 2))

# printing result
print("All possible pairs : " + str(res))
