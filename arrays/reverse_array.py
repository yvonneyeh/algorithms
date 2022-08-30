# Write a function that takes a list of characters and reverses the letters in place.

# In general, an in-place ↴ algorithm will require swapping elements.

# Alorithm:
# We swap the first and last characters, then the second and second-to-last characters, and so on
# until we reach the middle.

  def reverse(arr):

    left  = 0
    right = len(arr) - 1

    while left < right:
        # Swap characters
        arr[left], arr[right] = arr[right], arr[left]
        # Move towards middle
        left  += 1
        right -= 1


# O(n) time
# O(1) space
