#74. Search a 2D Matrix
# Medium
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class BinarySearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # BINARY SEARCH
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row *  col - 1

        while l < r:
            mid = (l + r) // 2
            # position of mid map to 2d matrix
            if matrix[mid // col][mid % col] < target:
                l = mid + 1
            else:
                r = mid
        return target == matrix[l//col][l % col]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]: # last digit in row
                top = row + 1 # move the top pointer down
            elif target < matrix[row][0]: # first digit in row
                bottom = row - 1
            else:
                break

        if not (top <= bottom):  # invalid pointers
            return False

        l, r = 0, COLS - 1
        row = (top + bottom) // 2

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:  # found target
                return True
        return False
