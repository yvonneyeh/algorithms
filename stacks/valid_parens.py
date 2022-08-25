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
