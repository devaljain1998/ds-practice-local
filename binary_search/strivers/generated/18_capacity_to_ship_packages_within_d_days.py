"""18. Capacity to Ship Packages Within D Days

You are given a list ``weights`` where ``weights[i]`` is the weight of the
ith package on a conveyor belt. The packages must be shipped in their given
order. Each day, load a contiguous sequence of the remaining packages onto
one ship. Its total load cannot exceed the ship's daily capacity.

Return the minimum integer capacity needed to ship every package within
``days`` days. You may use fewer than ``days`` days.

Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation: A capacity of 15 can ship the packages as
    [1,2,3,4,5], [6,7], [8], [9], [10]. A capacity of 14 needs six days.

Example 2:
    Input: weights = [3,2,2,4,1,4], days = 3
    Output: 6
    Explanation: Ship [3,2], [2,4], and [1,4]. A capacity of 5 needs
    four days because packages cannot be reordered.

Example 3:
    Input: weights = [1,2,3,1,1], days = 4
    Output: 3

Constraints:
    1 <= len(weights) <= 50,000
    1 <= weights[i] <= 500
    1 <= days <= len(weights)
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        raise NotImplementedError


METHOD = "shipWithinDays"
TEST_CASES = [
    ("easy: one package", ([10], 1), 10),
    ("easy: one day carries everything", ([4, 2, 7, 3], 1), 16),
    ("easy: enough days for each package", ([4, 2, 7], 3), 7),
    ("medium: five days", ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15),
    ("medium: three days", ([3, 2, 2, 4, 1, 4], 3), 6),
    ("medium: four days", ([1, 2, 3, 1, 1], 4), 3),
    ("medium: equal package weights", ([5, 5, 5, 5, 5], 2), 15),
    ("medium: alternating heavy packages", ([9, 1, 9, 1, 9, 1], 3), 10),
    ("medium: heavy package in middle", ([1, 1, 1, 100, 1, 1, 1], 3), 100),
    ("hard: heavy ends need spare capacity", ([500, 1, 1, 1, 500], 2), 502),
    ("hard: heavy ends with three days", ([500, 1, 1, 1, 500], 3), 500),
    ("hard: middle package cannot be split", ([1, 1, 1, 100, 1, 1, 1], 2), 103),
    ("hard: irregular contiguous partitions", ([5, 3, 2, 7, 4, 6, 2, 8], 3), 16),
    ("hard: increasing weights", (list(range(1, 101)), 10), 540),
    ("hard: many maximum-weight packages", ([500] * 100, 7), 7500),
    ("hard: maximum input length", ([500] * 50_000, 49_999), 1000),
]
