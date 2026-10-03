"""01. Search X in a Sorted Array

You are given an array ``nums`` of distinct integers sorted in ascending order
and an integer ``target``. Return the zero-based index of ``target`` in ``nums``.
If ``target`` does not occur, return ``-1``.

Your algorithm should run in O(log n) time.

Examples:
    Input: nums = [-5, -1, 0, 3, 9], target = 3
    Output: 3
    Explanation: ``nums[3]`` is 3.

    Input: nums = [1, 4, 7], target = 5
    Output: -1
    Explanation: 5 does not occur in the array.

Constraints:
    * 0 <= len(nums) <= 100_000
    * -1_000_000_000 <= nums[i], target <= 1_000_000_000
    * ``nums`` is strictly increasing.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


METHOD = "search"
TEST_CASES = [
    ("easy_empty", ([], 5), -1),
    ("easy_single_hit", ([7], 7), 0),
    ("easy_single_miss", ([7], 8), -1),
    ("easy_first", ([1, 4, 7], 1), 0),
    ("easy_last", ([1, 4, 7], 7), 2),
    ("medium_middle", ([-5, -1, 0, 3, 9], 3), 3),
    ("medium_missing_between", ([1, 4, 7], 5), -1),
    ("medium_below_minimum", ([-5, -1, 0, 3, 9], -6), -1),
    ("medium_above_maximum", ([-5, -1, 0, 3, 9], 10), -1),
    ("medium_negative_target", ([-9, -4, -1, 2, 6], -4), 1),
    ("medium_extreme_values", ([-1_000_000_000, 0, 1_000_000_000], 1_000_000_000), 2),
    ("hard_large_present", (list(range(-50_000, 50_001, 2)), 43_210), 46_605),
    ("hard_large_missing", (list(range(-50_000, 50_001, 2)), 43_211), -1),
]
