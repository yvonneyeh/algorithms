"""
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""

def lengthOfLongestSubstring(s):
    # keep track of start and end index for substring
    # use dictionary to save letters we've seen
    # save longest length, update it by checking if end - right is longer than current

    start = 0
    seen = set()
    longest = 0

    for end, letter in enumerate(s):
        while letter in seen:
            seen.remove(s[start])
            start += 1
        else:
            seen.add(letter)
            longest = max(longest, end - start + 1)

    return longest

# sliding window - keep track of start index
# create dictionary to keep track of letters we've seen
# loop through indices, if letter not in dictionary, add it
# if it is, stop
# add


def non_repeat_substring(s):
    seen = {}
    max_length = 0
    start = 0
    for i, character in enumerate(s):
        if character in seen and start <= seen[character]:
            start = seen[character] + 1
        else:
            max_length = max(max_length, i - start + 1)

        seen[character] = i

    return max_length

def main():
    print("aabccbb -> 3", non_repeat_substring("aabccbb"))
    print("abbbb -> 2", non_repeat_substring("abbbb"))
    print("abccde -> 3", non_repeat_substring("abccde"))


main()
