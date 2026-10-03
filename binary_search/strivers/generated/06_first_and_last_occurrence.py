"""06. Find First and Last Position of Element in Sorted Array.

Given a list of integers ``nums`` sorted in non-decreasing order and an
integer ``target``, return the starting and ending indices of ``target``.
If ``target`` is absent, return ``[-1, -1]``. Indices are zero-based.

Your algorithm must run in O(log n) time.

Examples:
    Input: nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: [3, 4]

    Input: nums = [5, 7, 7, 8, 8, 10], target = 6
    Output: [-1, -1]

    Input: nums = [], target = 0
    Output: [-1, -1]

Constraints:
    0 <= len(nums) <= 100_000
    -1_000_000_000 <= nums[i], target <= 1_000_000_000
    ``nums`` is sorted in non-decreasing order.
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        raise NotImplementedError


METHOD = "searchRange"
TEST_CASES = [
    ("easy: empty array", ([], 2), [-1, -1]),
    ("easy: one matching element", ([2], 2), [0, 0]),
    ("easy: one nonmatching element", ([2], 3), [-1, -1]),
    ("easy: both elements match", ([2, 2], 2), [0, 1]),
    ("easy: first of two", ([1, 3], 1), [0, 0]),
    ("easy: last of two", ([1, 3], 3), [1, 1]),
    ("medium: repeated middle value", ([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    ("medium: target missing between values", ([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    ("medium: target below all values", ([0, 1, 1, 3], -1), [-1, -1]),
    ("medium: target above all values", ([0, 1, 1, 3], 4), [-1, -1]),
    ("medium: every element matches", ([2, 2, 2, 2, 2], 2), [0, 4]),
    ("medium: repeated first value", ([1, 1, 1, 2, 3], 1), [0, 2]),
    ("medium: repeated last value", ([1, 2, 3, 3, 3], 3), [2, 4]),
    ("medium: negative values", ([-9, -9, -4, -4, -4, 0, 7], -4), [2, 4]),
    ("hard: extreme integer boundaries", ([-1_000_000_000, -1_000_000_000, 0, 1_000_000_000], -1_000_000_000), [0, 1]),
    ("hard: 100,000 elements with central plateau", ([-1] * 20_000 + [0] * 60_000 + [1] * 20_000, 0), [20_000, 79_999]),
    ("hard: large unique array near end", (list(range(20_001)), 19_999), [19_999, 19_999]),
]
