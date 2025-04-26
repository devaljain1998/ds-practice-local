from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(pos):
            if pos < 0:
                return 0
            
            # Loot the current house
            c1 = helper(pos - 2) + nums[pos]
            # Don't loot the current house and move to the next house:
            c2 = helper(pos-1)
            
            return max(c1, c2)
        
        return helper(len(nums) - 1)
