# 53. Maximum Subarray
"""
Medium

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:
    Input: nums = [1]
    Output: 1
Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray1(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            largest_sum = max(largest_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return largest_sum
    # Time: O(n)
    # Memory: O(1)

    def maxSubArray2(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            largest_sum = max(current_sum, largest_sum)

        return largest_sum

    def maxSubArray3(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

# Runtime: 1266 ms, faster than 18.30% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.6 MB, less than 9.67% of Python3 online submissions for Maximum Subarray.
