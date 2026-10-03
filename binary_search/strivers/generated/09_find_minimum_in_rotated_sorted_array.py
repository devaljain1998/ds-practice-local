"""09. Find Minimum in Rotated Sorted Array

An array of distinct integers was originally sorted in strictly increasing
order. It was then rotated at some pivot: for example, rotating
``[0, 1, 2, 4, 5, 6, 7]`` can produce ``[4, 5, 6, 7, 0, 1, 2]``.

Implement ``Solution.findMin(nums)`` to return the smallest element in the
rotated array. The array can also be in its original sorted order. Aim for
O(log n) time.

Example 1:
    Input: nums = [3, 4, 5, 1, 2]
    Output: 1
    Explanation: The original array [1, 2, 3, 4, 5] was rotated.

Example 2:
    Input: nums = [11, 13, 15, 17]
    Output: 11
    Explanation: The smallest value remains at the beginning.

Example 3:
    Input: nums = [2, 1]
    Output: 1

Constraints:
    1 <= len(nums) <= 5,000
    -5,000 <= nums[i] <= 5,000
    All values are distinct, and nums is a rotation of a strictly
    increasing array.
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        raise NotImplementedError


METHOD = "findMin"
TEST_CASES = [
    ("easy: one element", ([1],), 1),
    ("easy: two sorted elements", ([1, 2],), 1),
    ("easy: two rotated elements", ([2, 1],), 1),
    ("easy: three elements, minimum in middle", ([3, 1, 2],), 1),
    ("easy: already sorted", ([11, 13, 15, 17],), 11),
    ("medium: pivot in middle", ([3, 4, 5, 1, 2],), 1),
    ("medium: pivot later", ([4, 5, 6, 7, 0, 1, 2],), 0),
    ("medium: minimum at last index", ([2, 3, 4, 5, 1],), 1),
    ("medium: minimum at second index", ([5, 1, 2, 3, 4],), 1),
    ("medium: negative values", ([-1, 0, 2, -4, -2],), -4),
    ("medium: values across zero", ([0, 1, 2, -3, -2, -1],), -3),
    ("hard: extreme allowed values", ([4_999, 5_000, -5_000, -4_999],), -5_000),
    ("hard: large rotation", (list(range(-1_266, 2_500)) + list(range(-2_500, -1_266)),), -2_500),
    ("hard: large sorted array", (list(range(-2_500, 2_500)),), -2_500),
]
