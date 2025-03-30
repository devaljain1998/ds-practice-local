from typing import List


def subset_sum(nums: List[int], subset_sum: int) -> bool:
    n = len(nums)
    dp = [[False for _ in range(subset_sum + 1)] for _ in range(n + 1)]
    
    # If the the sum is 0, then the empty set is the answer:    
    for i in range(0, n + 1): 
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, subset_sum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = (
                    dp[i-1][j] or # exclude
                    dp[i - 1][j - nums[i - 1]] # include
                )
            else:
                dp[i][j] = dp[i - 1][j]
            
    return dp[n][subset_sum]

# Test cases:
print(subset_sum([2, 3, 7, 8, 10], 11)) # True
print(subset_sum([1, 3, 4, 8], 6)) # False
print(subset_sum([1, 3, 4, 8], 10)) # False
print(subset_sum([3, 34, 4, 12, 5, 2], 9)) # True