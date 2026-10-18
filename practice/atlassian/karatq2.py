import unittest

# # Problem Statement: Grid Path Search & Constrained Pair Sum

# ### **Part 1: Constrained Grid Traversal**

# Given an $m \times n$ matrix `grid` filled with non-negative integers representing cell costs, you start at the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)`.

# **Movement Rules & Constraints:**
# 1. From cell `(r, c)`, you can move **Right** `(r, c + 1)`, **Down** `(r + 1, c)`, or **Diagonal Right-Down** `(r + 1, c + 1)`.
# 2. **Cost Calculation:** The cost to enter a cell is `grid[r][c]`.
# 3. **Hazard Rule:** You cannot visit two consecutive cells whose individual entry costs are both strictly greater than a given threshold `K`.
# 4. **Energy Constraint:** A Diagonal step adds an extra flat energy penalty `P` to the cost of that step in addition to the target cell's cost.

# Find the **minimum total cost** to travel from `(0, 0)` to `(m - 1, n - 1)`. If no valid path satisfies all constraints, return `-1`.

# ---

# ### **Part 2: Array Pairing under Bounds (Two Sum Variant)**

# Along with the grid, you are given an integer array `nums` and a target range `[lower_bound, upper_bound]`.

# Find the total count of **unique index pairs** `(i, j)` with `0 <= i < j < len(nums)` such that:
# 1. `lower_bound <= nums[i] + nums[j] <= upper_bound`
# 2. At least one of `nums[i]` or `nums[j]` is equal to the **minimum path cost** found in Part 1 (if Part 1 returns `-1`, no pair can satisfy this condition, so return `0`).

def solve_grid_and_pairs(
    grid: list[list[int]],
    K: int,
    P: int,
    nums: list[int],
    lower_bound: int,
    upper_bound: int,
) -> tuple[int, int]:
    """
    Solves Part 1 (Constrained Grid Traversal) and Part 2 (Bounded Two Sum Variant).
    
    Returns:
        tuple[int, int]: (min_path_cost, valid_pair_count)
    """
    # TODO: Implement your solution here
    pass


class TestGridAndPairs(unittest.TestCase):

    def test_case_1_standard_path_and_pair_count(self):
        grid = [
            [1, 3, 1],
            [2, 8, 2],
            [1, 5, 1]
        ]
        K = 4
        P = 2
        nums = [2, 4, 3, 5, 1]
        lower_bound = 5
        upper_bound = 8

        result = solve_grid_and_pairs(grid, K, P, nums, lower_bound, upper_bound)
        self.assertEqual(result, (4, 3))

    def test_case_2_unreachable_hazard_violation(self):
        grid = [
            [1, 5, 5],
            [5, 5, 5],
            [5, 5, 1]
        ]
        K = 3
        P = 1
        nums = [1, 2, 3, 4]
        lower_bound = 2
        upper_bound = 10

        result = solve_grid_and_pairs(grid, K, P, nums, lower_bound, upper_bound)
        self.assertEqual(result, (-1, 0))

    def test_case_3_diagonal_shortcut_with_penalty(self):
        grid = [
            [0, 10, 10],
            [10, 10, 10],
            [10, 10, 0]
        ]
        K = 100
        P = 5
        nums = [0, 5, 10, 15]
        lower_bound = 5
        upper_bound = 15

        result = solve_grid_and_pairs(grid, K, P, nums, lower_bound, upper_bound)
        self.assertEqual(result, (20, 0))

    def test_case_4_edge_case_single_cell_grid(self):
        grid = [
            [3]
        ]
        K = 2
        P = 10
        nums = [3, 0, 1, 2, 3]
        lower_bound = 3
        upper_bound = 6

        result = solve_grid_and_pairs(grid, K, P, nums, lower_bound, upper_bound)
        self.assertEqual(result, (3, 6))

    def test_case_5_large_values_and_multiple_pairs(self):
        grid = [
            [2, 1, 9, 3],
            [4, 2, 1, 6],
            [8, 5, 2, 2]
        ]
        K = 5
        P = 1
        nums = [5, 2, 5, 3, 5, 1]
        lower_bound = 6
        upper_bound = 8

        result = solve_grid_and_pairs(grid, K, P, nums, lower_bound, upper_bound)
        self.assertEqual(result, (8, 0))


if __name__ == "__main__":
    unittest.main()