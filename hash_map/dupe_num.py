# Given an array with items 1 through N, find the missing number. If no number is missing return -1

# [1,2,2] > 3
# [1,2,3,5,5] > 4
# [3,2,1] > -1

def solution(nums):
    nums.sort()

    prev_num = nums[0]
    result = -1

    for num in nums[1:]:
        print(num)
        print(result)
        if num == prev_num:
            result = prev_num + 1
            print(result)
        prev_num = num


    return result

def solution(nums):

    num_count = {}
    result = -1

    for i in range(1, len(nums)+1):
        num_count[i] = 0

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    for key, value in num_count.items():
        if value == 0:
            result = key

    return result
