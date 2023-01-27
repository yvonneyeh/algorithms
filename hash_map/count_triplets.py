"""
You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio `r` and i < j < k.

Example

arr = [1,4,16,64]
r = 4

There are [1,4,6] and [4,16,64] at indices (0,1,2) and (1,2,3). Return 2

Function Description

Complete the countTriplets function in the editor below.

countTriplets has the following parameter(s):

int arr[n]: an array of integers
int r: the common ratio
Returns

int: the number of triplets
Input Format

The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .

"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):

    # dictionary of key = number, value = [indices]
    # iterate thru numbers, 1
    # if next progression exists in dictionary, (4 > index)

    # key = item in arr
    # value = count of item in arr

    # num_dictionary = {}
    # result = 0

    # for num in arr:
    #     num_dictionary[num] = num_dictionary.get(num, 0) + 1

    # for key in num_dictionary.keys():
    #     if key == key * r:
    #         result += num_dictionary[key] * num_dictionary[key*r] - 1 * num_dictionary[key*r*r] - 2
    #     elif key * r in num_dictionary.keys() and key * r * r in num_dictionary.keys():
    #         result += num_dictionary[key] * num_dictionary[key*r] * num_dictionary[key*r*r]

    # return result

    num_dictionary = {}
    result = 0

    for num in arr:
        num_dictionary[num] = num_dictionary.get(num, 0) + 1

    for key in num_dictionary.keys():
        if key == key * r:
            result += num_dictionary[key] * num_dictionary[key*r] - 1 * num_dictionary[key*r*r] - 2
        elif key * r in num_dictionary.keys() and key * r * r in num_dictionary.keys():
            result += num_dictionary[key] * num_dictionary[key*r] * num_dictionary[key*r*r]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
