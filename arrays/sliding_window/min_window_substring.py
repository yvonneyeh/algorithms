# 76. Minimum Window Substring

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # have = count of matching chars
        # keep track of 2 pointers, left and right
        # increment r while the have is less than need (len t)
        # shrink window while have = need

        if t == "" or len(t) > len(s): return ""

        target, window = {}, {}

        for letter in t:
            target[letter] = target.get(letter, 0) + 1

        have, need = 0, len(target)
        l = 0
        res_len = float("infinity")
        result = [0, 0]

        for r, letter in enumerate(s):
            window[letter] = window.get(letter, 0) + 1

            if letter in target and target[letter] == window[letter]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    result = [l, r]
                    res_len = r - l + 1
                    print(res_len)
                # pop from the left of our window
                left = s[l]
                window[left] -= 1
                if left in target and window[left] < target[left]:
                    have -= 1
                l += 1
        l, r = result
        return s[l : r + 1] if res_len != float("infinity") else ""
