"""11. Single Element in a Sorted Array

You are given a nonempty integer array ``nums`` sorted in nondecreasing order.
Exactly one value occurs once; every other value occurs exactly twice. Return
the value that occurs once.

Your solution should run in O(log n) time and use O(1) extra space.

Examples:
    Input: nums = [1, 1, 2, 3, 3]
    Output: 2
    Explanation: 2 is the only value without a matching copy.

    Input: nums = [3, 3, 7, 7, 10, 11, 11]
    Output: 10
    Explanation: Every value except 10 occurs twice.

    Input: nums = [-4]
    Output: -4

Constraints:
    * 1 <= len(nums) <= 100_000; ``len(nums)`` is odd.
    * -1_000_000_000 <= nums[i] <= 1_000_000_000
    * ``nums`` is sorted in nondecreasing order.
    * Exactly one value occurs once and every other value occurs twice.
"""


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        raise NotImplementedError


METHOD = "singleNonDuplicate"
TEST_CASES = [
    ("easy_only_element", ([7],), 7),
    ("easy_first", ([1, 2, 2, 3, 3],), 1),
    ("easy_middle", ([1, 1, 2, 3, 3],), 2),
    ("easy_last", ([1, 1, 2, 2, 3],), 3),
    ("easy_three_elements_first", ([1, 2, 2],), 1),
    ("easy_three_elements_last", ([1, 1, 2],), 2),
    ("medium_near_end", ([3, 3, 7, 7, 10, 11, 11],), 10),
    ("medium_negative_unique", ([-9, -4, -4, -1, -1],), -9),
    ("medium_zero_unique", ([-5, -5, 0, 2, 2],), 0),
    ("medium_negative_and_positive_pairs", ([-10, -10, -2, -2, 4, 5, 5],), 4),
    ("medium_consecutive_values", ([0, 0, 1, 1, 2, 3, 3, 4, 4],), 2),
    ("medium_unique_left_of_midpoint", ([0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5],), 1),
    ("medium_unique_right_of_midpoint", ([0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 5],), 4),
    ("medium_minimum_integer", ([-1_000_000_000, 0, 0, 1_000_000_000, 1_000_000_000],), -1_000_000_000),
    ("medium_maximum_integer", ([-1_000_000_000, -1_000_000_000, 0, 0, 1_000_000_000],), 1_000_000_000),
    (
        "hard_large_unique_first",
        ([0] + [value for value in range(1, 50_000) for _ in (0, 1)],),
        0,
    ),
    (
        "hard_large_unique_middle",
        ([value for value in range(25_000) for _ in (0, 1)]
         + [25_000]
         + [value for value in range(25_001, 50_000) for _ in (0, 1)],),
        25_000,
    ),
    (
        "hard_large_unique_last",
        ([value for value in range(49_999) for _ in (0, 1)] + [49_999],),
        49_999,
    ),
]
