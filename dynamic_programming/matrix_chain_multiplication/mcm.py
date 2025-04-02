import sys


dp: list[list[int]] = []

def solve(arr: list[int], i: int, j: int) -> int:
    if i >= j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    result = sys.maxsize  # Initialize to infinity for minimization
    for k in range(i, j):
        left_matrix: int = solve(arr, i, k)
        right_matrix: int = solve(arr, k + 1, j)
        product = arr[i - 1] * arr[k] * arr[j]  # Corrected indices
        
        result = min(result, left_matrix + right_matrix + product)  # Minimize cost
    
    dp[i][j] = result
    return result

def mcm(arr: list[int]) -> int:
    global dp
    n = len(arr)
    dp = [[-1 for _ in range(n)] for _ in range(n)]  # Corrected dimensions
    
    result = solve(arr, 1, n - 1)  # Adjusted indices for proper slicing
    
    del dp  # Delete dp
    return result

# Test cases:
print(mcm([10, 20, 30]))  # Expected output: 6000