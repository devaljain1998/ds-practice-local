"""03. Upper Bound

Given an integer array ``arr`` sorted in non-decreasing order and an integer
``x``, return the index of the first element strictly greater than ``x``.
If no such element exists, return ``len(arr)``. Indices are zero-based.

Example 1:
    Input: arr = [1, 2, 2, 4], x = 2
    Output: 3
    Explanation: Both 2s are equal to x; 4 is the first greater element.

Example 2:
    Input: arr = [-3, -1, 0, 0, 7], x = 1
    Output: 4
    Explanation: 7 is the first element greater than 1.

Example 3:
    Input: arr = [1, 3, 3], x = 3
    Output: 3
    Explanation: No element is greater than x, so return the array length.

Constraints:
    0 <= len(arr) <= 100_000
    -1_000_000_000 <= arr[i], x <= 1_000_000_000
    arr is sorted in non-decreasing order.
"""


class Solution:
    def upperBound(self, arr: list[int], x: int) -> int:
        raise NotImplementedError


METHOD = "upperBound"
TEST_CASES = [
    ("easy: empty array", ([], 2), 0),
    ("easy: singleton greater", ([5], 4), 0),
    ("easy: singleton equal", ([5], 5), 1),
    ("easy: singleton smaller", ([5], 6), 1),
    ("easy: before all", ([1, 2, 2, 4], 0), 0),
    ("easy: after all", ([1, 2, 2, 4], 5), 4),
    ("medium: past duplicates", ([1, 2, 2, 4], 2), 3),
    ("medium: absent between values", ([1, 2, 2, 4], 3), 3),
    ("medium: all values equal to target", ([2, 2, 2, 2], 2), 4),
    ("medium: all values greater than target", ([2, 2, 2], 1), 0),
    ("medium: negative values and zero", ([-5, -3, -3, 0, 2], -3), 3),
    ("medium: equal values at start", ([0, 0, 1, 2, 3], 0), 2),
    ("medium: equal values at end", ([-2, 0, 3, 3, 3], 3), 5),
    (
        "hard: extreme integer bounds",
        ([-1_000_000_000, -1_000_000_000, 1_000_000_000], -1_000_000_000),
        2,
    ),
    (
        "hard: large duplicate plateau",
        ([0] * 20_000 + [5] * 60_000 + [9] * 20_000, 5),
        80_000,
    ),
    ("hard: large distinct array near end", (list(range(100_000)), 99_998), 99_999),
]
