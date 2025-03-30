from typing import List

def subset_sum_count(arr: List[int], target: int) -> int:
    n = len(arr)
    dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    
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
        
    return dp[n][target]

def subset_count_with_a_difference(arr: List[int], diff: int) -> int:
    """
    s1 - s2 = t
    s1 + s2 = T
    s1 - (T - s1) = t
    2s1 = t + T
    s1 = (t + T) / 2
    """
    total_sum: int = sum(arr)
    s1: int = (diff + total_sum) // 2
    return subset_sum_count(arr, s1)

# Test cases:
print(subset_count_with_a_difference([1, 1, 2, 3], 1)) # 3
print(subset_count_with_a_difference([1, 2, 7], 4)) # 1
print(subset_count_with_a_difference([1, 2, 7], 5)) # 2