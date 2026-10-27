# SPDX-License-Identifier: Apache-2.0

"""Check problems of all test sets checked out in the `test_sets/` directory.

Each Python script at the root of a test-set directory is a test set, which we
check in a separate process with the ``qpbenchmark ... check`` command.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEST_SETS = ROOT / "test_sets"


def main() -> int:
    """Check all test sets.

    Returns:
        Exit code: zero if all test sets are well-formed, one otherwise.
    """
    failures = []
    for repo in sorted(TEST_SETS.iterdir()):
        if not repo.is_dir():
            continue
        scripts = sorted(repo.glob("*.py"))
        if not scripts:
            print(f"No test set in '{repo}': is the submodule checked out?")
            failures.append(repo.name)
            continue
        for script in scripts:
            print(f"Checking {script.relative_to(ROOT)}...", flush=True)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "qpbenchmark.benchmark",
                    "--test-set",
                    str(script),
                    "check",
                ],
            )
            if completed.returncode != 0:
                failures.append(str(script.relative_to(TEST_SETS)))
    if failures:
        print(f"Check failed for: {', '.join(failures)}")
        return 1
    print("All test sets are well-formed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
