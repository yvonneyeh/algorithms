def reverse_string(string):

    return string[::-1]

# Q. Given a string, a target string, and a frequency f, remove the target f number of times from the beginning of the input string. If f exceeds the number of target strings appeared in the input string, do nothing.

def solution(string, target, f):

    if (f * len(target)) > len(string):
        return string

    return string.replace(target, "", f)


# Q. Given a string and a target string, count the number of times the target string shows up in the input string. String parts that were already counted cannot be counted again (no overlapping allowed).
#
# Example:
# Input: "111", target = "11"
# Output: 1 (if the overlapping was allowed, the answer would be 2)


def solution(string, target):

    if not string or not target:
        return 0

    return string.count(target)


# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).
#
# Example
#
# For inputString = "crazy", the output should be solution(inputString) = "dsbaz".

def solution(inputString):

    result = []


    for item in inputString:
        num = ord(item)
        if num == ord('z'):
            num = ord('a')
        else:
            num += 1
        result.append(chr(num))

    return ('').join(result)


# Q. Given a string, add one space between each character.
#
# Example:
# Input: "Formation"
# Output: "F o r m a t i o n"
# [execution time limit] 4 seconds (py3)
#
# [input] string string
#
# [output] string
#
# [Python 3] Syntax Tips

def solution(string):

    result = []
    for item in string:
        result.append(item)

    return (' ').join(result)


# Q. Given a string, find the character that appears most frequently. You may assume there is only one most frequent character.


def solution(string):

    char_count = {}
    most_common_char = ""
    top_count = 0

    for item in string:
        char_count[item] = char_count.get(item, 0) + 1

    for key, value in char_count.items():
        if value > top_count:
            top_count = value
            most_common_char = key

    return most_common_char
