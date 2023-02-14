# [ ] Given an integer array and an integer, find whether the integer exists in the array. Return a boolean.
# [] Replace all negative values with a 0

# [Y] Given an integer array and an integer, return how many times the integer exists in the array.



# Write a function to:
# 1. [I,Y, SP] Find mean of an integer array

# options for empty array as input
# - raise an Exception
# - return None
# - return 0 (pro: satisfies the interface / con: could be hiding something fishy going on, bug?)

def mean(arr):
    def get_sum(arr):
        if len(arr) == 1:
            return arr[0]
        sum = arr[0] + get_sum(arr[1:])
        return sum
    return get_sum(arr)/len(arr)

def mean2(arr):
    def get_sum(arr, index):
        if len(arr) - 1 < index:
            return 0;
        sum = arr[index] + get_sum(arr, index+1)
        return sum
    return get_sum(arr,0)/len(arr)


arr = [0, 1, 2, 5]
# print(mean(arr))
# print(mean2(arr))

# 2. [I,SP] Reverse the values in an array

def reverse_values(arr):
    return reverse_values(arr[1:]) + arr[0:1] if arr else []

# 0, 1, 2, 3
# A, B , C, D
# print(reverse_values(arr))
# print(reverse_values([]))


def reverse2_old(arr):
    def inner(arr, start, end):
        if start >= end:
            return
        # swap
        arr[start], arr[end] = arr[end], arr[start]
        return inner(arr, start+1, end-1)
    inner(arr, 0, len(arr)-1)

def reverse2(arr, start=0, end=None):
    if not end:
        end = len(arr)-1
    if start >= end:
        return
    # swap
    arr[start], arr[end] = arr[end], arr[start]
    return reverse2(arr, start+1, end-1)

arr = [0, 1, 2, 5]
reverse2(arr)
print(arr)


arr = []
reverse2(arr)
print(arr)
