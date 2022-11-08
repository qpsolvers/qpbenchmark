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

from typing import Any, Dict, Iterator, Set

import numpy as np


class SolverSettings:

    """
    Apply settings to multiple solvers at once.
    """

    IMPLEMENTED_SOLVERS: Set[str] = set(
        [
            "cvxopt",
            "ecos",
            "gurobi",
            "highs",
            "osqp",
            "proxqp",
            "qpoases",
            "qpswift",
            "quadprog",
            "scs",
        ]
    )

    @classmethod
    def is_implemented(cls, solver: str):
        """
        Check whether a solver is implemented by this class.
        """
        return solver in cls.IMPLEMENTED_SOLVERS

    def __init__(self, time_limit: float):
        """
        Initialize settings.

        Args:
            time_limit: Time limit in seconds.
        """
        self.__settings: Dict[str, Dict[str, Any]] = {
            solver: {} for solver in self.IMPLEMENTED_SOLVERS
        }
        #
        self.__apply_time_limit(time_limit)

    def __getitem__(self, solver: str) -> Dict[str, Any]:
        """
        Get settings dictionary of a given solver.

        Args:
            solver: Name of the QP solver.

        Returns:
            Dictionary of custom solver settings.
        """
        return self.__settings[solver]

    def __apply_time_limit(self, time_limit: float) -> None:
        """
        Apply time limits to all solvers.

        Args:
            time_limit: Time limit in seconds.
        """
        self.__settings["gurobi"]["time_limit"] = time_limit
        self.__settings["highs"]["time_limit"] = time_limit
        self.__settings["osqp"]["time_limit"] = time_limit
        self.__settings["qpoases"]["time_limit"] = time_limit
        self.__settings["scs"]["time_limit_secs"] = time_limit

    def apply_absolute_tolerance(self, eps_abs: float) -> None:
        """
        Apply absolute tolerance, disable relative tolerance for all solvers.

        Args:
            eps_abs: Absolute primal feasibility tolerance.

        Notes:
            The primal residual of a solution :math:`(x, y, z)` consists of
            :math:`r_{prim,eq} = A x - b` and :math:`r_{prim,ineq} = \\max(0, G
            x - h)`. The overall primal residual is the maximum of these two.
            The dual residual is :math:`r_{dual} = P x + q + A^T y + G^T z`.
            Hence, when we ask for an absolute tolerance
            :math:`\\epsilon_{abs}` on residuals, we want the solver to find an
            approximation of the optimum such that:

            .. math::

                \\begin{align}
                \\| P x + g + A^T y + C^T z \\|_\\infty
                & \\leq \\epsilon_{abs} \\\\
                \\| A x - b \\|_\\infty & \\leq \\epsilon_{abs} \\\\
                \\| \\max(0, G x - h) \\|_\\infty & \\leq \\epsilon_{abs}
                \\end{align}

            The tolerance on the primal residual is called "feasibility
            tolerance" by some solvers, for instance CVXOPT and ECOS.
            See `this note
            <https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html>`__
            for details.
        """
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

    def apply_verbosity(self, verbose: bool) -> None:
        """
        Apply verbosity settings to all solvers.

        Args:
            verbose: Verbosity boolean.
        """
        for solver in self.IMPLEMENTED_SOLVERS:
            self.__settings[solver]["verbose"] = verbose

    @property
    def solvers(self) -> Iterator[str]:
        for solver in self.__settings:
            yield solver

    def get_param(self, solver: str, param: str, default: str) -> Any:
        if solver not in self.__settings:
            return default
        return self.__settings[solver].get(param, default)

    def set_param(self, solver: str, param: str, value: Any) -> None:
        self.__settings[solver][param] = value
