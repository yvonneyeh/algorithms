import math

def smallest_subarray_sum(s, arr):
  # the size of the subarray is not fixed
  # trying to figure out length of shortest subarray that is larger than 's'
  # create a sliding window
  # iterate through indices, add element to window sum
  # if window sum is greater than s, set min_length to min between curr and min

  min_length = math.inf
  window_start = 0
  window_sum = 0
  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start +1)
      window_sum -= arr[window_start]
      window_start += 1

  if min_length == math.inf:
    return 0

  return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()
