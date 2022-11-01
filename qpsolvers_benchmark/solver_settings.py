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

KNOWN_SOLVERS: Set[str] = set(
    [
        "cvxopt",
        "gurobi",
        "highs",
        "osqp",
        "proxqp",
        "qpswift",
        "scs",
    ]
)


class SolverSettings:

    """
    Apply general settings to multiple solvers at once.
    """

    def __init__(
        self,
        time_limit: float,
        verbose: bool,
        eps_abs: Optional[float] = None,
        eps_rel: Optional[float] = None,
    ):
        self.eps_abs = eps_abs
        self.eps_rel = eps_rel
        self.time_limit = time_limit
        self.verbose = verbose
        #
        self.__settings: Dict[str, Dict[str, Any]] = {
            solver: {} for solver in KNOWN_SOLVERS
        }
        self.apply_time_limits()
        self.apply_tolerances()
        self.apply_verbosity()

    def __getitem__(self, solver: str) -> Dict[str, Any]:
        try:
            return self.__settings[solver]
        except KeyError as e:
            raise KeyError(f"unknown solver {str(e)}") from e

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
        Apply absolute and relative tolerances to all solvers.
        """
        if self.eps_abs is not None:
            self.__settings["osqp"]["eps_abs"] = self.eps_abs
            self.__settings["qpswift"]["ABSTOL"] = self.eps_abs
        if self.eps_rel is not None:
            self.__settings["osqp"]["eps_rel"] = self.eps_rel
            self.__settings["qpswift"]["RELTOL"] = self.eps_abs

    def apply_verbosity(self) -> None:
        """
        Apply verbosity settings to all solvers.
        """
        for solver in KNOWN_SOLVERS:
            self.__settings[solver]["verbose"] = self.verbose
