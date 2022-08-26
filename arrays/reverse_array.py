# Write a function that takes a list of characters and reverses the letters in place.

# In general, an in-place ↴ algorithm will require swapping elements.

# Alorithm:
# We swap the first and last characters, then the second and second-to-last characters, and so on
# until we reach the middle.

  def reverse(arr):

    left_index  = 0
    right_index = len(arr) - 1

    while left_index < right_index:
        # Swap characters
        arr[left_index], arr[right_index] = \
            arr[right_index], arr[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1


# O(n) time
# O(1) space
