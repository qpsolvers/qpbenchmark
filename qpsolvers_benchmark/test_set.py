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
    def title(self) -> str:
        """
        Report title.
        """

    def __init__(
        self,
        data_dir: str,
        solver_settings: Dict[str, SolverSettings],
    ):
        """
        Initialize test set.

        Args:
            data_dir: Path to data directory.
            solver_settings: Keyword arguments for each solver.
        """
        solvers = sparse_solvers if self.sparse_only else available_solvers
        self.solvers = solvers
        self.solver_settings = solver_settings

    def run(
        self,
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
        nb_done = 0
        solvers = [only_solver] if only_solver else self.solvers
        for problem in self:
            if only_problem and problem.name != only_problem:
                continue
            for solver in solvers:
                for settings in self.solver_settings:
                    logging.info(
                        f"Solving {problem.name} by {solver} "
                        f"with {settings} settings..."
                    )
                    if solver == "proxqp":
                        failure = problem, solver, settings, None, 0.0
                        # https://github.com/Simple-Robotics/proxsuite/issues/62
                        if problem.name == "HUESTIS":
                            logging.warn("Skipping reported issue")
                            results.update(*failure)
                            continue
                        # other segfaults, potentially same issue as HUESTIS
                        elif problem.name in [
                            "AUG2D",
                            "AUG2DC",
                            "AUG2DCQP",
                            "AUG2DQP",
                            "BOYD2",
                            "CVXQP1_L",
                            "CVXQP2_L",
                            "CVXQP3_L",
                            "DTOC3",
                            "LISWET1",
                            "LISWET10",
                            "LISWET11",
                            "LISWET12",
                            "LISWET2",
                            "LISWET3",
                            "LISWET4",
                            "LISWET5",
                            "LISWET6",
                            "LISWET7",
                            "LISWET8",
                            "LISWET9",
                            "POWELL20",
                            "QSHIP08L",
                            "QSHIP12L",
                            "STADAT1",
                            "STADAT2",
                            "STADAT3",
                            "UBH1",
                            "YAO",
                        ]:
                            logging.warn("Skipping UNREPORTED issue")
                            results.update(*failure)
                            continue
                        # https://github.com/Simple-Robotics/proxsuite/issues/63
                        elif problem.name == "QGFRDXPN":
                            logging.warn("Skipping reported issue")
                            results.update(*failure)
                            continue
                        # other hangs (> 10 min, no solution)
                        elif problem.name in [
                            "BOYD1",
                            "CONT-100",
                            "CONT-101",
                            "CONT-200",
                            "CONT-201",
                            "CONT-300",
                            "EXDATA",
                        ]:
                            logging.warn("Skipping UNREPORTED issue")
                            results.update(*failure)
                            continue
                    elif solver == "highs":
                        failure = problem, solver, settings, None, 0.0
                        # not reported yet
                        if problem.name == "AUG2DC":
                            logging.warn("Skipping UNREPORTED issue")
                            results.update(*failure)
                            continue
                    elif solver == "cvxopt":
                        failure = problem, solver, settings, None, 0.0
                        # hangs (> 15 min), not reported yet
                        if problem.name in ["CVXQP3_L", "CONT-300"]:
                            logging.warn("Skipping UNREPORTED issue")
                            results.update(*failure)
                            continue
                    kwargs = self.solver_settings[settings][solver]
                    solution, runtime = problem.solve(solver, **kwargs)
                    results.update(
                        problem, solver, settings, solution, runtime
                    )
            nb_done += 1
        logging.info(
            f"Solved {nb_done} problems with {len(solvers)} solvers "
            f"and {len(self.solver_settings)} settings per solver"
        )
