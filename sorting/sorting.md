# Sorting algorithms

### insertion sort
  - pick up the next item and move it into its sorted position
  - O(n^2)

### selection sort
  - find the smallest one and move it to the front
  - lather, rinse, repeat until sorted
  - O(n^2)

### merge sort
  - We can merge two sorted lists in O(n)
  - if we treat every element as a sorted list of length one
    - then we can merge every pair of lists to get sorted lists of length 2     O(n)
    - then we can merge every pair of lists to get sorted lists of length 4    O(n)
    - then we can merge every pair of lists to get sorted lists of length 8   O(n)
    - then we can merge every pair of lists to get sorted lists of length 16      O(n)
    - then we can merge every pair of lists to get sorted lists of length 32      O(n)
    - then we can merge every pair of lists to get sorted lists of length 64      O(n)
    - then we can merge every pair of lists to get sorted lists of length 128     O(n)
    - ...
  - O(n  * log(n))

    v                           v
[1, 100, 1000, 10000]    [3, 4, 7, 20, 30, 50, 2000, 6000]

### quick sort
  - Choose a pivot
  - Move all numbers smaller than the pivot to the left and all numbers bigger than the pivot to the right O(n)
  - Recurse on each half
  - O(n * log(n))

### bucket sort
  - Have an O(1) choosing a bucket
  - For each card, put it in the right bucket
