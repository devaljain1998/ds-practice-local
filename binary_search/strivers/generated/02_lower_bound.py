"""02. Lower Bound

Given an integer array ``arr`` sorted in non-decreasing order and an integer
``x``, return the smallest index ``i`` such that ``arr[i] >= x``. If no such
index exists, return ``len(arr)``. Indices are zero-based. The answer for an
empty array is 0.

Example 1:
    Input: arr = [1, 2, 2, 4], x = 2
    Output: 1
    Explanation: Both indices 1 and 2 hold 2, so the first valid index is 1.

Example 2:
    Input: arr = [1, 2, 2, 4], x = 3
    Output: 3
    Explanation: 4 is the first value greater than or equal to 3.

Example 3:
    Input: arr = [1, 2, 2, 4], x = 5
    Output: 4
    Explanation: No element is at least 5, so return the array length.

Constraints:
    0 <= len(arr) <= 100,000
    -1,000,000,000 <= arr[i], x <= 1,000,000,000
    ``arr`` is sorted in non-decreasing order.
"""


class Solution:
    def lowerBound(self, arr: list[int], x: int) -> int:
        raise NotImplementedError


METHOD = "lowerBound"
_LARGE_SORTED = [-1] * 16_384 + [0] * 32_768 + [2] * 16_384
TEST_CASES = [
    ("easy - empty array", ([], 2), 0),
    ("easy - singleton equal", ([4], 4), 0),
    ("easy - singleton below target", ([4], 5), 1),
    ("easy - singleton above target", ([4], 3), 0),
    ("easy - target at first index", ([1, 3, 5, 7], 1), 0),
    ("easy - target at last index", ([1, 3, 5, 7], 7), 3),
    ("easy - target between values", ([1, 3, 5, 7], 4), 2),
    ("easy - target before all values", ([1, 3, 5, 7], -1), 0),
    ("easy - target after all values", ([1, 3, 5, 7], 8), 4),
    ("medium - first duplicate target", ([1, 2, 2, 2, 4, 4], 2), 1),
    ("medium - first value after duplicate block", ([1, 2, 2, 2, 4, 4], 3), 4),
    ("medium - duplicate maximum target", ([1, 2, 2, 2, 4, 4], 4), 4),
    ("medium - all values equal target", ([6] * 7, 6), 0),
    ("medium - all values below target", ([6] * 7, 7), 7),
    ("medium - all values above target", ([6] * 7, 5), 0),
    ("medium - negatives and zero", ([-9, -4, -4, -1, 0, 0, 5], -3), 3),
    ("medium - negative duplicate target", ([-9, -4, -4, -1, 0, 0, 5], -4), 1),
    (
        "medium - extreme allowed integers",
        ([-1_000_000_000, 0, 1_000_000_000], 1_000_000_000),
        2,
    ),
    ("hard - first index of long plateau", (_LARGE_SORTED, 0), 16_384),
    ("hard - gap after long plateau", (_LARGE_SORTED, 1), 49_152),
    ("hard - target beyond long array", (_LARGE_SORTED, 3), 65_536),
]
