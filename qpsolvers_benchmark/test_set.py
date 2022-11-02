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

    @abc.abstractproperty
    def maintainer(self) -> str:
        """
        GitHub username of test set maintainer.
        """

    @abc.abstractproperty
    def name(self) -> str:
        """
        Name of the test set.
        """

    @abc.abstractproperty
    def sparse_only(self) -> bool:
        """
        If True, test set is restricted to solvers with a sparse matrix API.
        """

    @abc.abstractproperty
    def time_limit(self) -> float:
        """
        Runtime limit in seconds.
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
        self.solvers = (
            qpsolvers.sparse_solvers if self.sparse_only else qpsolvers.available_solvers
        )

    def run(
        self,
        solver_settings: Dict[str, SolverSettings],
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
        """
        nb_called = 0
        filtered_solvers = [
            solver
            for solver in self.solvers
            if only_solver is None or solver == only_solver
        ]
        filtered_settings = [
            settings
            for settings in solver_settings.keys()
            if only_settings is None or settings == only_settings
        ]
        for problem in self:
            if only_problem and problem.name != only_problem:
                continue
            for solver in filtered_solvers:
                for settings in filtered_settings:
                    if skip_solver_issue(problem, solver):
                        failure = problem, solver, settings, None, 0.0
                        results.update(*failure)
                        continue
                    if skip_solver_timeout(self.time_limit, problem, solver):
                        failure = problem, solver, settings, None, 0.0
                        results.update(*failure)
                        continue
                    if results.has(problem, solver, settings):
                        if not rerun:
                            logging.info(
                                f"{problem.name} already solved by {solver} "
                                f"with {settings} settings..."
                            )
                            continue
                        elif not include_timeouts and results.is_timeout(
                            problem, solver, settings, self.time_limit
                        ):
                            logging.warn(
                                f"Skipping {problem.name} with {solver} and "
                                f"{settings} settings as a known timeout..."
                            )
                            continue
                    logging.info(
                        f"Solving {problem.name} by {solver} "
                        f"with {settings} settings..."
                    )
                    kwargs = solver_settings[settings][solver]
                    solution, runtime = problem.solve(solver, **kwargs)
                    results.update(
                        problem, solver, settings, solution, runtime
                    )
                    results.write()
                    nb_called += 1
        logging.info(f"Made {nb_called} QP solver calls")
