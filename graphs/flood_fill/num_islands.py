from typing import List

def flood_fill_dfs(grid: List[List[str]], i: int, j: int, original_color: str, new_color: str):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    
    if grid[i][j] != original_color:
        return
    
    grid[i][j] = new_color
    
    flood_fill_dfs(grid, i + 1, j, original_color, new_color)
    flood_fill_dfs(grid, i - 1, j, original_color, new_color)
    flood_fill_dfs(grid, i, j + 1, original_color, new_color)
    flood_fill_dfs(grid, i, j - 1, original_color, new_color)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if  grid[i][j] == '1':
                    flood_fill_dfs(grid, i, j, '1', '2')
                    num_islands += 1
        
        return num_islands
        