"""15. Find the Smallest Divisor Given a Threshold

You are given an array of positive integers ``nums`` and a positive integer
``threshold``. Choose a positive integer divisor. Divide every element of
``nums`` by that divisor, round each result up to the nearest integer, and
add the rounded results.

Return the smallest divisor for which this sum is at most ``threshold``.
The order of the numbers does not matter.

Example 1:
    Input: nums = [1, 2, 5, 9], threshold = 6
    Output: 5
    Explanation: With divisor 5, the rounded results are [1, 1, 1, 2],
    whose sum is 5. Every smaller divisor produces a sum greater than 6.

Example 2:
    Input: nums = [44, 22, 33, 11, 1], threshold = 5
    Output: 44
    Explanation: Each of the five rounded results must be exactly 1, so
    the divisor must be at least the largest number, 44.

Example 3:
    Input: nums = [21212, 10101, 12121], threshold = 1000000
    Output: 1
    Explanation: Dividing by 1 already gives a sum below the threshold.

Constraints:
    1 <= len(nums) <= 50_000
    1 <= nums[i] <= 1_000_000
    len(nums) <= threshold <= 1_000_000
"""


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        raise NotImplementedError


METHOD = "smallestDivisor"
TEST_CASES = [
    ("easy: example 1", ([1, 2, 5, 9], 6), 5),
    ("medium: example 2 minimum threshold", ([44, 22, 33, 11, 1], 5), 44),
    ("easy: example 3 ample threshold", ([21212, 10101, 12121], 1_000_000), 1),
    ("easy: single one", ([1], 1), 1),
    ("medium: single maximum at minimum threshold", ([1_000_000], 1), 1_000_000),
    ("easy: single large number with ample threshold", ([999_983], 1_000_000), 1),
    ("easy: all ones at minimum threshold", ([1, 1, 1, 1], 4), 1),
    ("medium: divisor one exactly meets threshold", ([1, 2, 5, 9], 17), 1),
    ("medium: divisor one just exceeds threshold", ([1, 2, 5, 9], 16), 2),
    ("medium: unsorted input", ([9, 1, 5, 2], 6), 5),
    ("medium: minimum threshold equals maximum element", ([6, 7, 8], 3), 8),
    ("medium: one above minimum threshold", ([6, 7, 8], 4), 7),
    ("medium: equal elements at two quotients", ([7, 7, 7, 7], 8), 4),
    ("medium: equal elements below quotient boundary", ([7, 7, 7, 7], 7), 7),
    ("hard: large adjacent values", ([999_999, 1_000_000], 3), 999_999),
    ("hard: large equal values at two quotients", ([1_000_000] * 3, 6), 500_000),
    ("hard: ones beside large outlier", ([1, 1, 1_000_000], 4), 500_000),
    ("hard: many ones beside large outlier", ([1] * 999 + [1_000_000], 1_001), 500_000),
    ("hard: maximum length and minimum threshold", ([1_000_000] * 50_000, 50_000), 1_000_000),
    ("hard: maximum length at two quotients", ([1_000_000] * 50_000, 100_000), 500_000),
    ("hard: maximum length at twenty quotients", ([1_000_000] * 50_000, 1_000_000), 50_000),
]
