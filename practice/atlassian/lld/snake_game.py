"""Atlassian code design / LLD practice: Snake Game

Interviewer:
    Let's build the logic behind the classic Snake game. You do not need a UI,
    a timer, or keyboard handling. Design the objects and implement an in-memory
    game that advances one cell whenever the caller supplies a direction.

    The snake begins with three segments. It can travel up, down, left, or
    right, and gains one segment on its fifth move, tenth move, and so on.
    The game finishes if the head runs into the snake's body.

    Start with these operations (Python names are used below):
        move_snake(direction) -> None
        is_game_over() -> bool

    Talk me through any ambiguous rules before you code. Explain your class
    responsibilities, the cost of a move, and how you would test your design.
    You may introduce supporting classes; the tests only use the public API.

Agreed clarifications for this exercise:
    1. SnakeGame(rows, cols) creates a rectangular board. Dimensions must be
       integers (excluding bool), rows >= 1 and cols >= 3. Otherwise raise
       ValueError. There is no food in the initial version.
    2. Coordinates are (row, column), indexed from zero. The initial body,
       ordered from head to tail, is ((0, 2), (0, 1), (0, 0)).
    3. Directions are exactly "UP", "DOWN", "LEFT", and "RIGHT". UP decreases
       the row; RIGHT increases the column. A move beyond an edge wraps to the
       opposite edge. Crossing an edge alone does not end the game.
    4. Every valid move while alive attempts one step. On a successful move
       the head advances, and the tail leaves its cell unless this is a growth
       move. Growth happens on moves 5, 10, 15, ...; never on move zero.
    5. Entering the current tail cell is legal when the tail leaves during that
       same move. It is a collision on a growth move, when the tail stays.
       Entering any other occupied cell ends the game. Do not ignore a reverse
       direction: moving into the neck is a collision.
    6. A collision sets game over but preserves the last valid body. Once the
       game is over, move_snake is a no-op, including for invalid directions.
    7. While alive, an unsupported direction raises ValueError and changes
       neither the body, the growth schedule, nor the game-over state.
    8. Add get_body() -> tuple[tuple[int, int], ...] for deterministic testing.
       It returns an immutable snapshot from head to tail; later moves must
       not change an earlier snapshot. Each game owns independent state.

Example on a 4 x 8 board:
    Initial:       ((0, 2), (0, 1), (0, 0))
    RIGHT:         ((0, 3), (0, 2), (0, 1))
    UP (wraps):    ((3, 3), (0, 3), (0, 2))
    LEFT:          ((3, 2), (3, 3), (0, 3))
    DOWN:          ((0, 2), (3, 2), (3, 3))
    RIGHT (grows): ((0, 3), (0, 2), (3, 2), (3, 3))
    The game is still running after all five moves.

Design expectations:
    Aim for O(1) average time per move and O(snake length) storage, without
    allocating the entire board. Reading a body snapshot may take O(length).
    Keep movement, growth, and collision behavior easy to reason about and
    adapt. Prefer a simple design over adding patterns without a clear need.

Interviewer follow-ups (discussion only; the tests cover the version above):
    - Can we make hitting a wall end the game instead of wrapping?
    - Replace periodic growth with food at randomly selected unoccupied cells.
      How would you test this deterministically and handle a full board?
    - How would you make simultaneous move calls safe? What must be atomic?

Research notes:
    This is a paraphrased practice prompt based on candidate interview reports,
    not an official Atlassian question or a verbatim interviewer transcript.
    Starting length, periodic growth, and self-collision are reported here:
    https://leetcode.com/discuss/post/6807250/atlassian-software-engineer-2-may-2025-3-ayr9/
    Wrapping, unit tests, and concurrent-input follow-ups are reported here:
    https://leetcode.com/discuss/post/2495755/Atlassian-or-SDE-2-(P4)-or-Bengaluru-or-Aug-2022-Offer/
    Food-based growth is a reported follow-up here:
    https://www.glassdoor.co.in/Interview/Game-of-Snakes-Remember-the-old-phone-game-of-snake-The-snake-can-move-up-down-left-or-right-in-a-2Dimensional-board-of-QTN_8493987.htm
    Exact initialization, rectangular dimensions, tail timing, validation,
    snapshot API, and post-collision behavior are explicit practice choices.

Run: python3 practice/atlassian/lld/snake_game.py
    Implement SnakeGame below. Unimplemented tests are reported as PENDING
    (unittest skips), not passes. Assertions and other errors fail normally.
"""

