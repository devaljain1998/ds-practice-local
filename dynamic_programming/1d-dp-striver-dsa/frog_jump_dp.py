from functools import cache

#User function Template for python3
class Solution:
    def minCost(self, height):
        dp = [0] * (len(height))
        dp[1] = abs(height[1] - height[0])
        for i in range(2, len(height)):
            dp[i] = min(
                dp[i-1] + abs(height[i] - height[i-1]),
                dp[i-2] + abs(height[i] - height[i-2])
            )
        return dp[len(height) - 1]
