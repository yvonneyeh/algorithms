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


def printArray(array: list[int]) -> None:
def printEveryOtherValue(array: list[int]) -> None:
def printEveryOtherValueSkipFirst(array: list[int]) -> None:
def printEveryKth(array: list[int], k: int) -> None:
def printReverse(array: list[int]) -> None:
def printReverseEveryOtherValue(array: list[int]) -> None:
def printReverseEveryOtherValueSkipLast(array: list[int]) -> None:
def printReverseEveryKth(array: list[int], k: int) -> None:
