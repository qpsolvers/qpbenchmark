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

from qpsolvers import available_solvers, sparse_solvers

from .problem import Problem
from .results import Results
from .solver_issues import skip_solver_issue
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

    def __init__(
        self,
        data_dir: str,
    ):
        """
        Initialize test set.

        Args:
            data_dir: Path to data directory.
        """
        solvers = sparse_solvers if self.sparse_only else available_solvers
        self.solvers = solvers

    def run(
        self,
        solver_settings: Dict[str, SolverSettings],
        results: Results,
        only_problem: Optional[str] = None,
        only_solver: Optional[str] = None,
    ) -> None:
        """
        Run test set.

        Args:
            results: Results instance to write to.
            only_problem: If set, only run that specific problem in the set.
            only_solver: If set, only run that specific solver.
        """
        nb_called = 0
        solvers = [only_solver] if only_solver else self.solvers
        for problem in self:
            if only_problem and problem.name != only_problem:
                continue
            for solver in solvers:
                for settings in solver_settings:
                    if skip_solver_issue(problem, solver):
                        failure = problem, solver, settings, None, 0.0
                        results.update(*failure)
                        continue
                    if results.has(problem, solver, settings):
                        logging.info(
                            f"{problem.name} already solved by {solver} "
                            f"with {settings} settings..."
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
