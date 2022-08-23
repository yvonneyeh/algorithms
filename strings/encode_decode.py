# Encode and Decode Strings

"""
Medium

Problem: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode

Example(s):

Example1

Input: [“lint”,“code”,“love”,“you”] Output: [“lint”,“code”,“love”,“you”] Explanation: One possible encode method is: “lint:;code:;love:;you”

Example2

Input: [“we”, “say”, “:”, “yes”] Output: [“we”, “say”, “:”, “yes”] Explanation: One possible encode method is: “we:;say:;:::;yes”

"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '.' + s
        return encoded
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        decoded = []
        i = 0
        while i < len(str):
            j = i
            if str[j] == '.':
                j += 1
            length = i + j
            decoded.append(str[j+1 : j+length])
            i = j + 1 + length
        return decoded
