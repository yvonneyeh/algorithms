#1021. Remove Outermost Parentheses

# Given a valid string s, remove the outermost parentheses of each block of nested parentheses. E.g. (()()) => ()()

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        stack = []

        # basket is used to store previous value
        temp = ''

        for p in S:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()
            print("stack", stack)
            temp += p

            # empty stack = valid decomposition
            # remove the outer parentheses and put it in the result
            # clean up temp
            if not stack:
                print("temp", temp)
                result.append(temp[1:-1])
                temp = ''

        return ''.join(result)

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        open = 0
        result = []
        for x in S:
            if x == ')':
                open -= 1
            if open > 0:
                result.append(x)
            if x == '(':
                open += 1
        return ''.join(result)
