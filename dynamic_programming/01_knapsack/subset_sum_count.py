from typing import List

# subset_sum_count returns the number of subsets that sum up to the given sum
def subset_sum_count(arr: List[int], n: int, target: int) -> int:
    dp: List[List[int]] = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    
    for i in range(0, target + 1):
        dp[0][i] = 0
    # Empty subsets make it possible to form a subset sum of 0
    for i in range(0, n + 1):
        dp[i][0] = 1
        
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Include or exclude
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            # exclude:
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Return last element of the matrix:
    return dp[n][target]

# Test cases:
print(subset_sum_count([2, 3, 5, 6, 8, 10], 6, 10)) # 3
print(subset_sum_count([1, 2, 3, 4, 5], 5, 10)) # 3
print(subset_sum_count([1, 2, 3, 4, 5], 5, 15)) # 1