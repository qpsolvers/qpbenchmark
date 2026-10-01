# SPDX-License-Identifier: Apache-2.0

"""Test set used in unit tests."""

import qpbenchmark

from .custom_problem import custom_problem


class CustomTestSet(qpbenchmark.TestSet):
    """Test set with two small problems."""

    @property
    def description(self) -> str:
        """Test set description."""
        return "Unit test test set"

    @property
    def title(self) -> str:
        """Report title."""
        return "Unit test test set"

    @property
    def sparse_only(self) -> bool:
        """Test set is not restricted to sparse solvers."""
        return False

    def __iter__(self):
        """Yield test-set problems one by one."""
        yield custom_problem(name="custom")
        yield custom_problem(name="custom_again")  # test only_problem
