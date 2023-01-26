# Write a function that takes a list of characters and reverses the letters in place.

# In general, an in-place ↴ algorithm will require swapping elements.

# Alorithm:
# We swap the first and last characters, then the second and second-to-last characters, and so on
# until we reach the middle.

  def reverse(arr):

    left  = 0
    right = len(arr) - 1

    while left < right:
        # Swap characters
        arr[left], arr[right] = arr[right], arr[left]
        # Move towards middle
        left  += 1
        right -= 1


# O(n) time
# O(1) space



'''
❓ PROMPT
Problem Statement: Write a function that takes an array and reverses its elements in place. Do not use built-in methods!

Daniel introduces two pointer problem: https://www.loom.com/share/4090423f2aad41efafe30dd09eb025d8

This task is a basic introduction to what is commonly called "two pointer" algorithms. They come up often when dealing with data ordered or organized in some way or when we're trying to do something with the ordering.

This problem is the latter. The order of the elements in the array at the start doesn't matter, but the task is to re-organize the elements so that at the end, the order is the reverse of what it was coming in.

Example(s)
reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N) to iterate through the length N array
Space: O(1) to reverse in-place. Creating a new array is O(N) so try in-place.


📆 PLAN
High-level outline of approach #:
Start with two indices, one initialized to 0 and one to one less than the length. Swap the elements at these two indices then increment the lower index and decrement the upper.


🛠️ IMPLEMENT
function reverse(array) {
def reverse(array: list[int]) -> list[int]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

# empty array
# 1 element array
# odd length array
# even length array

'''


def reverse(array: list[int]) -> list[int]:

    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return array

# def reverse(array: list[int]) -> list[int]:
#     i = 0
#     j = len(array) - 1
#     while i < j:
#         temp = array[j]
#         array[j] = array[i]
#         array[i] = temp
#         j -= 1
#         i += 1
#     return array

reverse([]) == []
reverse([5]) == [5]
reverse([5,10]) == [10,5]
reverse([5,10,15]) == [15,10,5]
reverse([5,10,15,20]) == [20,15,10,5]
reverse([1,2,3,4,5]) == [5,4,3,2,1]
