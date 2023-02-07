'''
Given a nested array where each element may be 1) an integer or 2) an array, whose elements may be integers or other arrays, compute the sum of all the integers in the nested array.

What is the shape or pattern of this nested array structure?

As a follow-up, modify this code to multiply each list sum by its depth in the nesting. [1, 2] returns 3 since (1 + 2) is only inside one array.

However, [4, [2, 3]] returns 14 because the depth of [2, 3] is 2, so (2+3) * 2 = 10.
4 is added at the end to get 10 + 4 = 14.
While [4, [2, [3]]] returns 26 because the depth of [3] is 3 so 3 * 3 = 9.
Then the depth of [2, 9] is 2 so (2+9) * 2 = 22.
4 is added at the end to get  22 + 4 = 26.


EXAMPLE(S)
sumNestedList([1, 2, 3]) == 6
sumNestedList([1, [1, 2, 3], 3]) == 10
sumNestedList([1, [1, [1, [1, [1]]]]]) == 5
sumNestedList([]) == 0
sumNestedList([1, []]) == 1

sumNestedListWithDepth([4, [2, 3]]) == 14 because 4 + (2+3)*2
sumNestedListWithDepth([4, [2, [3]]]) == 26 because 4+(2+ (3*3))*2


FUNCTION SIGNATURE
function sumNestedList(list) {
function sumNestedListWithDepth(list) {

def sumNestedList(nestedList: list[int]) -> int:
def sumNestedListWithDepth(nestedList: list[int]) -> int:
'''

def sumNestedList(nestedList: list[int]) -> int:
    if not nestedList:
        return 0
    total = 0
    for element in nestedList:
        if type(element) == int:
            total += element
        else:
            total += sumNestedList(element)
    return total

print(sumNestedList([1, 2, 3]) == 6)
print(sumNestedList([1, [1, 2, 3], 3]) == 10)
print(sumNestedList([1, [1, [1, [1, [1]]]]]) == 5)
print(sumNestedList([]) == 0)
print(sumNestedList([1, []]) == 1)

def sumNestedListWithDepth(nestedList: list[int], depth: int = 1) -> int:
    if not nestedList:
        return 0
    total = 0
    for element in nestedList:
        if type(element) == int:
            total += element * depth
        else:
            total += sumNestedListWithDepth(element, depth + 1) * depth
    return total

print(sumNestedListWithDepth([4, [2, 3]]) == 14) # 4+(2+3)*2
print(sumNestedListWithDepth([4, [2, [3]]]) == 26) # 4+(2+(3*3))*2
