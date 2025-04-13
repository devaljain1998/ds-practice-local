from typing import Deque, List
from collections import deque

EMPTY = 0
FRESH = 1
ROTTEN = 2

POSITIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minutes = 0
        queue: Deque = deque()
        
        # Insert all the ROTTEN oranges at minute 0:
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                    
        while queue:
            sz = len(queue)
            temp = False
            # Multi-source BFS:
            while sz > 0:
                current_pos = queue.popleft()
                x, y = current_pos
                
                # Moving all the directions and making rotting the
                # oranges:
                for dx, dy in POSITIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == FRESH:
                        grid[nx][ny] = ROTTEN
                        queue.append((nx, ny))
                        temp = True

                sz -= 1
            
            if temp:                    
                minutes += 1

        # Check if all the oranges were changed to ROTTEN
        # Else return impossible
        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    return -1

        return minutes
    
# Test cases:
# Test case 1:
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Output: 4
                