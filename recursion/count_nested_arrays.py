
"""
Given a nested array where each element may be 1) an integer or 2) an array, whose elements themselves may be integers or further arrays, count the total number of arrays.

What is the shape or pattern of this nested array structure? There can be empty lists but never None/null.


EXAMPLE(S)
countArrays([1, 2, 3]) == 1
countArrays([1, [1, 2, 3], 3]) == 2
countArrays([1, [1, [1, [1, [1]]]]]) == 5
countArrays([]) == 1


FUNCTION SIGNATURE
function countArrays(array) {
def countArrays(nestedList: list) -> int:
'''

-> if at all the list is None return 0
-> counter starts from 1
-> input is int or list, if list -> increment counter, int -> do nothing

*/
"""

from typing import List


def countArrays(nestedList: list) -> int:

    if nestedList is None:
        return 0

    counter =1
    # countArrays([1, [2, [3, [4, [5]]]]])
                #   i
    for i in nestedList:
        if type(i) is list:
            counter += countArrays(i)
            # counter = countArrays(i) + 1
    print(counter)
    return counter


print(countArrays([1, 2, 3]) == 1)
print(countArrays([1, [1, 2, 3], 3]) == 2)
print(countArrays([1, [1, [1, [1, [1]]]]]) == 5)
print(countArrays([]) == 1)
