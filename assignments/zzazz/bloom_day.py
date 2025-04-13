# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
from typing import List


# [7,7,7,7,12,7,7],2,3
# Output: 12 days

# Solution:
def solve(bloomDay: List[int], m: int, k: int) -> int:
    if len(bloomDay) < m * k:
        return -1

    left, right = min(bloomDay), max(bloomDay)

    def can_make_bouquets(mid: int) -> bool:
        bouquets = 0
        flowers = 0
        for day in bloomDay:
            if day <= mid:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    while left < right:
        mid = (left + right) // 2
        if can_make_bouquets(mid):
            right = mid
        else:
            left = mid + 1

    return left
