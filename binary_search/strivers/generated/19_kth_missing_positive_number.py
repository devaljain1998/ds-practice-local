"""19. Kth Missing Positive Number

Given a strictly increasing array ``arr`` of positive integers and a positive
integer ``k``, return the k-th positive integer that does not appear in ``arr``.
Count missing numbers starting at 1. A number greater than every array element
can also be the answer. If ``arr`` is empty, the answer is ``k``.

Example 1:
    Input: arr = [2, 3, 4, 7, 11], k = 5
    Output: 9
    Explanation: The missing positive integers begin 1, 5, 6, 8, 9, 10, ...;
    the fifth is 9.

Example 2:
    Input: arr = [1, 2, 3, 4], k = 2
    Output: 6
    Explanation: The missing positive integers begin 5, 6, 7, ...;
    the second is 6.

Example 3:
    Input: arr = [], k = 3
    Output: 3
    Explanation: Every positive integer is missing.

Constraints:
    0 <= len(arr) <= 100_000
    1 <= arr[i] <= 1_000_000_000
    1 <= k <= 1_000_000_000
    arr is strictly increasing (so it has no duplicates).
"""


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        raise NotImplementedError


METHOD = "findKthPositive"
TEST_CASES = [
    ("easy: sample gaps within and after", ([2, 3, 4, 7, 11], 5), 9),
    ("easy: answer after a consecutive array", ([1, 2, 3, 4], 2), 6),
    ("easy: empty array", ([], 3), 3),
    ("easy: first missing integer", ([2, 3, 4], 1), 1),
    ("easy: singleton starting at one", ([1], 1), 2),
    ("easy: singleton with a gap before it", ([2], 2), 3),
    ("medium: last missing before first element", ([5, 6, 7], 4), 4),
    ("medium: first missing after consecutive suffix", ([5, 6, 7], 5), 8),
    ("medium: first missing inside a gap", ([1, 4, 5], 1), 2),
    ("medium: last missing inside a gap", ([1, 4, 5], 2), 3),
    ("medium: first missing after an internal gap", ([1, 4, 5], 3), 6),
    ("medium: several gaps before answer", ([2, 4, 7], 4), 6),
    ("medium: last missing before a large element", ([1_000, 2_000], 999), 999),
    ("medium: answer just after a large element", ([1_000, 2_000], 1_000), 1_001),
    ("hard: dense large array and huge k", (list(range(1, 100_001)), 1_000_000_000), 1_000_100_000),
    ("hard: many alternating gaps, last gap", (list(range(2, 100_001, 2)), 50_000), 99_999),
    ("hard: many alternating gaps, just beyond end", (list(range(2, 100_001, 2)), 50_001), 100_001),
    ("hard: billion-scale endpoint and k", ([1_000_000_000], 1_000_000_000), 1_000_000_001),
]
