"""
Given a 2D rectangular matrix, return all of the values in a single, linear array in spiral order. Start at (0, 0) and first include everything in the first row. Then down the last column, back the last row (in reverse), and finally up the first column before turning right and continuing into the interior of the matrix.

For example:
 1  2  3  4
 5  6  7  8
 9 10 11 12
 13 14 15 16

Returns:

[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
"""

def spiralTraversal(matrix):
