"""
# Problem List

1. function reduce(head, accumulator, initialVal) - returns single value
2. function map(head, mapper) - returns new list
3. function any(head, test) - returns true if at least one value passes the test function
4. function all(head, test) - returns true if ALL of the values in the list pass the test function

BONUS: function filter(head, test) - modifies list and returns new head
"""

class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next


def sum(total, currentValue):
    return total + currentValue

def reduce(head, doReduce, initialVal = 0):
    result = initialVal
    current = head

    while current:
        result = doReduce(result, current.value)
        current = current.next

    return result

reduce(head, sum, 0)

"""
sourceHead: (112) -> (475) -> (5638) -> None
convert: lambda x: x * 10
sourceCurrent: (475) -> ...
targetHead: (1120) -> () -> None
targetCurrent: () -> None
"""

def map(sourceHead, convert):
    if not sourceHead: return sourceHead

    sourceCurrent = sourceHead
    targetHead = Node()
    targetCurrent = targetHead

    while True:
        targetCurrent.value = convert(sourceCurrent.value)
        sourceCurrent = sourceCurrent.next
        if not sourceCurrent break

        targetCurrent.next = Node()
        targetCurrent = targetCurrent.next

    return targetHead


def any(node, isTargetValue):
    while node:
        if isTargetValue(node.val): return True
        node = node.next

    return False

def all(node, isTargetValue):
    while node:
        if not isTargetValue(node.val): return False
        node = node.next

    return True
