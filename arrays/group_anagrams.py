# 49. Group Anagrams
"""
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]


Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    # dictionary should contain sorted word as key, each word that matches as value
    # if we see the same count in the dictionary, add it to the list value

        dictionary = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word not in dictionary:
                dictionary[sorted_word] = [s]
            else:
                dictionary[sorted_word].append(s)

        return dictionary.values()

    # Runtime: 89 ms
    # Memory: 17.7 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    # dictionary should contain count of letters as key, each word that matches as value
    # if we see the same count in the dictionary, add it to the list value

        dictionary = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # ord('a') = 91
                # get index starting at 0 by subtracting ord number
                count[ord(c) - ord('a')] += 1
            print(count)
            dictionary[tuple(count)].append(s)
        return dictionary.values()

    # Runtime: 127 ms
    # Memory: 19.7 MB
