#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import scipy.io as spio
import scipy.sparse as spa
from numpy import linalg


class Problem:
    def __init__(self, P, q, G, h, A, b, lb, ub):
        """
        Quadratic program in qpsolvers format.
        """
        self.P = P
        self.q = q
        self.G = G
        self.h = h
        self.A = A
        self.b = b
        self.lb = lb
        self.ub = ub

    @staticmethod
    def from_mat_file(path):
        """
        Load problem from MAT file.

        Args:
            path: Path to file.

        Notes:
            We assume that matrix files result from calling `sif2mat.m` in
            proxqp_benchmark. In particular, ``A = [sparse(A_c); speye(n)];``.
        """
        mat_dict = spio.loadmat(path)
        P = mat_dict["P"].astype(float).tocsc()
        q = mat_dict["q"].T.flatten().astype(float)
        A = mat_dict["A"].astype(float).tocsc()
        l = mat_dict["l"].T.flatten().astype(float)
        u = mat_dict["u"].T.flatten().astype(float)
        n = mat_dict["n"].T.flatten().astype(int)[0]
        m = mat_dict["m"].T.flatten().astype(int)[0]
        assert A.shape == (m, n)
        lb = l[-n:]
        ub = u[-n:]
        A_c = A[:-n]
        l_c = l[:-n]
        u_c = u[:-n]
        return Problem.from_double_sided_ineq(P, q, A_c, l_c, u_c, lb, ub)

    @staticmethod
    def from_double_sided_ineq(P, q, A, l, u, lb, ub):
        """
        Load problem from double-sided inequality format:

        .. code::

            minimize        0.5 x^T P x + q^T x
            subject to      l <= A x <= u
                            lb <= x <= ub

        Args:
            P: Cost matrix.
            q: Cost vector.
            A: Constraint inequality matrix.
            l: Constraint lower bound.
            u: Constraint upper bound.
            lb: Box lower bound.
            ub: Box upper bound.
        """
        bounds_are_equal = u - l < 1e-10
        eq_rows = np.where(bounds_are_equal)
        eq_matrix = A[eq_rows]
        eq_vector = u[eq_rows]
        ineq_rows = np.where(np.logical_not(bounds_are_equal))
        ineq_matrix = spa.vstack([A[ineq_rows], -A[ineq_rows]], format="csc")
        ineq_vector = np.hstack([u[ineq_rows], -l[ineq_rows]])
        return Problem(
            P, q, ineq_matrix, ineq_vector, eq_matrix, eq_vector, lb, ub
        )

    def constraints_as_double_sided_ineq(self):
        """
        ...
        """
        C = spa.vstack([self.G, self.A, spa.eye(self.n)], format="csc")
        l = np.hstack([np.full(self.h.shape, -np.infty), self.b, self.lb])
        u = np.hstack([self.h, self.b, self.ub])
        return C, l, u

    def is_valid_primal_solution(self, x, eps_abs: float) -> bool:
        """
        Validate optimality condition of a given primal solution.

        Args:
            x: Primal solution.
            eps_abs: Absolute tolerance.

        Returns:
            True if and only if (x, y) is a valid primal-dual solution.

        Note:
            This function is adapted from `is_qp_solution_optimal` in
            proxqp_benchmark. The original function included the relative
            tolerance parameter specified in the OSQP paper, set to zero.
        """
        C, l, u = self.constraints_as_double_sided_ineq()
        C_x = C.dot(x)
        primal_residual = np.minimum(C_x - l, 0.0) + np.maximum(C_x - u, 0.0)
        primal_error = linalg.norm(primal_residual, np.inf)
        if primal_error > eps_abs:
            print(f"Error in primal residual: {primal_error} > {eps_abs}")
            return False

        return True

    def is_valid_dual_solution(self, y, x, eps_abs: float) -> bool:
        """
        Validate optimality condition of a given primal solution.

        Args:
            x: Primal solution.
            y: Dual solution.
            eps_abs: Absolute tolerance.

        Returns:
            True if and only if (x, y) is a valid primal-dual solution.

        Note:
            This function is adapted from `is_qp_solution_optimal` in
            proxqp_benchmark. The original function included the relative
            tolerance parameter specified in the OSQP paper, set to zero.
        """
        P = self.P
        q = self.q
        C, _, _ = self.constraints_as_double_sided_ineq()
        dual_residual = P.dot(x) + q + C.T.dot(y)
        dual_error = linalg.norm(dual_residual, np.inf)
        if dual_error > eps_abs:
            print(f"Error in dual residual: {dual_error} > {eps_abs}")
            return False
        return True
