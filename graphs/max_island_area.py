# Max Area of Island
# LeetCode 695

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        biggestIslandArea = 0

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1):  # only if the cell is a land
                    # we have found an island
                    biggestIslandArea = max(
                        biggestIslandArea, self.visitIslandDFS(grid, r, c))

        return biggestIslandArea


    def visitIslandDFS(self, grid,  x,  y):
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return 0  # return, if it is not a valid cell
        if (grid[x][y] == 0):
            return 0  # return, if it is a water cell

        grid[x][y] = 0  # mark the cell visited by making it a water cell

        area = 1 # counting the current cell
        # recursively visit all neighboring cells (horizontally & vertically)
        area += self.visitIslandDFS(grid, x + 1, y)  # lower cell
        area += self.visitIslandDFS(grid, x - 1, y)  # upper cell
        area += self.visitIslandDFS(grid, x, y + 1)  # right cell
        area += self.visitIslandDFS(grid, x, y - 1)  # left cell
        return area
