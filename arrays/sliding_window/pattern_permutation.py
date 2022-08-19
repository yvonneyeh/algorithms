# Permutation in a String (hard)

"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:
    Input: Text="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
    Input: Text="odicf", Pattern="dc"
    Output: false
    Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
    Input: Text="bcdxabcdy", Pattern="bcdyabcdx"
    Output: true
    Explanation: Both the string and the pattern are a permutation of each other.
Example 4:
    Input: String="aaacb", Pattern="abc"
    Output: true
    Explanation: The string contains "acb" which is a permutation of the given pattern.

Algorithm:
1. Create a HashMap to calculate the frequencies of all characters in the pattern.
2. Iterate through the string, adding one character at a time in the sliding window.
3. If the character being added matches a character in the HashMap, decrement its frequency in the map. If the character frequency becomes zero, we got a complete match.
4. If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the HashMap), we have gotten our required permutation.
5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s size. At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.
"""

class Solution1:
    def checkInclusion(text, pattern):
        frequency = {}
        window_start = 0
        matches = 0

        for letter in pattern:
            frequency[letter] = frequency.get(letter, 0) + 1

        for window_end, right_letter in enumerate(text):
            if right_letter in frequency:
                frequency[right_letter] -= 1
                if frequency[right_letter] == 0:
                    matches += 1

            if matches == len(frequency):
                return True

            if window_end >= len(pattern) - 1:
                left_letter = text[window_start]
                window_start += 1
                if left_letter in frequency:
                    if frequency[left_letter] == 0:
                        matches -= 1
                    frequency[left_letter] += 1

        return False

    # Runtime: 76 ms, O(N+M) - count of pattern and text items
    # Memory: 14 MB, O(M) - worst case: whole pattern has distinct characters in dictionary


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_count = Counter(s1)

        for i in range(len(s2) - window + 1):
            s2_count = Counter(s2[i:i+window])
            if s2_count == s1_count:
                return True

        return False

    # Runtime: 2450 ms
    # Memory: 13.7 MB

"""
Hashtable:
[Accepted]
[Runtime: 3556 ms, faster than 5.07% ]

One string is a permutation of another if the two strings have the same character frequencies
Hence:
find freq dict for s1
find freq dict for substrings of s2 (that are the same size as s1)
runtime: O(n*k)

   --2--
   [Accepted]
   [Runtime: 3556 ms, faster than 5.07% ]

   One string is a permutation of another if the two strings
   have the same character frequencies

   Hence:
       - find freq dict for s1
       - find freq dict for substrings of s2 (that are the same size as s1)

   runtime: O(n*k^2)
   """
class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)):  # ---- O(n)
            sub = s2[i:i+k]  # ------ O(k)
            d2 = Counter(sub) # --- O(k)
            if d1 == d2:
                return True
        return False
