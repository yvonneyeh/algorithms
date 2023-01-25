'''
❓ PROMPT
Let's practice some basic skills in manipulating arrays and dealing with indices. We're going to iterate through the array and print out the values. Then we'll work through some variations that will help you get comfortable working with indices.

Use an input array of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] to verify the output easily. For the variations with a k parameter, use values of 1 through 10.

1. Print out every value
2. Print out every other value
3. Print out every other value, skipping the first one
4. Add a second parameter, k, and now print out every kth value, starting with the first.

Finally, print all of these again in *reverse*:
1. Every element starting with the last
2. Every other element starting with the last index
3. Every other element skipping the last index
4. Every kth element starting with the last

#### 🥅 Goal
Write this code as cleanly as possible with no special cases or if-statements, just choosing the starting index, increment expression, and ending condition for each loop.

**Important note for Python programmers**: Do not use a for loop with the range() function for this task. Python's for loop is actually what other languages call a for-each loop. The way that the range() function combines with this loop is very convenient but understanding and practicing these basic counting loop patterns is very important.

Instead, do this manually by manipulating an index variable directly and use a while loop.  Building this level of understanding now will make a lot of things easier later, and will even help you better understand and write more idiomatic Python using range().

Example(s)
testData = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k=3

printEveryKth(testData, k)

0,3,6,9


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


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''


# def printArray(array: list[int]) -> None:
#     for item in array:
#         print(item)
#
# def printEveryOtherValue(array: list[int]) -> None:
#     for i, item in enumerate(array):
#         if i % 2 == 0:
#             print(item)
#
# def printEveryOtherValueSkipFirst(array: list[int]) -> None:
#     for i, item in enumerate(array):
#         if i % 2 == 1:
#             print(item)
#
# def printEveryKth(array: list[int], k: int) -> None:
#     for i, item in enumerate(array):
#         if i % k == 0:
#             print(item)
#
#
# def printReverse(array: list[int]) -> None:
#     for item in array[::-1]:
#         print(item)
#
# def printReverseEveryOtherValue(array: list[int]) -> None:
#     for i, item in enumerate(array[::-1]):
#         if i % 2 == 0:
#             print(item)
#
# def printReverseEveryOtherValueSkipLast(array: list[int]) -> None:
#     for i, item in enumerate(array[::-1]):
#         if i % 2 == 1:
#             print(item)
#
# def printReverseEveryKth(array: list[int], k: int) -> None:
#     for i, item in enumerate(array[::-1]):
#         if i % k == 0:
#             print(item)


def printArray(array: list[int]) -> None:
    i = 0
    while i < len(array):
        print(array[i])
        i += 1

def printEveryOtherValue(array: list[int]) -> None:
    i = 0
    while i < len(array):
        print(array[i])
        i += 2

def printEveryOtherValueSkipFirst(array: list[int]) -> None:
    i = 1
    while i < len(array):
        print(array[i])
        i += 2

def printEveryKth(array: list[int], k: int) -> None:
    i = 0
    while i < len(array):
        print(array[i])
        i += k


def printReverse(array: list[int]) -> None:
    i = len(array) - 1
    while i >= 0:
        print(array[i])
        i -= 1

def printReverseEveryOtherValue(array: list[int]) -> None:
    i = len(array) - 1
    while i >= 0:
        print(array[i])
        i -= 2

def printReverseEveryOtherValueSkipLast(array: list[int]) -> None:
    i = len(array) - 2
    while i >= 0:
        print(array[i])
        i -= 2

def printReverseEveryKth(array: list[int], k: int) -> None:
    i = len(array) - 1
    while i >= 0:
        print(array[i])
        i -= k


# Test Cases

testData = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

printArray(testData); print() # 0,1,2,3,4,5,6,7,8,9,10,
printEveryOtherValue(testData); print() # 0,2,4,6,8,10,
printEveryOtherValueSkipFirst(testData); print() # 1,3,5,7,9,
printEveryKth(testData, k); print() # 0,3,6,9,
printReverse(testData); print() # 10,9,8,7,6,5,4,3,2,1,0,
printReverseEveryOtherValue(testData); print() # 10,8,6,4,2,0,
printReverseEveryOtherValueSkipLast(testData); print() # 9,7,5,3,1,
printReverseEveryKth(testData, k); print() # 10,7,4,1,



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
Time: O()
Space: O()


📆 PLAN
High-level outline of approach #:


🛠️ IMPLEMENT
function printAllPairs(array) {
def printAllPairs(array: list[int]) -> None:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

# What should be printed out when the array is empty or a single element? > Nothing.
# Should the algorithm output duplicate results if the array has duplicate values? > Yes, there's no uniqueness constraint.

# You'll need two for-loops. The outer one starts at 0 and the inner one starts at one greater than 0 in most cases. If the inner loop starts at 0 you'll end up with duplicate pairs, some in the opposite order. If the inner loop starts at index i, then you'll include pairs of values at the same index. If the inner loop starts at index i+1 then the output will be pairs of values at distinct indices.


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
