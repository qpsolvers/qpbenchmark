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
from time import perf_counter
from typing import Dict, Iterator, Optional, Tuple

import qpsolvers
from qpsolvers.exceptions import SolverNotFound

from .problem import Problem
from .results import Results
from .solver_issues import skip_solver_issue, skip_solver_timeout
from .solver_settings import SolverSettings
from .spdlog import logging
from .tolerance import Tolerance


def time_solve_problem(
    problem, solver: str, **kwargs
) -> Tuple[qpsolvers.Solution, float]:
    """
    Solve quadratic program.

    Args:
        problem: Quadratic program to solve.
        solver: Name of the backend QP solver to call.

    Returns:
        Solution to the quadratic program, along with the time the solver took
        to compute it.
    """
    # Don't time matrix conversions for solvers that require sparse inputs
    if solver in ["highs", "osqp", "scs"]:
        problem = problem.to_sparse()
    start_time = perf_counter()
    try:
        solution = qpsolvers.solve_problem(problem, solver=solver, **kwargs)
    except Exception as e:
        logging.warning(f"Caught solver exception: {e}")
        solution = qpsolvers.Solution(problem)
    runtime = perf_counter() - start_time
    return solution, runtime


class TestSet(abc.ABC):

    solver_settings: Dict[str, SolverSettings]
    tolerances: Dict[str, Tolerance]

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Problem]:
        """
        Yield test problems one by one.
        """

    @abc.abstractproperty
    def description(self) -> Optional[str]:
        """
        Test set description for the report (optional).
        """

    @abc.abstractmethod
    def define_tolerances(self):
        """
        Define validation tolerances.
        """

    @abc.abstractmethod
    def define_solver_settings(self):
        """
        Define solver settings.
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
        solvers = set(
            solver
            for solver in candidate_solvers
            if SolverSettings.is_implemented(solver)
        )
        for solver in candidate_solvers - solvers:
            logging.warning(
                f"Solver '{solver}' is available but skipped "
                "as its settings are unknown"
            )
        self.solver_settings = {}
        self.solvers = solvers
        self.tolerances = {}
        #
        self.define_tolerances()
        self.define_solver_settings()
        self.check_definitions()

    def check_definitions(self):
        """
        Check that settings and tolerance definitions are consistent.

        Raises:
            ValueError: in case of inconsistency.
        """
        tolerances = set(self.tolerances.keys())
        settings = set(self.solver_settings.keys())
        if tolerances != settings:
            logging.error("Settings are not consistent with tolerances")
            logging.info(f"Settings: {settings}")
            logging.info(f"Tolerances: {tolerances}")
            raise ValueError("Settings are not consistent with tolerances")

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
        raise KeyError(
            f"problem '{name}' not found "
            f"in the {self.__class__.__name__} test set"
        )

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
        start_counter = perf_counter()
        for problem in self:
            if only_problem and problem.name != only_problem:
                continue
            for solver in filtered_solvers:
                for settings in filtered_settings:
                    time_limit = self.tolerances[settings].runtime
                    if skip_solver_issue(problem, solver):
                        failure = (
                            problem,
                            solver,
                            settings,
                            qpsolvers.Solution(problem),
                            0.0,
                        )
                        results.update(*failure)
                        continue
                    if skip_solver_timeout(
                        time_limit, problem, solver, settings
                    ):
                        failure = (
                            problem,
                            solver,
                            settings,
                            qpsolvers.Solution(problem),
                            0.0,
                        )
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
                                f"{settings} settings as a previous timeout..."
                            )
                            continue
                    logging.info(
                        f"Solving {problem.name} by {solver} "
                        f"with {settings} settings..."
                    )
                    kwargs = self.solver_settings[settings][solver]
                    solution, runtime = time_solve_problem(
                        problem, solver, **kwargs
                    )
                    results.update(
                        problem, solver, settings, solution, runtime
                    )
                    results.write()
                    nb_called += 1

        duration = perf_counter() - start_counter
        logging.info(f"Ran the test set in {duration:.0f} seconds")
        logging.info(f"Made {nb_called} QP solver calls")
