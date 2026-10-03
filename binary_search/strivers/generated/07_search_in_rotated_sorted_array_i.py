"""07. Search in Rotated Sorted Array I

You are given an integer array ``nums`` that was originally sorted in
strictly increasing order. It may have been rotated at an unknown pivot. For
example, ``[0, 1, 2, 4, 5, 6, 7]`` could become ``[4, 5, 6, 7, 0, 1, 2]``.
All values are distinct.

Given ``nums`` and an integer ``target``, return the index of ``target`` in
``nums``. Return ``-1`` if it is absent. Write ``Solution.search`` with
O(log n) time complexity.

Examples:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1

    Input: nums = [1], target = 1
    Output: 0

Constraints:
    1 <= len(nums) <= 5000
    -10**4 <= nums[i], target <= 10**4
    ``nums`` contains distinct integers and is a rotation of an ascending
    sorted array (a rotation by zero positions is allowed).
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        raise NotImplementedError


METHOD = "search"
TEST_CASES = [
    ("rotated match", ([4, 5, 6, 7, 0, 1, 2], 0), 4),
    ("rotated absent", ([4, 5, 6, 7, 0, 1, 2], 3), -1),
    ("two elements", ([3, 1], 1), 1),
    ("not rotated", ([1, 2, 3], 3), 2),
    ("one element", ([1], 1), 0),
    ("easy: singleton absent", ([1], 0), -1),
    ("easy: two elements ascending first", ([1, 3], 1), 0),
    ("easy: two elements rotated first", ([3, 1], 3), 0),
    ("easy: two elements absent", ([3, 1], 2), -1),
    ("medium: unrotated first", ([1, 3, 5, 7, 9], 1), 0),
    ("medium: unrotated middle", ([1, 3, 5, 7, 9], 5), 2),
    ("medium: unrotated absent", ([1, 3, 5, 7, 9], 6), -1),
    ("medium: pivot after first element", ([9, 1, 3, 5, 7], 9), 0),
    ("medium: pivot before last element", ([3, 5, 7, 9, 1], 1), 4),
    ("medium: left sorted half", ([5, 7, 9, 11, 1, 3], 9), 2),
    ("medium: right sorted half", ([5, 7, 9, 11, 1, 3], 3), 5),
    ("medium: negative values across pivot", ([0, 4, 8, -9, -4], -4), 4),
    ("medium: target below minimum", ([0, 4, 8, -9, -4], -10), -1),
    ("medium: target above maximum", ([0, 4, 8, -9, -4], 10), -1),
    (
        "hard: maximum length, target at pivot",
        (list(range(1379, 2500)) + list(range(-2500, 1379)), -2500),
        1121,
    ),
    (
        "hard: maximum length, target before pivot",
        (list(range(1379, 2500)) + list(range(-2500, 1379)), 2499),
        1120,
    ),
    (
        "hard: maximum length, target deep after pivot",
        (list(range(1379, 2500)) + list(range(-2500, 1379)), 0),
        3621,
    ),
    (
        "hard: maximum length, absent interior value",
        (list(range(1200, 5000, 2)) + list(range(-5000, 1200, 2)), 501),
        -1,
    ),
]
