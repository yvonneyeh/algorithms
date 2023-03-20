'''
❓ PROMPT
Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

Example(s)
sumDigits(12) == 3
sumDigits(49) == 13
sumDigits(126) == 9


🔎 EXPLORE
State your assumptions & discoveries:
Q: Can I assume the input will be a positive integer?
A: It can be zero or positive

Create examples & test cases:
zero
single digit
multiple digits

🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(d) where d is the number of digits
Space: O(d) where d is the number of digits to create each stack frame


📆 PLAN
High-level outline of approach #:
The base case is when the input is a single digit.

🛠️ IMPLEMENT
function sumDigits(n) {
def sumDigits(n: int) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def sumDigits(n: int) -> int:
  if n < 10:
    return n

  return n % 10 + sumDigits(n // 10)

print(sumDigits(126) == 9)
print(sumDigits(49) == 13)
print(sumDigits(12) == 3)
print(sumDigits(10) == 1)
print(sumDigits(1) == 1)
print(sumDigits(0) == 0)
print(sumDigits(730) == 10)
print(sumDigits(1111) == 4 )
print(sumDigits(11111) == 5)
print(sumDigits(10110) == 3)
print(sumDigits(235) == 10)
