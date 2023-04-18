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

"""Matrix-vector representation of a quadratic program."""

from typing import Optional, Union

import numpy as np
import qpsolvers
import scipy.sparse as spa


class Problem(qpsolvers.Problem):
    """Quadratic program.

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
        """Quadratic program in qpsolvers format."""
        super().__init__(P, q, G, h, A, b, lb, ub)
        self.cost_offset = cost_offset
        self.name = name
        self.optimal_cost = optimal_cost

    def to_dense(self):
        """Return dense version.

        Returns:
            Dense version of the present problem.
        """
        return Problem(
            self.P.toarray().astype(float),
            self.q,
            self.G.toarray().astype(float) if self.G is not None else None,
            self.h,
            self.A.toarray().astype(float) if self.A is not None else None,
            self.b,
            self.lb,
            self.ub,
            name=self.name,
            optimal_cost=self.optimal_cost,
            cost_offset=self.cost_offset,
        )

    def to_sparse(self):
        """Return sparse version.

        Returns:
            Sparse version of the present problem.
        """
        P, G, A = self.P, self.G, self.A
        return Problem(
            spa.csc_matrix(P) if isinstance(P, np.ndarray) else P,
            self.q,
            spa.csc_matrix(G) if isinstance(G, np.ndarray) else G,
            self.h,
            spa.csc_matrix(A) if isinstance(A, np.ndarray) else A,
            self.b,
            self.lb,
            self.ub,
            name=self.name,
            optimal_cost=self.optimal_cost,
            cost_offset=self.cost_offset,
        )

    def cost_error(self, solution: qpsolvers.Solution) -> Optional[float]:
        """Compute difference between found cost and the optimal one.

        Args:
            solution: Problem solution.

        Returns:
            Cost error, i.e. deviation from the (known) optimal cost.

        Note:
            Cost errors can be negative when the primal residual is large. We
            count that as errors as well using absolute values.
        """
        x = solution.x
        if not solution.found or x is None or self.optimal_cost is None:
            return None
        P, q = self.P, self.q
        cost = 0.5 * x.dot(P.dot(x)) + q.dot(x) + self.cost_offset
        return abs(cost - self.optimal_cost)
