"""20. Painter's Partition

You are given ``boards`` in the order they must appear, where ``boards[i]``
is the length of board ``i``, and an integer ``k``. Assign every board to a
painter. A painter may paint only a contiguous group of boards, and a board
cannot be split between painters. You may use at most ``k`` painters, so some
painters may be idle when ``k`` exceeds the number of boards.

Each painter takes one unit of time per unit of board length. All painters
work simultaneously. Return the minimum time needed to finish every board.
Equivalently, minimize the largest sum of board lengths assigned to any one
painter.

Example 1:
    Input: boards = [10, 20, 30, 40], k = 2
    Output: 60
    Explanation: Assign [10, 20, 30] and [40]. Their workloads are 60 and
    40, so both painters finish after 60 time units. No contiguous split has
    a smaller maximum workload.

Example 2:
    Input: boards = [7, 2, 5, 10, 8], k = 2
    Output: 18
    Explanation: Assign [7, 2, 5] and [10, 8]. The workloads are 14 and 18.

Example 3:
    Input: boards = [10], k = 3
    Output: 10
    Explanation: Only one painter can paint the single board; the others
    may remain idle.

Constraints:
    1 <= len(boards) <= 100_000
    1 <= boards[i] <= 1_000_000_000
    1 <= k <= 1_000_000_000
"""


class Solution:
    def minTime(self, boards: list[int], k: int) -> int:
        raise NotImplementedError


METHOD = "minTime"
TEST_CASES = [
    ("easy: one board and one painter", ([7], 1), 7),
    ("easy: more painters than boards", ([10], 3), 10),
    ("easy: one painter paints everything", ([10, 20, 30, 40], 1), 100),
    ("easy: one board per painter", ([10, 20, 30, 40], 4), 40),
    ("easy: two painters sample", ([10, 20, 30, 40], 2), 60),
    ("easy: equal boards", ([5, 5, 5, 5, 5], 3), 10),
    ("medium: two boards and one painter", ([7, 11], 1), 18),
    ("medium: two boards and two painters", ([7, 11], 2), 11),
    ("medium: center board cannot be split", ([1, 100, 1], 2), 101),
    ("medium: largest board first", ([50, 1, 1, 1, 1], 2), 50),
    ("medium: largest board last", ([1, 1, 1, 1, 50], 2), 50),
    ("medium: irregular lengths", ([2, 34, 67, 90], 2), 103),
    ("medium: split after a short prefix", ([7, 2, 5, 10, 8], 2), 18),
    ("medium: equal boards require a group of three", ([5] * 7, 3), 15),
    ("medium: two painters with increasing lengths", ([1, 2, 3, 4, 5], 2), 9),
    ("medium: three painters with increasing lengths", ([1, 2, 3, 4, 5], 3), 6),
    ("medium: threshold requires three groups", ([9, 1, 1, 9], 2), 10),
    ("medium: many idle painters", ([3, 1, 4, 1, 5], 20), 5),
    ("hard: billion length boards need a wide result", ([1_000_000_000] * 3, 2), 2_000_000_000),
    ("hard: 100000 equal boards with three painters", ([1_000_000_000] * 100_000, 3), 33_334_000_000_000),
    ("hard: 100000 equal boards with one fewer painter", ([1_000_000_000] * 100_000, 99_999), 2_000_000_000),
    ("hard: 100000 unit boards split unevenly", ([1] * 100_000, 333), 301),
    ("hard: alternating billion and unit boards", ([1_000_000_000, 1] * 50_000, 50_000), 1_000_000_001),
    ("hard: 100000 increasing boards and two painters", (list(range(1, 100_001)), 2), 2_500_058_116),
]
