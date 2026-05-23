from typing import List

class Solution:
    def is_valid(self, bloomDay, m, k , days):
        """is it possible to make m boquets of k flowers each"""
        boquets = 0
        adjacent_flowers = 0

        for i in range(len(bloomDay)):
            bloomed = bloomDay[i] <= days
            if bloomed:
                adjacent_flowers += 1
                if adjacent_flowers % k == 0:
                    boquets += 1
            else:
                adjacent_flowers = 0
        
        return boquets >= m


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start = min(bloomDay)
        end = max(bloomDay)

        min_days = -1
        while start <= end:
            mid = start + (end - start) // 2

            if self.is_valid(bloomDay, m, k , mid):
                min_days = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return min_days