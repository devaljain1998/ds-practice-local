"""10. Find Out How Many Times the Array Is Rotated

You are given a nonempty array ``arr`` that was sorted in strictly increasing
order and then rotated to the right some number of times. In one right rotation,
the final element moves to the front and every other element shifts one place
to the right.

Return the number of right rotations, as a value from ``0`` to ``len(arr) - 1``.
Rotating by the array's full length is equivalent to zero rotations. Because
all values are distinct, the answer is also the index of the minimum element.

Example 1:
    Input: arr = [3, 4, 5, 1, 2]
    Output: 3
    Explanation: [1, 2, 3, 4, 5] was rotated right three times.

Example 2:
    Input: arr = [1, 2, 3, 4]
    Output: 0
    Explanation: The array is already in increasing order.

Example 3:
    Input: arr = [9, -5, 0, 4]
    Output: 1
    Explanation: The minimum is at index 1.

Constraints:
    1 <= len(arr) <= 100_000
    -1_000_000_000 <= arr[i] <= 1_000_000_000
    All elements of arr are distinct.
    arr is a right rotation of a strictly increasing array.
"""


class Solution:
    def findKRotation(self, arr: list[int]) -> int:
        raise NotImplementedError


METHOD = "findKRotation"
TEST_CASES = [
    ("easy: one element", ([7],), 0),
    ("easy: two elements unrotated", ([1, 2],), 0),
    ("easy: two elements rotated", ([2, 1],), 1),
    ("easy: three elements unrotated", ([1, 2, 3],), 0),
    ("easy: rotate three elements once", ([3, 1, 2],), 1),
    ("easy: rotate three elements twice", ([2, 3, 1],), 2),
    ("medium: three rotations", ([3, 4, 5, 1, 2],), 3),
    ("medium: four rotations", ([4, 5, 6, 7, 0, 1, 2],), 4),
    ("medium: minimum near front", ([9, -5, 0, 4],), 1),
    ("medium: minimum near end", ([0, 4, 8, 12, -7],), 4),
    ("medium: all negative values", ([-3, -1, -10, -7, -5],), 2),
    ("medium: negative and positive values", ([-3, -1, 2, 5, -9, -6],), 4),
    ("hard: extreme integer values", ([1_000_000_000, -1_000_000_000, -2, 0, 8],), 1),
    ("hard: large array with deep pivot", (
        list(range(100_000 - 37_219, 100_000)) + list(range(100_000 - 37_219)),
    ), 37_219),
]
