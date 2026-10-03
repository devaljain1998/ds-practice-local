"""04. Search Insert Position

Given a list of distinct integers ``nums`` sorted in ascending order and an
integer ``target``, return the index of ``target`` if it is present. Otherwise,
return the index where ``target`` should be inserted to keep ``nums`` sorted.

The insertion index can be anywhere from 0 through ``len(nums)``. An empty
list therefore always has insertion index 0.

Examples:
    Input: nums = [1, 3, 5, 6], target = 5
    Output: 2

    Input: nums = [1, 3, 5, 6], target = 2
    Output: 1

    Input: nums = [1, 3, 5, 6], target = 7
    Output: 4

Constraints:
    0 <= len(nums) <= 10_000
    -10^9 <= nums[i], target <= 10^9
    ``nums`` is strictly increasing.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        raise NotImplementedError


METHOD = "searchInsert"
TEST_CASES = [
    ("easy: present in middle", ([1, 3, 5, 6], 5), 2),
    ("easy: missing between values", ([1, 3, 5, 6], 2), 1),
    ("easy: insert after last", ([1, 3, 5, 6], 7), 4),
    ("easy: insert before first", ([1, 3, 5, 6], 0), 0),
    ("easy: empty list", ([], 2), 0),
    ("medium: singleton match", ([8], 8), 0),
    ("medium: singleton below", ([8], 7), 0),
    ("medium: singleton above", ([8], 9), 1),
    ("medium: first element match", ([-9, -3, 0, 4], -9), 0),
    ("medium: last element match", ([-9, -3, 0, 4], 4), 3),
    ("medium: insert zero among negatives and positives", ([-8, -2, 3, 9], 0), 2),
    ("medium: consecutive values missing below", ([3, 4, 5, 6], 2), 0),
    ("hard: large list missing near far end", (list(range(-10_000, 10_000, 2)), 9_753), 9_877),
    ("hard: large list exact match", (list(range(-10_000, 10_000, 2)), 9_998), 9_999),
    ("hard: extreme negative insertion", ([-10**9, 0, 10**9], -10**9 + 1), 1),
    ("hard: extreme positive insertion", ([-10**9, 0, 10**9 - 1], 10**9), 3),
]
