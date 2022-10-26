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
        # r = mat_dict["r"].T.flatten().astype(float)[0]
        A = mat_dict["A"].astype(float).tocsc()
        l = mat_dict["l"].T.flatten().astype(float)
        u = mat_dict["u"].T.flatten().astype(float)
        n = mat_dict["n"].T.flatten().astype(int)[0]
        m = mat_dict["m"].T.flatten().astype(int)[0]

        assert A.shape == (m, n)
        # assert (A[-n:] != spa.eye(n)).nnz == 0

        lb = l[-n:]
        ub = u[-n:]

        A = A[:-n]
        l = l[:-n]
        u = u[:-n]

        eq_mask = u - l < 1e-5
        eq_rows = np.where(eq_mask)
        ineq_rows = np.where(np.logical_not(eq_mask))
        print(eq_rows, ineq_rows)

        eq_matrix = A[eq_rows]
        eq_vector = u[eq_rows]
        ineq_matrix = spa.vstack([A[ineq_rows], -A[ineq_rows]], format="csc")
        ineq_vector = np.hstack([u[ineq_rows], -l[ineq_rows]])

        return Problem(
            P, q, ineq_matrix, ineq_vector, eq_matrix, eq_vector, lb, ub
        )

    def is_valid_solution(self, x, y, eps_abs):
        """
        Validate optimality condition of a given primal-dual solution.

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
        A = self.A
        l = self.l
        u = self.u

        A_x = A.dot(x)
        primal_residual = np.minimum(A_x - l, 0.0) + np.maximum(A_x - u, 0.0)
        primal_error = linalg.norm(primal_residual, np.inf)
        if primal_error > eps_abs:
            print(f"Error in primal residual: {primal_error} > {eps_abs}")
            return False

        dual_residual = P.dot(x) + q + A.T.dot(y)
        dual_error = linalg.norm(dual_residual, np.inf)
        if dual_error > eps_abs:
            print(f"Error in dual residual: {dual_error} > {eps_abs}")
            return False

        return True
