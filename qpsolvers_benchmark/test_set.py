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
Base class for test sets.
"""

import abc
from typing import Dict, Iterator, Optional

import qpsolvers
from qpsolvers.exceptions import SolverNotFound

from .problem import Problem
from .results import Results
from .solver_issues import skip_solver_issue, skip_solver_timeout
from .solver_settings import SolverSettings
from .spdlog import logging


class TestSet(abc.ABC):

    results: Results

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Problem]:
        """
        Yield test problems one by one.
        """

    @abc.abstractmethod
    def get_solver_settings(self) -> Dict[str, SolverSettings]:
        """
        Get solver settings for the test set.
        """

    @abc.abstractproperty
    def sparse_only(self) -> bool:
        """
        If True, test set is restricted to solvers with a sparse matrix API.
        """

    @abc.abstractproperty
    def title(self) -> str:
        """
        Report title.
        """

    def __init__(self):
        """
        Initialize test set.
        """
        candidate_solvers = set(
            qpsolvers.sparse_solvers
            if self.sparse_only
            else qpsolvers.available_solvers
        )
        known_solvers = set(
            solver
            for solver in candidate_solvers
            if SolverSettings.is_known_solver(solver)
        )
        for solver in candidate_solvers - known_solvers:
            logging.warning(
                f"Solver '{solver}' is available but skipped "
                "as its settings are unknown"
            )
        self.solver_settings = self.get_solver_settings()
        self.solvers = known_solvers

    def get_problem(self, name: str) -> Optional[Problem]:
        """
        Get a specific test set problem.

        Args:
            name: Problem name.

        Returns:
            Problem if found, None otherwise.
        """
        for problem in self:
            if problem.name == name:
                return problem
        return None

    def get_cost_error_limits(self) -> Dict[str, float]:
        """
        Get cost error limits for each settings.

        Returns:
            Dictionary from settings name to cost error limit.
        """
        return {
            name: settings.cost_error_limit
            for name, settings in self.solver_settings.items()
        }

    def get_primal_error_limits(self) -> Dict[str, float]:
        """
        Get primal error limits for each settings.

        Returns:
            Dictionary from settings name to primal residual limit.
        """
        return {
            name: settings.primal_error_limit
            for name, settings in self.solver_settings.items()
        }

    def get_time_limits(self) -> Dict[str, float]:
        """
        Get time limits for each settings.

        Returns:
            Dictionary from settings name to time limit.
        """
        return {
            name: settings.time_limit
            for name, settings in self.solver_settings.items()
        }

    def run(
        self,
        results: Results,
        only_problem: Optional[str] = None,
        only_settings: Optional[str] = None,
        only_solver: Optional[str] = None,
        rerun: bool = False,
        include_timeouts: bool = False,
    ) -> None:
        """
        Run test set.

        Args:
            results: Results instance to write to.
            only_problem: If set, only run that specific problem in the set.
            only_settings: If set, only run with these solver settings.
            only_solver: If set, only run that specific solver.
            rerun: If set, rerun instances that already have a result.
            include_timeouts: If set, also rerun known timeouts.
        """
        if only_settings and only_settings not in self.solver_settings:
            raise ValueError(
                f"settings '{only_settings}' not in the list of settings "
                f"for this test set: {list(self.solver_settings.keys())}"
            )
        if only_solver and only_solver not in self.solvers:
            raise SolverNotFound(
                f"solver '{only_solver}' not in the list of "
                f"available solvers for this test set: {self.solvers}"
            )

        filtered_solvers = [
            solver
            for solver in self.solvers
            if only_solver is None or solver == only_solver
        ]
        filtered_settings = [
            settings
            for settings in self.solver_settings.keys()
            if only_settings is None or settings == only_settings
        ]

        nb_called = 0
        for problem in self:
            if only_problem and problem.name != only_problem:
                continue
            for solver in filtered_solvers:
                for settings in filtered_settings:
                    time_limit = self.solver_settings[settings].time_limit
                    if skip_solver_issue(problem, solver):
                        failure = problem, solver, settings, None, 0.0
                        results.update(*failure)
                        continue
                    if skip_solver_timeout(time_limit, problem, solver):
                        failure = problem, solver, settings, None, 0.0
                        results.update(*failure)
                        continue
                    if results.has(problem, solver, settings):
                        if not rerun:
                            logging.debug(
                                f"{problem.name} already solved by {solver} "
                                f"with {settings} settings..."
                            )
                            continue
                        elif not include_timeouts and results.is_timeout(
                            problem, solver, settings, time_limit
                        ):
                            logging.info(
                                f"Skipping {problem.name} with {solver} and "
                                f"{settings} settings as a known timeout..."
                            )
                            continue
                    logging.debug(
                        f"Solving {problem.name} by {solver} "
                        f"with {settings} settings..."
                    )
                    kwargs = self.solver_settings[settings][solver]
                    solution, runtime = problem.solve(solver, **kwargs)
                    results.update(
                        problem, solver, settings, solution, runtime
                    )
                    results.write()
                    nb_called += 1
        logging.info(f"Made {nb_called} QP solver calls")
