# find the length of the longest valid substring in a string of parens, where valid means that all open brackets have a closed bracket

"""
Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()()

Input:  ()(()))))
Output: 6
Explanation:  ()(())
"""

# For every string, check if it is a valid string or not.
# If valid and length is more than maximum length so far, then update maximum length.
# We can check whether a substring is valid or not in linear time using a stack
# return length of stack

1) Create an empty stack and push -1 to it.
   The first element of the stack is used
   to provide a base for the next valid string.

2) Initialize result as 0.

3) If the character is '(' i.e. str[i] == '('),
   push index'i' to the stack.

2) Else (if the character is ')')
   a) Pop an item from the stack (Most of the
      time an opening bracket)
   b) If the stack is not empty, then find the
      length of current valid substring by taking
      the difference between the current index and
      top of the stack. If current length is more
      than the result, then update the result.
   c) If the stack is empty, push the current index
      as a base for the next valid substring.

3) Return result.

def findMaxLen(string):
    n = len(string)

    # Create a stack and push -1
    # as initial index to it.
    stk = []
    stk.append(-1)

    # Initialize result
    result = 0

    # Traverse all characters of given string
    for i in range(n):

        # If opening bracket, push index of it
        if string[i] == '(':
            stk.append(i)

        # If closing bracket, i.e., str[i] = ')'
        else:

            # Pop the previous opening bracket's index
            if len(stk) != 0:
               stk.pop()

            # Check if this length formed with base of
            # current valid substring is more than max
            # so far
            if len(stk) != 0:
                result = max(result,
                             i - stk[len(stk)-1])

            # If stack is empty. push current index as
            # base for next valid substring (if any)
            else:
                stk.append(i)

    return result


def find_longest_valid_parens(s):
    stack = []
    restult = 0

    # Traversing the Expression
    for paren in s:
        if paren in ["(", "{", "["]:
            stack.append(paren)
        else:
            if len(stack) != 0:
                stack.pop()
            
    return result
