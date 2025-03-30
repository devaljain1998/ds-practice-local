import sys
from typing import List


def subset_sum(nums: List[int], subset_sum: int) -> List[List[bool]]:
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
            
    return dp

def minimum_subset_sum_difference(nums: List[int]) -> int:
    """
    s1 - s2 = minimized
    s1 + s2 = total_sum
    s1 = total_sum - s2
    so we need to minimize:
    s1 - s2 => s1 - (total_sum - s1) => 2s1 - total_sum
    2s1 - total_sum => minimized
    """
    total_sum: int = sum(nums)
    subset_sum_matrix: List[List[bool]] = subset_sum(nums, total_sum)
    minimum_subset_sum : int = sys.maxsize
    n: int = len(nums)
    
    for i in range((total_sum // 2) + 1):
        if subset_sum_matrix[n][i]:
            minimum_subset_sum = min(minimum_subset_sum, abs(total_sum - 2*i))
            
    return minimum_subset_sum

# Test cases:
print(minimum_subset_sum_difference([1, 2, 7])) # 4
print(minimum_subset_sum_difference([1, 2, 3, 9])) # 3
print(minimum_subset_sum_difference([1, 2, 3, 9])) # 3
print(minimum_subset_sum_difference([1, 2, 3, 5])) # 1
print(minimum_subset_sum_difference([1, 2, 3, 6])) # 0