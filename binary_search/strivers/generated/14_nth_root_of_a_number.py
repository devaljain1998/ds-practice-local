"""14. Find Nth Root of a Number

Given an integer ``n`` and a nonnegative integer ``m``, find an integer ``x``
such that ``x ** n == m``. Return ``x`` if it exists; otherwise return ``-1``.
Use the argument order ``NthRoot(n, m)``. The answer must be exact: rounding a
real-valued root is not enough.

Examples:
    Input: n = 3, m = 27
    Output: 3
    Explanation: 3 ** 3 = 27.

    Input: n = 4, m = 69
    Output: -1
    Explanation: 2 ** 4 = 16 and 3 ** 4 = 81, so no integer fourth root exists.

    Input: n = 5, m = 0
    Output: 0
    Explanation: 0 ** 5 = 0.

Constraints:
    1 <= n <= 60
    0 <= m <= 10 ** 18
"""


class Solution:
    def NthRoot(self, n: int, m: int) -> int:
        raise NotImplementedError


METHOD = "NthRoot"
TEST_CASES = [
    ("easy: zero cube", (3, 0), 0),
    ("easy: zero with largest exponent", (60, 0), 0),
    ("easy: one square", (2, 1), 1),
    ("easy: one with largest exponent", (60, 1), 1),
    ("easy: first root of eleven", (1, 11), 11),
    ("easy: first root at upper limit", (1, 10 ** 18), 10 ** 18),
    ("easy: exact small square", (2, 16), 4),
    ("easy: between small squares", (2, 15), -1),
    ("easy: exact cube", (3, 27), 3),
    ("medium: just below cube", (3, 26), -1),
    ("medium: just above cube", (3, 28), -1),
    ("medium: fourth root between powers", (4, 69), -1),
    ("medium: exact fifth power", (5, 243), 3),
    ("medium: exact eighth power", (8, 390625), 5),
    ("medium: close to eighth power", (8, 390626), -1),
    ("medium: exact twelfth power", (12, 531441), 3),
    ("hard: large exact square", (2, 999_999_937 ** 2), 999_999_937),
    ("hard: one above large square", (2, 999_999_937 ** 2 + 1), -1),
    ("hard: large exact cube", (3, 10 ** 18), 10 ** 6),
    ("hard: one below large cube", (3, 10 ** 18 - 1), -1),
    ("hard: large exact ninth power", (9, 10 ** 18), 100),
    ("hard: large exact eighteenth power", (18, 10 ** 18), 10),
    ("hard: large nonperfect fourth power", (4, 10 ** 18), -1),
    ("hard: large exponent exact power", (59, 2 ** 59), 2),
    ("hard: large exponent near power", (59, 2 ** 59 - 1), -1),
    ("hard: largest exponent with large input", (60, 10 ** 18), -1),
]
