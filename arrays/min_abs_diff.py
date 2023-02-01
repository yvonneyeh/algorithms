'''
❓ PROMPT
Given an array of unique integers, find all pairs of elements with the minimum absolute difference. If there are multiple pairs, return them in ascending order.

Example(s)
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Explanation: There is only 1 pair of elements with a minimum absolute difference of 2.

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
Explanation: There are 3 pairs of elements with a minimum absolute difference of 4, which are listed in ascending order according to the smaller value in the pair.

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: There are 3 pairs of elements with a minimum absolute difference of 1, which are listed in ascending order according to the smaller value in the pair.


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

- Sort the array, this way differences between numbers is the smallest it can be
- keep track of smallest difference var
- result = []
- look at every pair in the array


🛠️ IMPLEMENT
function minAbsDiffPairs(arr) {
def minAbsDiffPairs(arr: list[int]) -> list[list[int]]:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''


# def minAbsDiffPairs(arr: list[int]) -> list[list[int]]:
#     sorted(array)
#     result = []
#     min_diff = 0
#
#     for i in range(len(last)-2):
#         current = arr[i] - arr[i+1]
#         if current < min_diff:
#             min_diff = abs(current)
#         elif current == min_diff:
#             result.append([arr[i], arr[i+1]])
#
#     return result


def minAbsDiffPairs(arr: list[int]) -> list[list[int]]:
    arr.sort()
    result = []
    min_diff = float('inf') # make default largest num possible

    for i in range(len(arr)-1): # stop is non-inclusive
        current = arr[i+1] - arr[i]
        pair = [arr[i], arr[i+1]]

        if current < min_diff:
            result = [pair]
            min_diff = current
        elif current == min_diff:
            result.append(pair)

    return result


arr = [1,3,6,10,15]
print(minAbsDiffPairs(arr) == [[1,3]])

arr = [3,8,-10,23,19,-4,-14,27]
print(minAbsDiffPairs(arr) == [[-14,-10],[19,23],[23,27]])

arr = [4,2,1,3]
print(minAbsDiffPairs(arr) == [[1,2],[2,3],[3,4]])

arr = [1,3,6,7,10,15]
print(minAbsDiffPairs(arr) == [[6,7]])

arr = [5,15]
print(minAbsDiffPairs(arr) == [[5,15]])

arr = [15,5]
print(minAbsDiffPairs(arr) == [[5,15]])
