# Valid Parentheses
# Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


def isValid_dict(self, s: str) -> bool:
    # create a stack to keep track of characters
    # if it's an opening paren, push it to stack
    # if it's a closing paren, pop it
    # (())
    # stack should be empty for valid paren

    stack = []
    paren_map = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for c in s:
        if c in paren_map:
            if stack and stack[-1] == paren_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


def isValid_list(self, s: str) -> bool:

    # open and closing lists
    # init stack
    # look at every char in s
    # if char is in open, append to stack
    # if not, check if there is item in stack and last item matches opening index
        # pop item if valid
        # else = not valid

    # return true if len of stack is empty

    opened = ['(','{','[']
    closed = [')','}',']']
    stack = []

    for c in s:
        if c in opened:
            stack.append(c)
        else:
            if stack and stack[-1] == opened[closed.index(c)]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

class Solution_dict:
    def isValid(self, s: str) -> bool:

        # if it's the left bracket then we append it to the stack
        # else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
        # finally check if the stack still contains unmatched left bracket

        parens = {'(':')', '{':'}','[':']'}
        stack = []

        for c in s:
            if c in parens:
                stack.append(c)
            elif not stack or parens[stack.pop()] != c:
                    return False
        return len(stack) == 0
