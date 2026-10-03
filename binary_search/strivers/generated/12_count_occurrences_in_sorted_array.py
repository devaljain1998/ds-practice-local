"""12. Count Occurrences of a Number in a Sorted Array.

Given an integer array ``arr`` sorted in non-decreasing order and an integer
``target``, return the number of times ``target`` appears in ``arr``. Return
``0`` if it does not appear. Repeated values are allowed.

Design an algorithm that runs in O(log n) time.

Examples:
    Input: arr = [1, 2, 2, 2, 3], target = 2
    Output: 3
    Explanation: The value 2 occurs at indices 1, 2, and 3.

    Input: arr = [1, 2, 2, 2, 3], target = 4
    Output: 0

    Input: arr = [-3, -3, -3, -1], target = -3
    Output: 3

Constraints:
    0 <= len(arr) <= 100_000
    -1_000_000_000 <= arr[i], target <= 1_000_000_000
    ``arr`` is sorted in non-decreasing order.
"""


class Solution:
    def countOccurrences(self, arr: list[int], target: int) -> int:
        raise NotImplementedError


METHOD = "countOccurrences"
TEST_CASES = [
    ("easy: empty array", ([], 2), 0),
    ("easy: one matching element", ([2], 2), 1),
    ("easy: one nonmatching element", ([2], 3), 0),
    ("easy: both elements match", ([2, 2], 2), 2),
    ("easy: first of two distinct elements", ([1, 3], 1), 1),
    ("easy: last of two distinct elements", ([1, 3], 3), 1),
    ("medium: repeated middle value", ([1, 2, 2, 2, 3], 2), 3),
    ("medium: target missing between values", ([1, 2, 2, 2, 4], 3), 0),
    ("medium: target below all values", ([0, 1, 1, 3], -1), 0),
    ("medium: target above all values", ([0, 1, 1, 3], 4), 0),
    ("medium: every element matches", ([2, 2, 2, 2, 2], 2), 5),
    ("medium: repeated first value", ([1, 1, 1, 2, 3], 1), 3),
    ("medium: repeated last value", ([1, 2, 3, 3, 3], 3), 3),
    ("medium: negative values and zero", ([-9, -9, -4, -4, -4, 0, 7], -4), 3),
    ("medium: only zero occurs", ([-2, -1, 0, 0, 0, 1], 0), 3),
    ("hard: extreme integer boundaries", ([-1_000_000_000, -1_000_000_000, 0, 1_000_000_000], -1_000_000_000), 2),
    ("hard: 100,000 elements with central plateau", ([-1] * 20_000 + [0] * 60_000 + [1] * 20_000, 0), 60_000),
    ("hard: 100,000 matching elements", ([7] * 100_000, 7), 100_000),
    ("hard: large unique array near end", (list(range(100_000)), 99_998), 1),
    ("hard: absent from large unique array", (list(range(0, 100_000, 2)), 99_999), 0),
]
