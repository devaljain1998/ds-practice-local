"""Tests for the exercise runner itself (not for unfinished solutions)."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from run import run_exercise, select_exercises


class RunnerTests(unittest.TestCase):
    def test_select_by_number_or_name(self):
        files = [Path("01_search_x_in_sorted_array.py"), Path("02_lower_bound.py")]
        self.assertEqual(select_exercises(files, "02"), [files[1]])
        self.assertEqual(select_exercises(files, "2"), [files[1]])
        self.assertEqual(select_exercises(files, "02_lower_bound"), [files[1]])
        self.assertEqual(select_exercises(files, "lower_bound"), [files[1]])
        self.assertEqual(select_exercises(files, "03"), [])

    def run_source(self, source):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.py"
            path.write_text(source)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = run_exercise(path)
            return result, output.getvalue()

    def test_pass_and_fresh_inputs(self):
        result, output = self.run_source('''
class Solution:
    def solve(self, values):
        return values.pop()
METHOD = "solve"
TEST_CASES = [("first", ([1],), 1), ("second", ([1],), 1)]
''')
        self.assertEqual(result, (2, 0, 0))
        self.assertIn("PASS first", output)

    def test_pending_answer_is_reported(self):
        result, output = self.run_source('''
class Solution:
    def solve(self, value):
        raise NotImplementedError
METHOD = "solve"
TEST_CASES = [("todo", (3,), 3)]
''')
        self.assertEqual(result, (0, 0, 1))
        self.assertIn("PENDING todo", output)

    def test_wrong_answer_is_reported(self):
        result, output = self.run_source('''
class Solution:
    def solve(self, value):
        return value + 1
METHOD = "solve"
TEST_CASES = [("wrong", (3,), 3)]
''')
        self.assertEqual(result, (0, 1, 0))
        self.assertIn("FAIL wrong", output)


if __name__ == "__main__":
    unittest.main()
