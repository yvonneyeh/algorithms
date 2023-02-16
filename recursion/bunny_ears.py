'''
❓ PROMPT
We have a number of bunnies, each with two big floppy ears. We want to compute the total number of ears across all the bunnies recursively, without loops or multiplication.

Example(s)
bunnyEars(3) == 6
bunnyEars(5) == 10


🔎 EXPLORE
State your assumptions & discoveries:

Q: Can I assume the input will be a positive integer?
A: It can be zero or positive


Create examples & test cases:

zero bunnies
1 bunny
even number of bunnies
odd number of bunnies


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O(n) where n is the number of bunnies
Space: O(n) where n is the number of stack frames because one is created for each bunny


📆 PLAN
High-level outline of approach #:

# Base case: if bunnies==0, just return 0.
  if bunnies == 0:
    return 0

# Recursive case: make a recursive call with bunnies-1
# (towards the base case), and fix up what it returns.


🛠️ IMPLEMENT
function bunnyEars(bunnies) {
def bunnyEars(bunnies: int) -> int:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def bunnyEars(bunnies: int) -> int:

    if bunnies == 0:
        return 0

    return bunnyEars(bunnies - 1) + 2
