# Trapping Rain Water
"""
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

class Solution:
    # constant memory O(1)
    def trap(self, height: List[int]) -> int:

        # edge case for empty array
        if not height: return 0

        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        total_water = 0

        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                current = max(max_left - height[l], 0) # if negative, set to 0
                total_water += current
            else:
                r -= 1
                max_right = max(max_right, height[r])
                current = max(max_right - height[r], 0) # if negative, set to 0
                total_water += current

        return total_water


        # Runtime: 257 ms
        # Memory Usage: 15.9 MB
