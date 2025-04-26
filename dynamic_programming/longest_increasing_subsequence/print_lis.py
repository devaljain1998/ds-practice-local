class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp = [1 for i in range(N+1)]
        
        for i in range(N, -1, -1):
            for idx 