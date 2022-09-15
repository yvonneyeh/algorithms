# 238. Product of Array Except Self
"""
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create results array with all 1s same length as nums
        # go from left to right, start from 1 to end of list, multiply num with product
        # update results array by multiplying same index w new product

        answer = [1] * len(nums)

        product = 1
        for i in range(1, len(nums)): # left to right, start from 1 to end of list
            product *= nums[i-1]
            answer[i] *= product

        product = 1
        for i in range(len(nums)-2, -1, -1): # right to left, start: 2nd last, stop: 1st, step: backwards
            product *= nums[i+1]
            answer[i] *= product

        return answer
