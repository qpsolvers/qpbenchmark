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
Solver settings.
"""

from typing import Any, Dict, Optional, Set

import numpy as np


class SolverSettings:

    """
    Apply general settings to multiple solvers at once.

    Attributes:
        absolute_tolerance: Absolute tolerance on primal and dual residuals.

    The primal residual of a solution :math:`(x, y, z)` consists of
    :math:`r_{prim,eq} = A x - b` and :math:`r_{prim,ineq} = \\max(0, G x -
    h)`. The overall primal residual is the maximum of these two.

    The dual residual is :math:`r_{dual} = P x + q + A^T y + G^T z`.

    Hence, when we ask for an absolute tolerance :math:`\\epsilon_{abs}` on
    residuals, we want the solver to find an approximation of the optimum such
    that:

    .. math::

        \\begin{align}
        \\| P x + g + A^T y + C^T z \\|_\\infty & \\leq \\epsilon_{abs} \\\\
        \\| A x - b \\|_\\infty & \\leq \\epsilon_{abs} \\\\
        \\| \\max(0, G x - h) \\|_\\infty & \\leq \\epsilon_{abs}
        \\end{align}

    Note:
        The tolerance on the primal residual is called "feasibility tolerance"
        by some solvers, for instance CVXOPT and ECOS.
    """

    absolute_tolerance: float
    time_limit: float

    KNOWN_SOLVERS: Set[str] = set(
        [
            "cvxopt",
            "ecos",
            "gurobi",
            "highs",
            "osqp",
            "proxqp",
            "qpswift",
            "quadprog",
            "scs",
        ]
    )

    @classmethod
    def is_known_solver(cls, solver: str):
        return solver in cls.KNOWN_SOLVERS

    def __init__(
        self,
        time_limit: float,
        primal_residual_limit: float,
        verbose: bool = False,
        absolute_tolerance: Optional[float] = None,
    ):
        self.absolute_tolerance = absolute_tolerance
        self.primal_residual_limit = primal_residual_limit
        self.time_limit = time_limit
        self.verbose = verbose
        #
        self.__settings: Dict[str, Dict[str, Any]] = {
            solver: {} for solver in self.KNOWN_SOLVERS
        }
        self.apply_time_limits()
        self.apply_tolerances()
        self.apply_verbosity()

    def __getitem__(self, solver: str) -> Dict[str, Any]:
        return self.__settings[solver]

    def apply_time_limits(self) -> None:
        """
        Apply time limits to all solvers.
        """
        self.__settings["gurobi"]["time_limit"] = self.time_limit
        self.__settings["highs"]["time_limit"] = self.time_limit
        self.__settings["osqp"]["time_limit"] = self.time_limit
        self.__settings["scs"]["time_limit_secs"] = self.time_limit

    def apply_tolerances(self) -> None:
        """
        Apply absolute tolerance, disable relative tolerance for all solvers.
        """
        eps_abs = self.absolute_tolerance
        if eps_abs is None:
            return
        self.__settings["cvxopt"]["feastol"] = eps_abs
        self.__settings["ecos"]["feastol"] = eps_abs
        self.__settings["highs"]["dual_feasibility_tolerance"] = eps_abs
        self.__settings["highs"]["primal_feasibility_tolerance"] = eps_abs
        self.__settings["osqp"]["eps_abs"] = eps_abs
        self.__settings["osqp"]["eps_rel"] = 0.0
        self.__settings["proxqp"]["eps_abs"] = eps_abs
        self.__settings["proxqp"]["eps_rel"] = 0.0
        self.__settings["qpswift"]["RELTOL"] = eps_abs * np.sqrt(3.0)
        self.__settings["scs"]["eps_abs"] = eps_abs
        self.__settings["scs"]["eps_rel"] = 0.0

    def apply_verbosity(self) -> None:
        """
        Apply verbosity settings to all solvers.
        """
        for solver in self.KNOWN_SOLVERS:
            self.__settings[solver]["verbose"] = self.verbose
