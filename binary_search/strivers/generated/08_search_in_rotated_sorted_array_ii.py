"""08. Search in Rotated Sorted Array II

You are given an integer array ``nums`` that was sorted in nondecreasing order
and then rotated at an unknown pivot. For example, rotating
``[0, 0, 1, 2, 2, 3]`` can produce ``[2, 3, 0, 0, 1, 2]``. Duplicate values are
allowed. Given an integer ``target``, return ``True`` if it occurs in ``nums``
and ``False`` otherwise. Try to minimize the number of operations.

Example 1:
    Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 0
    Output: True

Example 2:
    Input: nums = [2, 5, 6, 0, 0, 1, 2], target = 3
    Output: False

Constraints:
    1 <= len(nums) <= 5000
    -10_000 <= nums[i], target <= 10_000
    ``nums`` was sorted in nondecreasing order before rotation.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        raise NotImplementedError


METHOD = "search"
_LARGE_SORTED = list(range(-2500, 2500))
_LARGE_ROTATED = _LARGE_SORTED[1750:] + _LARGE_SORTED[:1750]
TEST_CASES = [
    ("easy: sample match", ([2, 5, 6, 0, 0, 1, 2], 0), True),
    ("easy: sample absent", ([2, 5, 6, 0, 0, 1, 2], 3), False),
    ("easy: one element match", ([1], 1), True),
    ("easy: one element absent", ([1], 0), False),
    ("easy: unrotated first element", ([0, 2, 4, 6], 0), True),
    ("easy: unrotated last element", ([0, 2, 4, 6], 6), True),
    ("easy: unrotated gap", ([0, 2, 4, 6], 3), False),
    ("medium: pivot near front", ([6, 1, 2, 3, 4, 5], 1), True),
    ("medium: pivot near end", ([2, 3, 4, 5, 6, 1], 1), True),
    ("medium: ambiguous left half", ([1, 0, 1, 1, 1], 0), True),
    ("medium: ambiguous right half", ([1, 1, 1, 0, 1], 0), True),
    ("medium: duplicate target around pivot", ([2, 2, 3, 1, 2], 2), True),
    ("medium: duplicate endpoints target absent", ([2, 2, 3, 4, 2], 1), False),
    ("medium: all equal match", ([1, 1, 1, 1], 1), True),
    ("medium: all equal absent", ([1, 1, 1, 1], 2), False),
    ("medium: negative values and duplicates", ([0, 1, 1, -3, -1, 0], -1), True),
    ("medium: boundary values", ([10000, -10000, 0, 10000], -10000), True),
    ("hard: one distinct value hidden in 5000 duplicates", ([1] * 2499 + [0] + [1] * 2500, 0), True),
    ("hard: 5000 duplicate values with target absent", ([1] * 2500 + [2] * 2500, 0), False),
    ("hard: rotated 5000 distinct values target at pivot", (_LARGE_ROTATED, -2500), True),
    ("hard: rotated 5000 distinct values target absent", (_LARGE_ROTATED, 10000), False),
]
