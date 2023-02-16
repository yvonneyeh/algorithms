'''
❓ PROMPT
Given a base-10 integer as a string, parse the integer and return it as an int. This problem can be done iteratively and recursively, and it's worth doing both!

Example(s)
atoi("123") == 123
atoi("4") == 4
atoi("007") == 7
atoi("-1") == -1


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can the string contain leading zeroes?
A: Yes
Q: What about negative numbers?
A: Yes
Q: What if the number will be bigger than the size of an int? (e.g. greater than or equal to 2^31 in Java)
A: We can assume the number will always be smaller than the size of an int.
Q: Can I use parseInt?
A: No. The intent of this exercise is to learn how this function works.
Q: Will there be +, decimals, commas, or other characters?
A: No, the provided characters will only be the negative sign, '-', and the digits 0 through 9.
Q: Can the numbers be in exponential notation, like 14e2?
A: No.

Create examples & test cases:

a negative number
zero
a positive number
a number with leading zeros
a number with trailing zeros
a number with leading and trailing zeros


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:

O(n), where n is the length of the string


🛠️ IMPLEMENT
function atoi(intAsString) {
def atoi(intAsString: str) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def atoi_iterative(intAsString: str) -> int:
  charMap = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
  }
  value = 0
  negative = intAsString[0] == '-'
  start = 1 if negative else 0
  for i in range(start, len(intAsString)):
    digit = charMap[intAsString[i]]
    value = value * 10 + digit
  return -value if negative else value

def atoi_recursive(intAsString: str) -> int:
  charMap = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
  }
  def recursiveHelper(intAsString, index, value = 0):
    if index == len(intAsString):
      return value

    nextValue = value * 10 + charMap[intAsString[index]]
    return recursiveHelper(intAsString, index + 1, nextValue)

  negative = intAsString[0] == '-'
  start = 1 if negative else 0

  value = recursiveHelper(intAsString, start)
  return -value if negative else value
