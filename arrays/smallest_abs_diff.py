# Write a function that returns the smallest absolute difference between any two element. For example, the input [1, 2, 3, 4], the smallest difference is 1 (any adjacent pair difference).

# [execution time limit] 4 seconds (py3)
# [input] array.integer array
# [output] integer


def solution(array):

    result = float('inf')

    array.sort()

    for i, num in enumerate(array):
        if i < len(array) - 1:
            current = abs(num - array[i+1])
        if result > current:
            result = current

    return result
