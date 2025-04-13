from typing import List


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(image: List[List[int]], i: int, j: int, original_color: int, new_color: int):
    def is_valid(i: int, j: int) -> bool:
        return 0 <= i < len(image) and 0 <= j < len(image[0])
    
    if not is_valid(i, j) or image[i][j] != original_color:
        return
    
    image[i][j] = new_color
    
    for dx, dy in directions:
        new_i, new_j = i + dx, j + dy
        if is_valid(new_i, new_j) and image[new_i][new_j] == original_color:
            dfs(image, new_i, new_j, original_color, new_color)

class Solution:
    def floodFill(self, image: List[List[int]], i: int, j: int, color: int) -> List[List[int]]:
        original_color = image[i][j]
        if original_color == color:
            return image
        
        dfs(image, i, j, original_color, color)
                    
        return image