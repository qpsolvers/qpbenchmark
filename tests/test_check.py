# SPDX-License-Identifier: Apache-2.0

"""Unit tests for problem checks."""

import unittest

import numpy as np
import scipy.sparse as spa

from qpbenchmark.check import check_problem, check_test_set
from qpbenchmark.problem import Problem

from .custom_test_set import CustomTestSet


def make_problem(**kwargs) -> Problem:
    """Build a well-formed problem with all constraints, then override.

    Args:
        kwargs: Problem fields to override.

    Returns:
        Problem with two variables.
    """
    fields = {
        "P": np.eye(2),
        "q": np.ones(2),
        "G": np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]),
        "h": np.array([1.0, np.inf, 2.0]),
        "A": np.array([[1.0, -1.0]]),
        "b": np.array([0.0]),
        "lb": np.array([-np.inf, 0.0]),
        "ub": np.array([1.0, np.inf]),
        "name": "TEST",
    }
    fields.update(kwargs)
    return Problem(**fields)


class TestCheck(unittest.TestCase):
    """Test fixture for problem checks."""

    def test_well_formed(self):
        """Problems with disabled inequalities are well-formed."""
        self.assertEqual(check_problem(make_problem()), [])

    def test_unconstrained(self):
        """Unconstrained problems are well-formed."""
        problem = make_problem(
            G=None, h=None, A=None, b=None, lb=None, ub=None
        )
        self.assertEqual(check_problem(problem), [])

    def test_sparse(self):
        """Sparse matrices are checked as well."""
        self.assertEqual(
            check_problem(make_problem(P=spa.csc_matrix(np.eye(2)))), []
        )
        P = spa.csc_matrix(np.array([[1.0, 0.0], [0.0, np.inf]]))
        self.assertEqual(len(check_problem(make_problem(P=P))), 1)

    def test_singular_cost(self):
        """Cost matrices need not be positive definite."""
        P = np.array([[1.0, 0.0], [0.0, 0.0]])
        self.assertEqual(check_problem(make_problem(P=P)), [])

    def test_dimensions(self):
        """Inconsistent dimensions are reported."""
        self.assertEqual(len(check_problem(make_problem(P=np.eye(3)))), 1)
        self.assertEqual(len(check_problem(make_problem(h=np.ones(2)))), 1)
        self.assertEqual(
            len(check_problem(make_problem(A=np.ones((1, 3))))), 1
        )
        self.assertEqual(len(check_problem(make_problem(b=np.ones(2)))), 1)
        self.assertEqual(len(check_problem(make_problem(lb=np.zeros(3)))), 1)
        self.assertEqual(len(check_problem(make_problem(ub=np.ones(1)))), 1)

    def test_matrix_values(self):
        """Infinite and NaN values in matrices and equalities are reported."""
        P = np.array([[1.0, np.nan], [np.nan, 1.0]])
        self.assertEqual(len(check_problem(make_problem(P=P))), 1)
        q = np.array([1.0, np.inf])
        self.assertEqual(len(check_problem(make_problem(q=q))), 1)
        G = np.array([[1.0, 0.0], [0.0, -np.inf], [1.0, 1.0]])
        self.assertEqual(len(check_problem(make_problem(G=G))), 1)
        b = np.array([np.inf])
        self.assertEqual(len(check_problem(make_problem(b=b))), 1)

    def test_inequality_values(self):
        """Only infinite values that disable inequalities are allowed."""
        h = np.array([1.0, np.nan, 2.0])
        self.assertEqual(len(check_problem(make_problem(h=h))), 1)
        h = np.array([1.0, -np.inf, 2.0])
        self.assertEqual(len(check_problem(make_problem(h=h))), 1)
        lb = np.array([np.inf, 0.0])
        self.assertEqual(len(check_problem(make_problem(lb=lb))), 1)
        ub = np.array([1.0, -np.inf])
        self.assertEqual(len(check_problem(make_problem(ub=ub))), 1)

    def test_incomplete_constraints(self):
        """Constraints with a missing matrix or vector are reported."""
        self.assertEqual(len(check_problem(make_problem(h=None))), 1)
        self.assertEqual(len(check_problem(make_problem(A=None))), 1)

    def test_check_test_set(self):
        """Well-formed test sets have no issue."""
        self.assertEqual(check_test_set(CustomTestSet()), [])

    def test_duplicate_names(self):
        """Duplicate problem names are reported."""

        class DuplicateTestSet(CustomTestSet):
            def __iter__(self):
                yield make_problem(name="SAME")
                yield make_problem(name="SAME")

        self.assertEqual(
            check_test_set(DuplicateTestSet()),
            ["SAME: problem name appears 2 times"],
        )
