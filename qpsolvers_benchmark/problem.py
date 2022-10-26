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

"""
Matrix-vector representation of a quadratic program.
"""

import os
from typing import Union

import numpy as np
import scipy.io as spio
import scipy.sparse as spa
from qpsolvers import solve_qp


class Problem:

    """
    Quadratic program.
    """

    A: Union[np.ndarray, spa.csc_matrix]
    G: Union[np.ndarray, spa.csc_matrix]
    P: Union[np.ndarray, spa.csc_matrix]
    b: np.ndarray
    h: np.ndarray
    lb: np.ndarray
    name: str
    q: np.ndarray
    ub: np.ndarray

    def __init__(self, P, q, G, h, A, b, lb, ub, name: str):
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
        self.n = P.shape[0]
        self.name = name

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
        name = os.path.basename(path)
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
        C = A[:-n]
        l_c = l[:-n]
        u_c = u[:-n]
        return Problem.from_double_sided_ineq(
            P, q, C, l_c, u_c, lb, ub, name=name
        )

    @staticmethod
    def from_double_sided_ineq(P, q, C, l, u, lb, ub, name: str):
        """
        Load problem from double-sided inequality format:

        .. code::

            minimize        0.5 x^T P x + q^T x
            subject to      l <= C x <= u
                            lb <= x <= ub

        Args:
            P: Cost matrix.
            q: Cost vector.
            C: Constraint inequality matrix.
            l: Constraint lower bound.
            u: Constraint upper bound.
            lb: Box lower bound.
            ub: Box upper bound.
        """
        bounds_are_equal = u - l < 1e-10
        eq_rows = np.where(bounds_are_equal)
        eq_matrix = C[eq_rows]
        eq_vector = u[eq_rows]
        ineq_rows = np.where(np.logical_not(bounds_are_equal))
        ineq_matrix = spa.vstack([C[ineq_rows], -C[ineq_rows]], format="csc")
        ineq_vector = np.hstack([u[ineq_rows], -l[ineq_rows]])
        return Problem(
            P,
            q,
            ineq_matrix,
            ineq_vector,
            eq_matrix,
            eq_vector,
            lb,
            ub,
            name=name,
        )

    def constraints_as_double_sided_ineq(self):
        """
        Get problem constraints as double-sided inequalities.

        Returns:
            Tuple ``(C, l, u)`` corresponding to ``l <= C x <= u``.
        """
        C = spa.vstack([self.G, self.A, spa.eye(self.n)], format="csc")
        l = np.hstack([np.full(self.h.shape, -np.infty), self.b, self.lb])
        u = np.hstack([self.h, self.b, self.ub])
        return C, l, u

    def solve(self, solver: str, **kwargs):
        """
        Solve quadratic program.

        Args:
            solver: Name of the backend QP solver to call.

        Returns:
            Primal solution to the quadratic program, or None if it is
            unfeasible.
        """
        return solve_qp(
            self.P,
            self.q,
            G=self.G,
            h=self.h,
            A=self.A,
            b=self.b,
            lb=self.lb,
            ub=self.ub,
            solver=solver,
            **kwargs,
        )
