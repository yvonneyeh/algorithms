# Two Sum
def two_sum(nums: List[int], target: int) -> List[int]:
   seen = {}
   for i, value in enumerate(nums):
       remaining = target - nums[i]

       if remaining in seen:
           return [i, seen[remaining]]
       else:
           seen[value] = i

# Two Sum II - Input Array Is Sorted

def two_sum_sorted(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 # using 2 pointers

        while l < r:
            current = numbers[l] + numbers[r]
            if current > target:
                r -= 1
            elif current < target:
                l += 1
            else:
                return [l+1, r+1]


# Three Sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort array to be able to check for dupes
        # iterate through list and create a target number
        # two sum with l/r pointer to find matches

        result = []
        nums.sort()

        for i, target in enumerate(nums):
            # if not first num, check if previous number is same, if so, continue
            # don't reuse values
            if i > 0 and nums[i] == nums[i-1]:
                    continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = target + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return result


def three_sum(nums: List[int]) -> List[List[int]]:
    res = set()

	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0:
			n.append(num)
		else:
			z.append(num)

	#2. Create a separate set for negatives and positives for O(1) look-up times
	N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
	if len(z) >= 3:
		res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res



/*
'''
❓ PROMPT
Now we're going to apply two different patterns to the same problem and see how the code looks and how it affects the runtime.

The task is to determine if an array contains a pair that adds up to a value, k. The array is sorted ahead of time.

Just like many problems in computer science and software engineering, there are multiple ways to solve the problem, but they often have different time or space complexity, or there are other tradeoffs.

Learning to recognize these decision points is an important step in becoming a strong software engineer.

Patterns and Tools: https://www.loom.com/share/0186a52926dd431bbb25204074812a3a

Example(s)
[1, 5, 8, 10, 13, 18], k = 15 => true


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
function sumToK(array, k) {
def sumToK(array, k):


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

# empty array
# 1-element array
# 2-element array
# a pair
# all unique elements
# a pair can sum up to K
# multiple pairs can sum up to K
# no pairs can sum up to K

'''
*/



def sumToK(array, k):

    seen = {}

    for i, num in enumerate(array):
        target = k - num
        if num not in seen:
            seen[target] = i
        else:
            return True

    return False
