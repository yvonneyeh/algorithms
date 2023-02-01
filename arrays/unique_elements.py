"""
Given an unsorted array, return the number of unique elements that appear only once in the array.

Examples:
• Given an array: [3, 1, 1, 2, 3, 1, 1, 1, 4] // returns 2 (unique elements: 2 and 4)
• Given an array: [1] // returns 1 (unique element: 1)
"""

def numUniques(array: [int]) -> int:

    num_count = {}
    result = []

    for item in array:
        num_count[item] = num_count.get(item, 0) + 1

    for key, value in num_count.items():
        if value == 1:
            result.append(key)

    return len(result)

# Test Cases
print(numUniques([])) # 0
print(numUniques([3, 1, 1, 2, 3, 1, 1, 1, 4])) # 2
print(numUniques([1])) # 1
