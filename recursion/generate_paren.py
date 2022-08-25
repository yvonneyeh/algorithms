# Generate Parentheses
"""
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # only add open paren if open < n
        # only add close paren if close < n
        # stop (valid) when open == close == n [base case]

        stack = []
        result = []

        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()
            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return result