from enum import Enum
import unittest

class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    def get_movement(self, dir: Direction) -> tuple[int, int]:
        dir_mp = {
            self.UP: (0, 1),
            self.DOWN: (0, -1),
            self.RIGHT: (1, 0),
            self.LEFT: (-1, 0)
        }

        return dir_mp[dir]

class Snake:




class SnakeGame:
    """Implement the public contract above; choose your own internal design."""

    def __init__(self, rows: int, cols: int):
        raise NotImplementedError("Implement SnakeGame.__init__")

    def move_snake(self, direction: str) -> None:
        raise NotImplementedError("Implement SnakeGame.move_snake")

    def is_game_over(self) -> bool:
        raise NotImplementedError("Implement SnakeGame.is_game_over")

    def get_body(self) -> tuple[tuple[int, int], ...]:
        raise NotImplementedError("Implement SnakeGame.get_body")


class TestSnakeGame(unittest.TestCase):
    def assert_state(self, game, body, *, game_over=False):
        self.assertEqual(game.get_body(), body)
        self.assertIs(game.is_game_over(), game_over)
        self.assertIsInstance(game.get_body(), tuple)
        for cell in game.get_body():
            self.assertIsInstance(cell, tuple)

    def move_all(self, game, directions):
        for step, direction in enumerate(directions, start=1):
            with self.subTest(step=step, direction=direction):
                self.assertIsNone(game.move_snake(direction))

    def test_initial_body_and_game_status(self):
        self.assert_state(SnakeGame(4, 8), ((0, 2), (0, 1), (0, 0)))

    def test_right_moves_head_and_removes_tail(self):
        game = SnakeGame(4, 8)
        self.assertIsNone(game.move_snake("RIGHT"))
        self.assert_state(game, ((0, 3), (0, 2), (0, 1)))

    def test_down_increases_row(self):
        game = SnakeGame(4, 8)
        game.move_snake("DOWN")
        self.assert_state(game, ((1, 2), (0, 2), (0, 1)))

    def test_turns_and_fifth_move_match_prompt_example(self):
        game = SnakeGame(4, 8)
        steps = (
            ("RIGHT", ((0, 3), (0, 2), (0, 1))),
            ("UP", ((3, 3), (0, 3), (0, 2))),
            ("LEFT", ((3, 2), (3, 3), (0, 3))),
            ("DOWN", ((0, 2), (3, 2), (3, 3))),
            ("RIGHT", ((0, 3), (0, 2), (3, 2), (3, 3))),
        )
        for step, (direction, expected) in enumerate(steps, start=1):
            with self.subTest(step=step, direction=direction):
                self.assertIsNone(game.move_snake(direction))
                self.assert_state(game, expected)

    def test_up_wraps_using_row_count(self):
        game = SnakeGame(3, 8)
        game.move_snake("UP")
        self.assert_state(game, ((2, 2), (0, 2), (0, 1)))

    def test_down_wraps_using_row_count(self):
        game = SnakeGame(3, 8)
        self.move_all(game, ("DOWN", "DOWN", "DOWN"))
        self.assert_state(game, ((0, 2), (2, 2), (1, 2)))

    def test_right_wraps_using_column_count(self):
        game = SnakeGame(8, 4)
        self.move_all(game, ("RIGHT", "RIGHT"))
        self.assert_state(game, ((0, 0), (0, 3), (0, 2)))

    def test_left_wraps_using_column_count(self):
        game = SnakeGame(4, 7)
        self.move_all(game, ("DOWN", "LEFT", "LEFT", "LEFT"))
        self.assert_state(game, ((1, 6), (1, 0), (1, 1)))

    def test_growth_occurs_on_every_fifth_move_only(self):
        game = SnakeGame(4, 30)
        for move in range(1, 17):
            with self.subTest(move=move):
                game.move_snake("RIGHT")
                length = 3 + move // 5
                expected = tuple((0, col) for col in range(2 + move, 2 + move - length, -1))
                self.assert_state(game, expected)

    def test_growth_keeps_old_tail_then_normal_move_removes_it(self):
        game = SnakeGame(4, 20)
        self.move_all(game, ("RIGHT",) * 4)
        self.assert_state(game, ((0, 6), (0, 5), (0, 4)))
        game.move_snake("RIGHT")
        self.assert_state(game, ((0, 7), (0, 6), (0, 5), (0, 4)))
        game.move_snake("RIGHT")
        self.assert_state(game, ((0, 8), (0, 7), (0, 6), (0, 5)))

    def test_reverse_direction_hits_neck_and_preserves_body(self):
        game = SnakeGame(4, 8)
        self.assertIsNone(game.move_snake("LEFT"))
        self.assert_state(game, ((0, 2), (0, 1), (0, 0)), game_over=True)

    def test_collision_with_body_beyond_neck(self):
        game = SnakeGame(5, 30)
        self.move_all(game, ("RIGHT",) * 10 + ("DOWN", "LEFT"))
        before = ((1, 11), (1, 12), (0, 12), (0, 11), (0, 10))
        self.assert_state(game, before)
        game.move_snake("UP")
        self.assert_state(game, before, game_over=True)

    def test_entering_departing_tail_is_legal(self):
        game = SnakeGame(10, 10)
        self.move_all(game, ("RIGHT",) * 4 + ("DOWN", "LEFT"))
        self.assert_state(game, ((1, 5), (1, 6), (0, 6), (0, 5)))
        game.move_snake("UP")  # Move 7: the tail at (0, 5) leaves.
        self.assert_state(game, ((0, 5), (1, 5), (1, 6), (0, 6)))

    def test_entering_tail_on_growth_move_is_collision(self):
        game = SnakeGame(10, 10)
        self.move_all(game, ("RIGHT",) * 4 + ("DOWN", "LEFT", "UP", "RIGHT", "DOWN"))
        before = ((1, 6), (0, 6), (0, 5), (1, 5))
        self.assert_state(game, before)
        game.move_snake("LEFT")  # Move 10: the tail at (1, 5) stays.
        self.assert_state(game, before, game_over=True)

    def test_single_row_full_board_tail_moves_until_growth(self):
        game = SnakeGame(1, 3)
        expected_bodies = (
            ((0, 0), (0, 2), (0, 1)),
            ((0, 1), (0, 0), (0, 2)),
            ((0, 2), (0, 1), (0, 0)),
            ((0, 0), (0, 2), (0, 1)),
        )
        for move, expected in enumerate(expected_bodies, start=1):
            with self.subTest(move=move):
                game.move_snake("RIGHT")
                self.assert_state(game, expected)
        game.move_snake("RIGHT")
        self.assert_state(game, expected_bodies[-1], game_over=True)

    def test_wrapping_into_occupied_head_is_collision(self):
        game = SnakeGame(1, 8)
        game.move_snake("UP")
        self.assert_state(game, ((0, 2), (0, 1), (0, 0)), game_over=True)

    def test_old_cells_are_reusable_after_multiple_wraps(self):
        game = SnakeGame(2, 6)
        for move in range(1, 16):
            with self.subTest(move=move):
                game.move_snake("RIGHT")
                length = 3 + move // 5
                expected = tuple((0, (2 + move - offset) % 6) for offset in range(length))
                self.assert_state(game, expected)
        game.move_snake("RIGHT")  # Full board, but the tail leaves on move 16.
        self.assert_state(game, ((0, 0), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1)))

    def test_calls_after_game_over_are_no_ops(self):
        game = SnakeGame(4, 8)
        game.move_snake("LEFT")
        for direction in ("RIGHT", "DOWN", "UP", "LEFT", "bad", None):
            with self.subTest(direction=direction):
                self.assertIsNone(game.move_snake(direction))
                self.assert_state(game, ((0, 2), (0, 1), (0, 0)), game_over=True)

    def test_invalid_directions_do_not_change_state_or_growth_schedule(self):
        game = SnakeGame(4, 20)
        self.move_all(game, ("RIGHT",) * 4)
        for direction in ("", "right", "DIAGONAL", "R", None, 1, [], {}):
            with self.subTest(direction=direction):
                with self.assertRaises(ValueError):
                    game.move_snake(direction)
                self.assert_state(game, ((0, 6), (0, 5), (0, 4)))
        game.move_snake("RIGHT")
        self.assert_state(game, ((0, 7), (0, 6), (0, 5), (0, 4)))
        game.move_snake("RIGHT")
        self.assert_state(game, ((0, 8), (0, 7), (0, 6), (0, 5)))

    def test_invalid_board_dimensions(self):
        dimensions = (
            (0, 8), (-1, 8), (4, 0), (4, -1), (4, 1), (4, 2),
            (1.5, 8), (4, 8.5), (True, 8), (4, True), ("4", 8), (4, None),
        )
        for rows, cols in dimensions:
            with self.subTest(rows=rows, cols=cols):
                with self.assertRaises(ValueError):
                    SnakeGame(rows, cols)

    def test_body_snapshot_does_not_change_after_a_move(self):
        game = SnakeGame(4, 8)
        snapshot = game.get_body()
        game.move_snake("RIGHT")
        self.assertEqual(snapshot, ((0, 2), (0, 1), (0, 0)))
        self.assert_state(game, ((0, 3), (0, 2), (0, 1)))

    def test_status_and_snapshot_queries_do_not_advance_game(self):
        game = SnakeGame(4, 20)
        for _ in range(10):
            self.assert_state(game, ((0, 2), (0, 1), (0, 0)))
        self.move_all(game, ("RIGHT",) * 4)
        self.assert_state(game, ((0, 6), (0, 5), (0, 4)))

    def test_games_have_independent_bodies_status_and_growth_counters(self):
        first, second = SnakeGame(4, 20), SnakeGame(4, 20)
        self.move_all(first, ("RIGHT",) * 5)
        self.assert_state(first, ((0, 7), (0, 6), (0, 5), (0, 4)))
        self.assert_state(second, ((0, 2), (0, 1), (0, 0)))
        second.move_snake("LEFT")
        self.assert_state(second, ((0, 2), (0, 1), (0, 0)), game_over=True)
        first.move_snake("RIGHT")
        self.assert_state(first, ((0, 8), (0, 7), (0, 6), (0, 5)))

    def test_long_sequence_keeps_complete_ordered_body(self):
        game = SnakeGame(4, 2048)
        self.move_all(game, ("RIGHT",) * 1000)
        expected = tuple((0, col) for col in range(1002, 799, -1))
        self.assertEqual(len(expected), 203)
        self.assert_state(game, expected)


class _PracticeTestResult(unittest.TextTestResult):
    """Distinguish an unfinished exercise from an incorrect implementation."""

    def addError(self, test, err):
        if isinstance(err[1], NotImplementedError):
            self.addSkip(test, f"PENDING: {err[1]}")
        else:
            super().addError(test, err)

    def addSubTest(self, test, subtest, err):
        if err is not None and isinstance(err[1], NotImplementedError):
            self.addSkip(subtest, f"PENDING: {err[1]}")
        else:
            super().addSubTest(test, subtest, err)


if __name__ == "__main__":
    print("SnakeGame practice: PENDING means unimplemented, not passed.", flush=True)
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, resultclass=_PracticeTestResult))
