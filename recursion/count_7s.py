'''
❓ PROMPT
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops).

Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while integer division by 10 removes the rightmost digit (126 / 10 is 12). Be aware that some languages require some special handling to do integer division while others do not.

*Python integer division*: x // y
*Javascript integer division*: Math.floor(x / y)

Example(s)
count7(7) == 1
count7(123) == 0
count7(717) == 2


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can I assume the input will be a positive integer?
A: It can be zero or positive


Create examples & test cases:

zero
single digits
numbers with all 7's
numbers with no 7's
numbers with a mixture of digits including 7


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(n) where n is the number of digits
Space: O(n) where n is the number of digits to create each stack frame


📆 PLAN
High-level outline of approach #:

The base case is when the input is a single digit.


🛠️ IMPLEMENT
function count7(n) {
def count7(n: int) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def  count7(n: int) -> int:
  if n == 0:
    return 0

  if n % 10 == 7:
    return 1 + count7(n // 10)

  return count7(n // 10)


print(count7(717) == 2)
print(count7(7) == 1)
print(count7(5) == 0)
print(count7(123) == 0)
print(count7(77) == 2)
print(count7(7123) == 1)
print(count7(771237) == 3)
print(count7(771737) == 4)
print(count7(47571) == 2)
print(count7(777777) == 6)
print(count7(70701277) == 4)
print(count7(777576197) == 5)
print(count7(99999) == 0)
print(count7(99799) == 1)
