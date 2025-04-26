from functools import cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        @cache
        def solve(i: int) -> int:
            # Reached the end
            if i == n:
                return 0
            
            # Exploring all partitions:
            length = 0
            maxi = float('-inf')
            max_sum = float('-inf')
            for j in range(i, min(n, i+k)):
                length += 1
                maxi = max(maxi, arr[j])
                max_sum = max(max_sum, maxi*length + solve(j+1))
            
            return max_sum
        
        return solve(0)