# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

list_of_nums =  [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5

def find_average_of_subarrays(arr, k):
    result = []
    print(len(arr)-k+1)
    print(k)
    for i in range(len(arr)-k+1):
        print(i)
        # find sum of next 'k' elements
        sum_of_nums = 0.0
        for j in range(i, i+k):
            sum_of_nums += arr[j]
        result.append(sum_of_nums/k) # calculate avg and append to list
    return result

print(find_average_of_subarrays(list_of_nums, K))

# O(N∗K) - where ‘N’ is the number of elements in the input array.
# inefficient bc there are overlapping elements between the subarray

# visualize the subarray w/ a sliding window
# keep track of sum: subtract element going out, add element coming into window
# save us from going through the whole subarray to find the sum and
# algorithm complexity will reduce to O(N)

def find_average_of_subarrays_with_sliding_window(arr, k):
    result = []
    window_sum, window_start = 0.0, 0 
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1: # arrive at end of current window
            result.append(window_sum/k) # calculate average, add to list
            window_sum -= arr[window_start] # subtract first element in window
            window_start += 1 # slide window forward

    return result

print(find_average_of_subarrays_with_sliding_window(list_of_nums, K))
