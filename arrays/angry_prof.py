#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    # input = threshold, student arrival time
    # output = YES cancelled, NO not cancelled

    # look at all student arrival times, sorted
    # keep track of number of students that arrived on time
    # if on time students >= threshold, return NO
    # on time < threshold, return YES

    early_or_on_time_students = 0

    for time in a:
        if time <= 0:
            early_or_on_time_students += 1

    if early_or_on_time_students < k:
        return "YES"
    else:
        return "NO"





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
