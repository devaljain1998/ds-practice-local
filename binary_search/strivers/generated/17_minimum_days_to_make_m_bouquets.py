"""17. Minimum Number of Days to Make m Bouquets (LeetCode 1482)

You have n flowers in a row. The ith flower blooms on day bloomDay[i].
You want to make m bouquets. Each bouquet must use exactly k adjacent flowers,
and each flower can be used in at most one bouquet.

Return the minimum day on which you can make all m bouquets. Return -1 if it
is impossible, even after every flower has bloomed.

Example 1:
    Input: bloomDay = [1, 10, 3, 10, 2], m = 3, k = 1
    Output: 3
    Explanation: On day 3, the flowers at indices 0, 2, and 4 have bloomed.
    Each can form a one-flower bouquet. Before day 3, only two have bloomed.

Example 2:
    Input: bloomDay = [1, 10, 3, 10, 2], m = 3, k = 2
    Output: -1
    Explanation: Three bouquets of two flowers need six distinct flowers,
    but there are only five.

Example 3:
    Input: bloomDay = [7, 7, 7, 7, 12, 7, 7], m = 2, k = 3
    Output: 12
    Explanation: On day 7, the two runs of bloomed flowers have lengths four
    and two, so they yield only one bouquet. On day 12, all seven flowers have
    bloomed and two disjoint bouquets are possible.

Constraints:
    1 <= len(bloomDay) <= 100_000
    1 <= bloomDay[i] <= 1_000_000_000
    1 <= m <= 1_000_000
    1 <= k <= 1_000_000
"""

def is_valid(bloomDays, m, k, mx):
    boquets = 0
    flowers = 0
    for bloomDay in bloomDays:
        # Flower is not bloomed
        if bloomDay > mx:
            flowers = 0
            continue
        
        flowers += 1
        # If flowers are forming a boquet:
        if flowers == k:
            flowers = 0
            boquets += 1
    
    return boquets >= m
        


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        # Not possible
        if m * k > n:
            return -1

        left = 1
        right = max(bloomDay)

        min_days = -1
        while left <= right:
            mid = left + (right - left) // 2
            if is_valid(bloomDay, m, k, mid):
                min_days = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_days


METHOD = "minDays"
TEST_CASES = [
    ("easy: single flower bouquets", ([1, 10, 3, 10, 2], 3, 1), 3),
    ("easy: impossible", ([1, 10, 3, 10, 2], 3, 2), -1),
    ("medium: adjacency matters", ([7, 7, 7, 7, 12, 7, 7], 2, 3), 12),
    ("medium: separate runs", ([1, 2, 4, 9, 3, 4], 2, 2), 4),
    ("easy: one flower blooms immediately", ([1], 1, 1), 1),
    ("easy: one flower blooms on maximum day", ([1_000_000_000], 1, 1), 1_000_000_000),
    ("easy: all flowers bloom together", ([5] * 8, 2, 4), 5),
    ("easy: one flower short of required capacity", ([1] * 5, 3, 2), -1),
    ("medium: every flower is required", ([4, 2, 9, 1, 7, 3], 2, 3), 9),
    ("medium: one run cannot reuse flowers", ([1] * 5 + [10], 3, 2), 10),
    ("medium: early groups separated by late flower", ([2, 2, 100, 2, 2], 2, 2), 2),
    ("medium: early flowers are nonadjacent", ([1, 10, 1, 10, 1, 10, 1], 2, 2), 10),
    ("medium: single flower bouquets with duplicate days", ([8, 2, 4, 2, 8, 6], 4, 1), 6),
    ("medium: late flower bridges short runs", ([1, 1, 9, 1, 1], 1, 3), 9),
    ("medium: late flowers are unnecessary", ([3, 3, 99, 3, 3, 99], 2, 2), 3),
    ("hard: large separated early groups", ([1, 1, 1, 1_000_000_000] * 5_000, 5_000, 3), 1),
    ("hard: large one more bouquet needed", ([1, 1, 1, 1_000_000_000] * 5_000, 5_001, 3), 1_000_000_000),
    ("hard: large alternating bloom days", ([1, 1_000_000_000] * 10_000, 5_000, 2), 1_000_000_000),
]


# Test case 1:
if __name__ == '__main__':
    print(Solution().minDays([1,10,3,10,2], 3, 1))
