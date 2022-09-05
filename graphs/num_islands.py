# Number of Islands
# LeetCode 200

"""
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

Example 2:

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

class BFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
                    # right, left, top, bottom

        if not grid or not grid[0]:
            return 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if (r in range(rows) and
                        c in range(cols) and
                       grid[r][c] == "1" and
                       (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands



class DFS:
    def numIslands(self, grid: List[List[str]]) -> int:
            if not grid or not grid[0]:
                return 0

            islands = 0
            visit = set()
            rows, cols = len(grid), len(grid[0])

            def dfs(r, c):
                if (
                    r not in range(rows)
                    or c not in range(cols)
                    or grid[r][c] == "0"
                    or (r, c) in visit
                ):
                    return

                visit.add((r, c))
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == "1" and (r, c) not in visit:
                        islands += 1
                        dfs(r, c)
            return islands


def countIslandsDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    totalIslands = 0

    for i in range(rows):
        for j in range(cols):
            if (matrix[i][j] == 1):  # only if the cell is a land
                # we have found an island
                totalIslands += 1
                visitIslandDFS(matrix, i, j)
    return totalIslands


def visitIslandDFS(matrix,  x,  y):
    if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
        return  # return, if it is not a valid cell
    if (matrix[x][y] == 0):
        return  # return, if it is a water cell

    matrix[x][y] = 0  # mark the cell visited by making it a water cell

    # recursively visit all neighboring cells (horizontally & vertically)
    visitIslandDFS(matrix, x + 1, y)  # lower cell
    visitIslandDFS(matrix, x - 1, y)  # upper cell
    visitIslandDFS(matrix, x, y + 1)  # right cell
    visitIslandDFS(matrix, x, y - 1)  # left cell


def main():
    print(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(countIslandsDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()
