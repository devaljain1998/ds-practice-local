from typing import List


class Solution:
    def dfs(self, x, y, grid, visited, m, n):
        visited.add((x, y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newx, newy = x + dx, y + dy
            if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 1 and (newx, newy) not in visited:
                self.dfs(newx, newy, grid, visited, m, n)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        for i in range(n):
            if grid[0][i] == 1 and (0, i) not in visited:
                self.dfs(0, i, grid, visited, m, n)
            if grid[m-1][i] == 1 and (m-1, i) not in visited:
                self.dfs(m-1, i, grid, visited, m, n)

        for i in range(m):
            if grid[i][0] == 1 and (i, 0) not in visited:
                self.dfs(i, 0, grid, visited, m, n)
            if grid[i][n-1] == 1 and (0, n-1) not in visited:
                self.dfs(0, n-1, grid, visited, m, n)
        
        unreachable = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    unreachable += 1
        
        return unreachable
