"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string. You can assume the string
has only uppercase and lowercase letters (a - z).
"""

# Compress strings: "aabcccccaaa" > "a2b1c5a3"
# If compressed str would not become smaller than original string, return original
# only upper and lowercase letters

# compress: traverse string, keep count of repeated characters
# if current and next character are same, ++ count
# otherwise concatenate current character and count to output string
# reset count to 1
# compare length of old and new strings, return shorter

# Input: string
# Output: compressed string
# Constraints: optimize
# Edge Cases: empty string, compressed string that's same length as the original string

# time complexity: linear
# space complexity: constant


def compress_strings(s):
    compressed = []
    count = 0
    for i in range(len(s)):
        if i != 0 and s[i] != s[i - 1]:
            compressed.append(s[i - 1] + str(count))
            count = 0
        count += 1

    # add last repeated character
    if count:
        compressed.append(s[-1] + str(count))

    # returns original string if compressed string isn't smaller
    return min(s, "".join(compressed), key=len)

s = 'aabcccccaaa'
print('aabcccccaaa > ', compress_strings(s))
