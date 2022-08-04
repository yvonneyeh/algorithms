def longest_substring_with_k_distinct(str, k):
  # if length of k is greater than the length of the string, return the length of the string

  # idea 1 = create set to keep track of distinct characters
  # idea 2 = dictionary keep track of number count

  # create counter for substring

  # loop through string, add letter to dict if not inside, make sure set doesn't exceed K
  # if letter is in the set, add one to counter keeping track of substring length
  # using a sliding window, keep track of window start and end
  # if letter is in set, move window forward and keep adding letters until letters are not in set
  #

# First, we will insert characters from the beginning of the string until we have K distinct characters in the HashMap.
# These characters will constitute our sliding window. We are asked to find the longest such window having no more than K distinct characters. We will remember the length of this window as the longest window so far.
# After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
# In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than K. We will shrink the window until we have no more than K distinct characters in the HashMap. This is needed as we intend to find the longest window.
# While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if its frequency becomes zero.
# At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.

  letter_frequency = {}
  longest = 0
  window_start = 0

  if k >= len(set(str)):
    return k
  for letter in str:
    if letter not in letter_frequency:
      letter_frequency[letter] = 1
    else:

      substring += letter
      longest += 1




  return longest
