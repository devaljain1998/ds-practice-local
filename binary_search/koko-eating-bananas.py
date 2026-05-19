from typing import List
from math import ceil


class Solution:
    def is_valid(self, piles: List[int], h: int, mx: int) -> bool:
        """Can Koko finish within h hours"""
        hours = 0

        for p in piles:
            hours += ceil(p / mx)

            # Check if hours exceeded h
            if hours > h:
                return False
        
        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1 # Must eat the minimum number of banana pile in any hour
        end = max(piles) # Atmax she can eat the entire pile in one hours
        # as she can only eat one pile in a given hour

        min_hours = -1

        while start <= end:
            # Maximum bananas that it can eat in an hour
            mid = start + (end - start) // 2

            if self.is_valid(piles, h, mid):
                min_hours = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return min_hours
