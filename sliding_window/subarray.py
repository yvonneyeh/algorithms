# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

list_of_nums =  [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5

def find_average_of_subarrays(arr, k):
    result = []
    for i in range(len(arr)-k+1):
        # find sum of next 'k' elements
        sum_of_nums = 0.0
        for j in range(i, i+k):
            sum_of_nums += arr[j]
        result.append(sum_of_nums/k) # calculate avg and append to list
    return result

print(find_average_of_subarrays(list_of_nums, K))
