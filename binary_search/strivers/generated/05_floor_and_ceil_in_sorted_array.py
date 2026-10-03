"""05. Floor and Ceil in a Sorted Array

Given an integer array ``arr`` sorted in non-decreasing order and an integer
``x``, return a two-element list ``[floor, ceil]``. The floor is the greatest
value in ``arr`` that is less than or equal to ``x``. The ceil is the smallest
value in ``arr`` that is greater than or equal to ``x``. Return ``-1`` for a
floor or ceil that does not exist. Return values, not array indices.

Example 1:
    Input: arr = [1, 2, 4, 6, 10], x = 5
    Output: [4, 6]
    Explanation: 4 is the greatest value below 5, and 6 is the least above 5.

Example 2:
    Input: arr = [1, 2, 2, 4], x = 2
    Output: [2, 2]
    Explanation: An exact match is both the floor and the ceil.

Example 3:
    Input: arr = [3, 7], x = 1
    Output: [-1, 3]
    Explanation: No array value is less than or equal to 1.

Constraints:
    0 <= len(arr) <= 100_000
    -1_000_000_000 <= arr[i], x <= 1_000_000_000
    arr is sorted in non-decreasing order and may contain duplicates.
"""


class Solution:
    def getFloorAndCeil(self, arr: list[int], x: int) -> list[int]:
        raise NotImplementedError


METHOD = "getFloorAndCeil"
TEST_CASES = [
    ("Easy: between values", ([1, 2, 4, 6, 10], 5), [4, 6]),
    ("Easy: exact match", ([1, 2, 4, 6, 10], 4), [4, 4]),
    ("Easy: below minimum", ([1, 2, 4, 6, 10], 0), [-1, 1]),
    ("Easy: above maximum", ([1, 2, 4, 6, 10], 11), [10, -1]),
    ("Easy: empty array", ([], 3), [-1, -1]),
    ("Easy: singleton exact", ([7], 7), [7, 7]),
    ("Easy: singleton below", ([7], 6), [-1, 7]),
    ("Easy: singleton above", ([7], 8), [7, -1]),
    ("Medium: duplicate exact values", ([1, 2, 2, 2, 4, 4, 7], 2), [2, 2]),
    ("Medium: between duplicate runs", ([1, 2, 2, 4, 4, 7], 3), [2, 4]),
    ("Medium: all values equal", ([5, 5, 5, 5], 5), [5, 5]),
    ("Medium: negative values", ([-10, -4, -1, 0, 3, 8], -2), [-4, -1]),
    ("Medium: zero between values", ([-5, -2, 3, 9], 0), [-2, 3]),
    ("Medium: exact negative one", ([-5, -1, 0, 3], -1), [-1, -1]),
    ("Hard: minimum allowed value", ([-1_000_000_000, 0, 1_000_000_000], -1_000_000_000), [-1_000_000_000, -1_000_000_000]),
    ("Hard: maximum allowed value", ([-1_000_000_000, 0, 1_000_000_000], 1_000_000_000), [1_000_000_000, 1_000_000_000]),
    ("Hard: 100000 spaced values", (list(range(0, 200_000, 2)), 123_457), [123_456, 123_458]),
    ("Hard: 100000 values in three runs", ([-50] * 33_333 + [0] * 33_334 + [50] * 33_333, 1), [0, 50]),
]
