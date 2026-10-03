"""13. Find Square Root of a Number

Given a nonnegative integer ``n``, return the greatest integer ``r`` such
that ``r * r <= n``. In other words, implement ``Solution.floorSqrt(n)`` and
return the square root rounded down to an integer. Return an exact integer;
floating-point approximations can round incorrectly for large inputs.

Examples:
    Input: n = 16
    Output: 4
    Explanation: 4 * 4 = 16.

    Input: n = 8
    Output: 2
    Explanation: 2 * 2 <= 8, but 3 * 3 > 8.

    Input: n = 0
    Output: 0

Constraints:
    0 <= n <= 10**18

Do not use a built-in square-root function to compute the answer.
"""


class Solution:
    def floorSqrt(self, n: int) -> int:
        raise NotImplementedError


METHOD = "floorSqrt"
TEST_CASES = [
    ("easy: zero", (0,), 0),
    ("easy: one", (1,), 1),
    ("easy: two", (2,), 1),
    ("easy: three", (3,), 1),
    ("easy: first nontrivial square", (4,), 2),
    ("easy: just before nine", (8,), 2),
    ("easy: nine", (9,), 3),
    ("medium: just before sixteen", (15,), 3),
    ("medium: sixteen", (16,), 4),
    ("medium: just after sixteen", (17,), 4),
    ("medium: just before twenty-five", (24,), 4),
    ("medium: twenty-five", (25,), 5),
    ("medium: just after twenty-five", (26,), 5),
    ("medium: two-digit floor boundary", (99,), 9),
    ("medium: three-digit square", (100,), 10),
    ("medium: one past three-digit square", (101,), 10),
    ("hard: before 46340 squared", (2_147_395_599,), 46_339),
    ("hard: 46340 squared", (2_147_395_600,), 46_340),
    ("hard: 32-bit signed maximum", (2_147_483_647,), 46_340),
    ("hard: before large square", (15_241_578_750_190_520,), 123_456_788),
    ("hard: large square", (15_241_578_750_190_521,), 123_456_789),
    ("hard: after large square", (15_241_578_750_190_522,), 123_456_789),
    ("hard: just below maximum", (999_999_999_999_999_999,), 999_999_999),
    ("hard: maximum perfect square", (1_000_000_000_000_000_000,), 1_000_000_000),
]
