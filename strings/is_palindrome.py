# Given a string, check if it's a palindrome (same read forwards and backwards)

# Are letters case sensitive? If so, convert all to lowercase first

def is_palindrome_reverse(s):
    s = s.lower()
    return s == reversed(s)

def is_palindrome_slice_notation(s):
    return s == s[::-1]

def is_palindrome_(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
# Time complexity: O(n)
# Auxiliary Space: O(1)
