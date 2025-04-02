def solve(arr: list[list[bool]], i: int, j: int, m: int, n: int, dp: dict) -> int:
    # state found in dp
    if (i, j) in dp:
        return dp[i, j]

    # reached the destination
    if i == (m-1) and j == (n-1):
        return 1
    
    # invalid states
    if i >= m or j >= n:
        return 0

    num_ways: int = 0
    # Mark the current state as visited:
    arr[i][j] = True

    # move right
    if j + 1 < n and not arr[i][j+1]:
        num_ways += solve(arr, i, j+1, m, n, dp)

    # move bottom
    if i + 1 < m and not arr[i+1][j]:
        num_ways += solve(arr, i+1, j, m, n, dp)

    # reverse the visited tile to backtrack:
    arr[i][j] = False

    dp[i, j] = num_ways
    return num_ways

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[False for _ in range(n)] for _ in range(m)]
        dp = dict()
        return solve(arr, 0, 0, m, n, dp)
        
# Test cases:
print(Solution().uniquePaths(3, 7))  # Expected output: 28