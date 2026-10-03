# Binary search practice

These are the 20 questions in the Fundamentals, Logic Building, and On answers sections shown in the screenshots. Exercise filenames and their opening docstrings are numbered in the order to solve them: `01`–`03` are Fundamentals, `04`–`12` are Logic Building, and `13`–`20` are On answers. Each exercise has a LeetCode-style `class Solution`, one method to fill in, and named test cases. Unsolved methods raise `NotImplementedError` until you replace them with your solution.

From the repository root:

```bash
python3 binary_search/strivers/generated/run.py --list
python3 binary_search/strivers/generated/run.py 02
python3 binary_search/strivers/generated/run.py --all
```

You can also run `python3 run.py 02` from this directory. The runner accepts `02`, `2`, or the full filename without `.py`. A case is `PENDING` until its method is implemented, `PASS` when its result matches, and `FAIL` or `ERROR` otherwise. The runner exits with code 0 only when every selected case passes. It makes a fresh `Solution` and copies the input for each case.

Use the module docstring for the full problem statement, examples, and constraints. Each `TEST_CASES` list has easy, medium, and hard cases. Fill in only the method body. To add a case, append `(name, positional_arguments_tuple, expected_result)` to `TEST_CASES`.

The two search problems in rotated arrays differ: I has distinct values and returns an index; II allows duplicates and returns a boolean. Floor and ceil returns a two-element list, with `-1` for a missing side. Painter's Partition uses contiguous boards and at most `k` painters, with one time unit per board length.

To check the runner itself:

```bash
python3 -m unittest discover -s binary_search/strivers/generated -p test_runner.py
```
