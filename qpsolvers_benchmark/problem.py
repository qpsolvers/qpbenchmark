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

from time import perf_counter
from typing import Optional, Union

import numpy as np
import qpsolvers
import scipy.sparse as spa
from numpy import linalg

from .spdlog import logging


class Problem(qpsolvers.Problem):

    """
    Quadratic program.

    Attributes:
        cost_offset: Cost offset, used to compare solution cost to a known
            optimal one. Defaults to zero.
        name: Name of the problem, for reporting.
        optimal_cost: If known, cost at the optimum of the problem.
    """

    cost_offset: float
    name: str
    optimal_cost: Optional[float]

    def __init__(
        self,
        P: Union[np.ndarray, spa.csc_matrix],
        q: np.ndarray,
        G: Optional[Union[np.ndarray, spa.csc_matrix]],
        h: Optional[np.ndarray],
        A: Optional[Union[np.ndarray, spa.csc_matrix]],
        b: Optional[np.ndarray],
        lb: Optional[np.ndarray],
        ub: Optional[np.ndarray],
        name: str,
        optimal_cost: Optional[float] = None,
        cost_offset: float = 0.0,
    ):
        """
        Quadratic program in qpsolvers format.
        """
        super().__init__(P, q, G, h, A, b, lb, ub)
        self.cost_offset = cost_offset
        self.name = name
        self.optimal_cost = optimal_cost

    def to_dense(self):
        """
        Return dense version.

        Returns:
            Dense version of the present problem.
        """
        return Problem(
            self.P.toarray().astype(float),
            self.q,
            self.G.toarray().astype(float),
            self.h,
            self.A.toarray().astype(float),
            self.b,
            self.lb,
            self.ub,
            name=self.name,
            optimal_cost=self.optimal_cost,
            cost_offset=self.cost_offset,
        )

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
            solution = qpsolvers.solve_qp(
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
            logging.warning(f"Caught solver exception: {e}")
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
        cost = 0.5 * x.dot(P.dot(x)) + q.dot(x) + self.cost_offset
        return cost - self.optimal_cost

    def primal_error(self, x: Optional[np.ndarray]) -> Optional[float]:
        """
        Compute the primal residual for a given vector.

        Args:
            x: Primal candidate.

        Returns:
            Primal residual, i.e. the largest constraint violation.

        Notes:
            This function is adapted from `is_qp_solution_optimal` in
            proxqp_benchmark. The original function included the relative
            tolerance parameter specified in the OSQP paper, set to zero.

            See `Optimality conditions and numerical tolerances in QP solvers
            <https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html>`__
            for a primer on residuals.
        """
        if x is None:
            return None
        C_list = []
        l_list = []
        u_list = []
        if self.G is not None and self.h is not None:
            C_list.append(spa.csc_matrix(self.G))
            l_list.append(np.full(self.h.shape, -np.infty))
            u_list.append(self.h)
        if self.A is not None and self.b is not None:
            C_list.append(spa.csc_matrix(self.A))
            l_list.append(self.b)
            u_list.append(self.b)
        if self.lb is not None or self.ub is not None:
            n: int = self.P.shape[0]
            C_list.append(spa.eye(n))
            l_list.append(
                self.lb
                if self.lb is not None
                else np.full(self.ub.shape, -np.infty)  # type: ignore
            )
            u_list.append(
                self.ub
                if self.ub is not None
                else np.full(self.lb.shape, +np.infty)  # type: ignore
            )
        if not C_list:  # no constraint
            return 0.0
        C = spa.vstack(C_list, format="csc")
        l = np.hstack(l_list)
        u = np.hstack(u_list)
        C_x = C.dot(x)
        p = np.minimum(C_x - l, 0.0) + np.maximum(C_x - u, 0.0)
        return linalg.norm(p, np.inf)  # type: ignore
