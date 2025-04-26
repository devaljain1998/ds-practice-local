from typing import List
from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @lru_cache(maxsize=100000)
        def solve(pos: int, prev_ind: int) -> int:
            # Base cases:
            if pos == n:
                return 0

            # Take:
            take = float('-inf')
            if prev_ind == -1 or nums[pos] > nums[prev_ind]:
                take = 1 + solve(pos+1, pos)
            skip = solve(pos+1, prev_ind)
            
            return int(max(take, skip))
        
        return solve(0, -1)