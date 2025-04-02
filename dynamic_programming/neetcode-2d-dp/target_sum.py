from typing import List


def subset_sum(nums, target):
    dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    for i in range(0, len(nums) + 1):
        dp[i][0] = 1

    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j - nums[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[len(nums)][target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        
        return subset_sum(nums, (total + target) // 2)
