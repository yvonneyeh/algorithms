# Maximum Sum Subarray of Size K
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

"""
Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

  # create a sliding window of length k
  # add elements to list of sums
  # if the end of window reaches the end,
    # add the sum to list
    # subtract first element from win sum
    # move window start one forward
  # return maximum from list

def max_sum_of_subarray_of_size_k(k, arr):
    sums = []
    window_sum = 0.0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            sums.append(window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max(sums)

# don't need to keep track of all of the sums in array, just track max sum

def max_sum_of_subarray_of_size_k_refactored(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum

# Time Complexity = O(N)
# Space Complexity = O(1)
