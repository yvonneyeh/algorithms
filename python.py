# Python for interviews

# Variables are dynamicly typed
n = 0
print('n =', n)
>>> n = 0

n = "abc"
print('n =', n)
>>> n = abc

# Multiple assignments
n, m = 0, "abc"
n, m, z = 0.125, "abc", False

# Increment
n = n + 1 # good
n += 1    # good
n++       # bad

# None is null (absence of value)
n = 4
n = None
print("n =", n)
>>> n = None


# If statements don't need parentheses
# or curly braces.
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multi-line conditions.
# and = &&
# or  = ||
n, m = 1, 2
if ((n > 2 and
    n != m) or n == m):
    n += 1


n = 0
while n < 5:
    print(n)
    n += 1
>>> 0 1 2 3 4

# Looping from i = 0 to i = 4
for i in range(5):
    print(i)
>>> 0 1 2 3 4

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)
>>> 2 3 4 5

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)
>>> 5 4 3 2

# Division is decimal by default
print(5 / 2)
>>> 2.5

# Double slash rounds down
print(5 // 2)
>>> 2

# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
print(-3 // 2)
>>> -2

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
print(int(-3 / 2))
>>> -1

# Modding is similar to most languages
print(10 % 3)
>>> 1

# Except for negative values
print(-10 % 3)
>>> 2

# To be consistent with other languages modulo
import math
from multiprocessing import heap
print(math.fmod(-10, 3))
>>> -1

# More math helpers
print(math.floor(3 / 2))
>>> 1
print(math.ceil(3 / 2))
>>> 2
print(math.sqrt(2))
>>> 1.4142135623730951
print(math.pow(2, 3))
>>> 8

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))
>>> 1.6069380442589903e+60

# But still less than infinity
print(math.pow(2, 200) < float("inf"))
>>> True


# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)
>>> [1, 2, 3]

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)
>>> [1, 2, 3, 4, 5]

arr.pop()
print(arr)
>>> [1, 2, 3, 4]

arr.insert(1, 7)
print(arr)
>>> [1, 7, 2, 3, 4]

arr[0] = 0
arr[3] = 0
print(arr)
>>> [0, 7, 2, 0, 4]

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
>>> [1, 1, 1, 1, 1]
print(len(arr))
>>> 5

# Careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1])
>>> 3

# Indexing -2 is the second to last value, etc.
print(arr[-2])
>>> 2

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])
>>> [2, 3]

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])
>>> [1, 2, 3, 4]

# But no out of bounds error
print(arr[0:10])
>>> [1, 2, 3, 4]

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)
>>> 1, 2, 3

# Be careful though, this throws an error
a, b = [1, 2, 3]

# Looping through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])
>>> 1 2 3

# Without index
for n in nums:
    print(n)
>>> 1 2 3

# With index and value
for i, n in enumerate(nums):
    print(i, n)
>>> 0 1
>>> 1 2
>>> 2 3

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
>>> 1 2
>>> 3 4
>>> 5 6

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)
>>> [3, 2, 1]


# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)
>>> [3, 4, 5, 7, 8]

arr.sort(reverse=True)
print(arr)
>>> [8, 7, 5, 4, 3]

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)
>>> ["alice", "bob", "doe", "jane"]

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)
>>> ["bob", "doe", "jane", "alice"]

# List comprehension
arr = [i for i in range(5)]
print(arr)
>>> [0, 1, 2, 3, 4]

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)
print(arr[0][0], arr[3][3])
>>> [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# This won't work as you expect it to
arr = [[0] * 4] * 4

Strings
# Strings are similar to arrays
s = "abc"
print(s[0:2])
>>> "ab"

# But they are immutable, this won't work
s[0] = "A"

# This creates a new string
s += "def"
print(s)
>>> "abcdef"

# Valid numeric strings can be converted
print(int("123") + int("123"))
>>> 246

# And numbers can be converted to strings
print(str(123) + str(123))
>>> "123123"

# In rare cases you may need the ASCII value of a char
print(ord("a"))
print(ord("b"))
>>> 97
>>> 98

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))
>>> "abcdef"
Queues
# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
>>> deque([1, 2])

queue.popleft()
print(queue)
>>> deque([2])

queue.appendleft(1)
print(queue)
>>> deque([1, 2])

queue.pop()
print(queue)
>>> deque([1])
HashSets
# HashSet
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
>>> {1, 2}
print(len(mySet))
>>> 2

print(1 in mySet)
>>> True
print(2 in mySet)
>>> True
print(3 in mySet)
>>> False

mySet.remove(2)
print(2 in mySet)
>>> False

# list to set
print(set([1, 2, 3]))
>>> {1, 2, 3}

# Set comprehension
mySet = { i for i in range(5) }
print(mySet)
>>> {0, 1, 2, 3, 4}
HashMaps
# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
>>> {"alice": 88, "bob": 77}

print(len(myMap))
>>> 2

myMap["alice"] = 80
print(myMap["alice"])
>>> 80

print("alice" in myMap)
>>> True

myMap.pop("alice")
print("alice" in myMap)
>>> False

myMap = { "alice": 90, "bob": 70 }
print(myMap)
>>> { "alice": 90, "bob": 70 }

# Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)
>>> { 0: 0, 1: 2, 2: 4 }

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])
>>> "alice" 90
>>> "bob" 70

for val in myMap.values():
    print(val)
>>> 90
>>> 70

for key, val in myMap.items():
    print(key, val)
>>> "alice" 90
>>> "bob" 70
Tuples
# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
>>> (1, 2, 3)

print(tup[0])
>>> 1

print(tup[-1])
>>> 3

# Can't modify, this won't work
tup[0] = 0

# Can be used as key for hash map/set
myMap = { (1,2): 3 }
print(myMap[(1,2)])
>>> 3

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)
>>> True

# Lists can't be keys
myMap[[3, 4]] = 5
Heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])
>>> 2

while len(minHeap):
    print(heapq.heappop(minHeap))
>>> 2 3 4

# No max heaps by default, work around is
# to use min heap and multiply by -1 when push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])
>>> 4

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
>>> 4 3 2

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))
>>> 1 2 4 5 8
Functions
def myFunc(n, m):
    return n * m

print(myFunc(3, 4))
>>> 12

# Nested functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))
>>> "abc"

# Can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)
>>> [2, 4] 6
Classes
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

myObj = MyClass([1, 2, 3])
print(myObj.getLength())
>>> 3
print(myObj.getDoubleLength())
>>> 6
