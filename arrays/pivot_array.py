"""
Rotate Array @ Pivot Number

In this variation, you will be receiving an array of Int, where the number 0 represents a word break. Reverse all the elements between the 0s.

Ex. [1, 2, 3, 0, 4, 5, 6] returns [3, 2, 1, 0, 6, 5, 4] (1, 2, 3 and 4, 5, 6 were the two chunks that were reversed)

Ex. [1, 2, 3, 4, 5, 6] returns [6, 5, 4, 3, 2, 1] (since there are no zeroes, the entire array is considered one chunk)

Ex. [1, 0, 2, 0, 3] returns [1, 0, 2, 0, 3] (Since all the chunks size 1, no change happens)


Approach:
- find 0 in array
- get index of 0
- helper function to rotate array
"""


def rotate_array(array):

  pivot = []

  for i, item in enumerate(array):
    if item == 0:
      pivot.append(i)

  def rotate(array, l, r):
    while l < r:
      array[l], array[r] = array[r], array[l]
      l += 1
      r -= 1

  if not pivot:
    rotate(array, 0, len(array) - 1)
    return array

  # [1,3]
  pivot.append(pivot[-1] + 1)

  for i, p in enumerate(pivot):
    if i == 0: # beginning
      l = 0
      r = p - 1 # pivot[i]

    elif i == len(pivot) - 1: # end
      l = pivot[i]
      r = len(array) - 1

    else: # middle pivots
      l = pivot[i-1] + 1
      r = pivot[i] - 1

    rotate(array, l, r)

  return array


print(rotate_array([1, 2, 3, 0, 4, 5, 6]))  # [3, 2, 1, 0, 6, 5, 4]
print(rotate_array([1, 2, 3, 4, 5, 6]))  # [6, 5, 4, 3, 2, 1]
print(rotate_array([1, 2, 3, 0, 1, 2, 3, 0, 1, 2,
                    3]))  # [3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1]
print(rotate_array([1, 0, 2, 0, 3]))  # [1, 0, 2, 0, 3]
print(rotate_array([1, 0, 2, 3, 4, 0, 5, 6, 0]))
