# SPDX-License-Identifier: Apache-2.0

"""Unit tests for the scales of optimality conditions."""

import unittest

import numpy as np
import qpsolvers
import scipy.sparse as spa

from qpbenchmark.scales import compute_scales


class TestScales(unittest.TestCase):
    """Test fixture for scales."""

    def test_compute_scales(self):
        """Check scales by hand, skipping rows with infinite bounds."""
        P = np.array([[2.0, -1.0], [-1.0, 3.0]])
        G = np.array([[1.0, -2.0], [0.0, 1.0]])
        A = np.array([[-1.0, 1.0]])
        for to_matrix in (np.asarray, spa.csc_matrix):
            problem = qpsolvers.Problem(
                P=to_matrix(P),
                q=np.array([1.0, -1.0]),
                G=to_matrix(G),
                h=np.array([3.0, np.inf]),
                A=to_matrix(A),
                b=np.array([-2.0]),
                lb=np.array([-np.inf, -5.0]),
                ub=np.array([4.0, np.inf]),
            )
            solution = qpsolvers.Solution(problem)
            solution.x = np.array([1.0, -2.0])
            solution.y = np.array([-3.0])
            solution.z = np.array([0.5, 0.0])
            solution.z_box = np.array([1.5, -0.25])
            primal, dual, gap = compute_scales(solution)
            # max(|A||x| + |b|, |G||x| + |h|, |x| + |lb|, |x| + |ub|)
            self.assertAlmostEqual(primal, max(5.0, 8.0, 7.0, 5.0))
            # max(|P||x| + |q| + |A^T||y| + |G^T||z| + |z_box|)
            self.assertAlmostEqual(dual, max(10.0, 12.25))
            # Sum of |x^T P x|, |q^T x|, |b^T y|, |h^T z|, box terms
            self.assertAlmostEqual(gap, 18.0 + 3.0 + 6.0 + 1.5 + 1.25 + 6.0)

    def test_no_solution(self):
        """Scales are undefined when there is no primal vector."""
        problem = qpsolvers.Problem(P=np.eye(2), q=np.ones(2))
        scales = compute_scales(qpsolvers.Solution(problem))
        self.assertTrue(np.isnan(scales).all())


if __name__ == "__main__":
    unittest.main()
