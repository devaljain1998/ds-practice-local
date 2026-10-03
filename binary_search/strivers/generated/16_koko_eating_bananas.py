"""16. Koko Eating Bananas

Koko has ``piles[i]`` bananas in the ith pile. The guards will return in
``h`` hours. She chooses an integer eating speed ``k`` bananas per hour.

Each hour, Koko chooses one pile and eats up to ``k`` bananas from it. If the
pile has fewer than ``k`` bananas, she finishes that pile and does not eat
from another pile during the same hour.

Return the minimum positive integer ``k`` that lets her eat every banana
before the guards return.

Example 1:
    Input: piles = [3, 6, 7, 11], h = 8
    Output: 4
    Explanation: At speed 4, the piles take 1, 2, 2, and 3 hours.

Example 2:
    Input: piles = [30, 11, 23, 4, 20], h = 5
    Output: 30
    Explanation: There is only one hour available for each pile.

Example 3:
    Input: piles = [30, 11, 23, 4, 20], h = 6
    Output: 23

Constraints:
    1 <= len(piles) <= 10,000
    1 <= piles[i] <= 1,000,000,000
    len(piles) <= h <= 1,000,000,000
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        raise NotImplementedError


METHOD = "minEatingSpeed"
TEST_CASES = [
    ("easy: one banana in one hour", ([1], 1), 1),
    ("easy: single pile in one hour", ([8], 1), 8),
    ("easy: single pile with generous time", ([9], 100), 1),
    ("easy: all ones", ([1, 1, 1], 3), 1),
    ("medium: example one", ([3, 6, 7, 11], 8), 4),
    ("medium: one hour per pile", ([30, 11, 23, 4, 20], 5), 30),
    ("medium: one extra hour", ([30, 11, 23, 4, 20], 6), 23),
    ("medium: equal piles with exact hours", ([5, 5, 5, 5], 4), 5),
    ("medium: equal piles with double hours", ([5, 5, 5, 5], 8), 3),
    ("medium: speed just above a divisor", ([9, 9, 9], 6), 5),
    ("medium: one large pile plus two small", ([1, 1, 100], 4), 50),
    ("hard: maximum pile and maximum hours", ([1_000_000_000], 1_000_000_000), 1),
    ("hard: maximum piles in minimum hours", ([1_000_000_000, 1_000_000_000], 2), 1_000_000_000),
    ("hard: maximum piles in double hours", ([1_000_000_000, 1_000_000_000], 4), 500_000_000),
    ("hard: rounding at a billion", ([1_000_000_000, 1, 1], 5), 333_333_334),
    ("hard: ten thousand mixed piles", ([1] * 9_999 + [1_000_000_000], 10_001), 500_000_000),
    ("hard: ten thousand maximum piles", ([1_000_000_000] * 10_000, 20_000), 500_000_000),
]
