'''
❓ PROMPT
Given an array, reverse every sub-array formed by consecutive k elements.

Example(s)
Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3
Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]

Input: arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 5
Output: [5, 4, 3, 2, 1, 8, 7, 6]

Input: arr = [1, 2, 3, 4, 5, 6], k = 1
Output: [1, 2, 3, 4, 5, 6]

Input: arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 10
Output: [8, 7, 6, 5, 4, 3, 2, 1]


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(N)
Space: O(N) - create a new array


📆 PLAN
High-level outline of approach #:

- keep count of reversals
-


🛠️ IMPLEMENT
function reverse(arr, k) {
def reverse(arr: list[int], k: int) -> None:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''


def reverse(arr: list[int], k: int) -> None:
    # result = []
    i = 0

    while i < len(arr):

        left = i
        right = i + k - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        i += k

    return arr
