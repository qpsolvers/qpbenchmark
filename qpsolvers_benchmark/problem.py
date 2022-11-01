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
from time import perf_counter
from typing import Optional, Union

import numpy as np
import scipy.io as spio
import scipy.sparse as spa
from numpy import linalg
from qpsolvers import solve_qp


class Problem:

    """
    Quadratic program.

    Attributes:
        r: Cost offset, used to compare solution cost to a known optimal one.
    """

    A: Union[np.ndarray, spa.csc_matrix]
    G: Union[np.ndarray, spa.csc_matrix]
    P: Union[np.ndarray, spa.csc_matrix]
    b: np.ndarray
    h: np.ndarray
    lb: np.ndarray
    name: str
    optimal_cost: Optional[float]
    q: np.ndarray
    r: float
    ub: np.ndarray

    def __init__(
        self,
        P: Union[np.ndarray, spa.csc_matrix],
        q: np.ndarray,
        G: Union[np.ndarray, spa.csc_matrix],
        h: np.ndarray,
        A: Union[np.ndarray, spa.csc_matrix],
        b: np.ndarray,
        lb: np.ndarray,
        ub: np.ndarray,
        name: str,
        optimal_cost: Optional[float] = None,
        r: float = 0.0,
    ):
        """
        Quadratic program in qpsolvers format.
        """
        self.A = A
        self.G = G
        self.P = P
        self.b = b
        self.h = h
        self.lb = lb
        self.n = P.shape[0]
        self.name = name
        self.optimal_cost = optimal_cost
        self.q = q
        self.r = r
        self.ub = ub

    @property
    def nb_variables(self) -> int:
        """
        Number of optimization variables.
        """
        return self.P.shape[0]

    @property
    def nb_constraints(self) -> int:
        """
        Number of inequality and equality constraints.
        """
        return self.G.shape[0] + self.A.shape[0] + self.lb.shape[0]

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
        assert path.endswith(".mat")
        name = os.path.basename(path)[:-4]
        mat_dict = spio.loadmat(path)
        P = mat_dict["P"].astype(float).tocsc()
        q = mat_dict["q"].T.flatten().astype(float)
        r = mat_dict["r"].T.flatten().astype(float)[0]
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
            P, q, C, l_c, u_c, lb, ub, name=name, r=r
        )

    @staticmethod
    def from_double_sided_ineq(P, q, C, l, u, lb, ub, name: str, r: float):
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
            r=r,
        )

    def to_dense(self):
        """
        Return dense copy.

        Returns:
            Dense copy of the present problem.
        """
        return Problem(
            self.P.toarray(),
            self.q,
            self.G.toarray(),
            self.h,
            self.A.toarray(),
            self.b,
            self.lb,
            self.ub,
            self.name,
            self.optimal_cost,
            self.r,
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
        # Don't time matrix conversions for solvers that require sparse inputs
        P, G, A = self.P, self.G, self.A
        if solver in ["highs", "osqp", "scs"]:
            P = spa.csc_matrix(P) if isinstance(P, np.ndarray) else P
            G = spa.csc_matrix(G) if isinstance(G, np.ndarray) else G
            A = spa.csc_matrix(A) if isinstance(A, np.ndarray) else A
        start_time = perf_counter()
        try:
            solution = solve_qp(
                P,
                self.q,
                G=G,
                h=self.h,
                A=A,
                b=self.b,
                lb=self.lb,
                ub=self.ub,
                solver=solver,
                **kwargs,
            )
        except Exception as e:
            print(f"Caught solver exception: {e}")
            solution = None
        runtime = perf_counter() - start_time
        return solution, runtime

    def cost_error(self, x: Optional[np.ndarray]) -> Optional[float]:
        """
        Compute difference between found cost and the optimal one.

        Args:
            x: Primal solution.

        Returns:
            Cost error, i.e. deviation from the (known) optimal cost.
        """
        if x is None or self.optimal_cost is None:
            return None
        P, q = self.P, self.q
        cost = 0.5 * x.dot(P.dot(x)) + q.dot(x) + self.r
        return cost - self.optimal_cost

    def primal_error(self, x: Optional[np.ndarray]) -> Optional[float]:
        """
        Compute primal error for a given (primal) solution.

        Args:
            x: Primal solution.

        Returns:
            Primal error, i.e. the largest constraint violation.

        Note:
            This function is adapted from `is_qp_solution_optimal` in
            proxqp_benchmark. The original function included the relative
            tolerance parameter specified in the OSQP paper, set to zero.
        """
        if x is None:
            return None
        C, l, u = self.constraints_as_double_sided_ineq()
        C_x = C.dot(x)
        primal_residual = np.minimum(C_x - l, 0.0) + np.maximum(C_x - u, 0.0)
        return linalg.norm(primal_residual, np.inf)

    def dual_error(self, x, y) -> Optional[float]:
        """
        Compute dual error for a set of dual multipliers at a primal solution.

        Args:
            x: Primal solution.
            y: Dual solution.

        Returns:
            True if and only if (x, y) is a valid primal-dual solution.

        Note:
            This function is adapted from `is_qp_solution_optimal` in
            proxqp_benchmark. The original function included the relative
            tolerance parameter specified in the OSQP paper, set to zero.
        """
        P, q = self.P, self.q
        C, _, _ = self.constraints_as_double_sided_ineq()
        dual_residual = P.dot(x) + q + C.T.dot(y)
        return linalg.norm(dual_residual, np.inf)
