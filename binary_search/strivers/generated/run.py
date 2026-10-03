"""Run the cases embedded in generated binary search exercises.

Usage: python run.py --list | python run.py 02 | python run.py --all
"""

import argparse
import copy
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def exercise_files():
    return sorted(
        path for path in ROOT.glob("*.py")
        if path.name not in {"run.py", "test_runner.py"}
    )


def select_exercises(files, query):
    if query.isdecimal():
        number = f"{int(query):02d}"
        return [path for path in files if path.stem.partition("_")[0] == number]
    return [
        path for path in files
        if path.stem == query or path.stem.partition("_")[2] == query
    ]


def run_exercise(path):
    """Print each case and return (passed, failed, pending)."""
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    passed = failed = pending = 0
    print(f"\n{path.stem}")
    for name, args, expected in module.TEST_CASES:
        try:
            actual = getattr(module.Solution(), module.METHOD)(*copy.deepcopy(args))
        except NotImplementedError:
            pending += 1
            print(f"  PENDING {name}")
        except Exception as error:
            failed += 1
            print(f"  ERROR {name}: {type(error).__name__}: {error}")
        else:
            if type(actual) is type(expected) and actual == expected:
                passed += 1
                print(f"  PASS {name}")
            else:
                failed += 1
                print(f"  FAIL {name}: expected {expected!r}, got {actual!r}")
    return passed, failed, pending


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exercise", nargs="?", help="question number or filename without .py")
    parser.add_argument("--list", action="store_true", help="list available exercises")
    parser.add_argument("--all", action="store_true", help="run every exercise")
    options = parser.parse_args()
    files = exercise_files()
    if options.list or (options.exercise is None and not options.all):
        for path in files:
            print(path.stem)
        return 0
    if options.all:
        selected = files
    else:
        selected = select_exercises(files, options.exercise)
        if not selected:
            parser.error(f"unknown exercise: {options.exercise}; use --list")
    totals = [0, 0, 0]
    for path in selected:
        for index, count in enumerate(run_exercise(path)):
            totals[index] += count
    print(f"\n{totals[0]} passed, {totals[1]} failed, {totals[2]} pending")
    return 0 if totals[1] == totals[2] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
