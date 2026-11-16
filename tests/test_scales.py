# SPDX-License-Identifier: Apache-2.0

"""Unit tests for the magnitudes involved in optimality conditions."""

import unittest

import numpy as np
import qpsolvers
import scipy.sparse as spa

from qpbenchmark.scales import dual_scale, gap_scale, primal_scale


def make_solution(sparse: bool = False) -> qpsolvers.Solution:
    """Build a solution with all types of constraints and mixed signs.

    Args:
        sparse: If true, use sparse matrices in the problem.

    Returns:
        Solution with hand-picked primal and dual vectors.
    """
    P = np.array([[2.0, -1.0], [-1.0, 3.0]])
    G = np.array([[1.0, -2.0], [0.0, 1.0]])
    A = np.array([[-1.0, 1.0]])
    if sparse:
        P, G, A = spa.csc_matrix(P), spa.csc_matrix(G), spa.csc_matrix(A)
    problem = qpsolvers.Problem(
        P=P,
        q=np.array([1.0, -1.0]),
        G=G,
        h=np.array([3.0, np.inf]),
        A=A,
        b=np.array([-2.0]),
        lb=np.array([-np.inf, -5.0]),
        ub=np.array([4.0, np.inf]),
    )
    solution = qpsolvers.Solution(problem)
    solution.found = True
    solution.x = np.array([1.0, -2.0])
    solution.y = np.array([-3.0])
    solution.z = np.array([0.5, 0.0])
    solution.z_box = np.array([1.5, -0.25])
    return solution


class TestScales(unittest.TestCase):
    """Test fixture for scales."""

    def test_primal_scale(self):
        """Primal scale is the max of row magnitudes over finite rows."""
        # |A||x| + |b| = 3 + 2 = 5
        # |G||x| + |h| = (1 + 4) + 3 = 8 (second row has infinite h)
        # |x| + |lb| = 2 + 5 = 7 (first entry has infinite lb)
        # |x| + |ub| = 1 + 4 = 5 (second entry has infinite ub)
        for sparse in (False, True):
            self.assertAlmostEqual(primal_scale(make_solution(sparse)), 8.0)

    def test_dual_scale(self):
        """Dual scale is the max over components of all term magnitudes."""
        # |P||x| = [4, 7], |q| = [1, 1], |A^T||y| = [3, 3],
        # |G^T||z| = [0.5, 1.0], |z_box| = [1.5, 0.25]
        # Sums: [10, 12.25]
        for sparse in (False, True):
            self.assertAlmostEqual(dual_scale(make_solution(sparse)), 12.25)

    def test_gap_scale(self):
        """Gap scale is the sum of the absolute values of all terms."""
        # |x|^T |P| |x| = [1, 2] . [4, 7] = 18
        # |q|^T |x| = 3, |b|^T |y| = 6, |h|^T |z| = 1.5 (finite h only)
        # |lb|^T |z_box^-| = 5 * 0.25, |ub|^T |z_box^+| = 4 * 1.5
        expected = 18.0 + 3.0 + 6.0 + 1.5 + 1.25 + 6.0
        for sparse in (False, True):
            self.assertAlmostEqual(gap_scale(make_solution(sparse)), expected)

    def test_no_solution(self):
        """Scales are undefined when there is no primal vector."""
        solution = make_solution()
        solution.x = None
        self.assertTrue(np.isnan(primal_scale(solution)))
        self.assertTrue(np.isnan(dual_scale(solution)))
        self.assertTrue(np.isnan(gap_scale(solution)))

    def test_unconstrained(self):
        """Scales of an unconstrained problem only involve P and q."""
        problem = qpsolvers.Problem(P=np.eye(2), q=np.array([1.0, -2.0]))
        solution = qpsolvers.Solution(problem)
        solution.x = np.array([-1.0, 2.0])
        self.assertAlmostEqual(primal_scale(solution), 0.0)
        self.assertAlmostEqual(dual_scale(solution), 4.0)
        self.assertAlmostEqual(gap_scale(solution), 5.0 + 5.0)


if __name__ == "__main__":
    unittest.main()
