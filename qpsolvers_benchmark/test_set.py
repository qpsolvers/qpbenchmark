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
import os.path
from typing import Any, Dict, Iterator, Optional

from qpsolvers import sparse_solvers

from .problem import Problem
from .results import Results


class TestSet(abc.ABC):

    results: Results

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Problem]:
        """
        Yield test problems one by one.
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

    @abc.abstractmethod
    def write_report(self) -> None:
        """
        Write report files to results directory.
        """

    def __init__(self, data_dir: str, results_dir: str):
        results = Results(os.path.join(results_dir, f"{self.name}.csv"))
        self.results = results
        self.results_dir = results_dir

    @property
    def report_path(self) -> str:
        return os.path.join(self.results_dir, f"{self.name}.md")

    def run(
        self,
        solver_settings: Dict[str, Dict[str, Any]],
        only_problem: Optional[str] = None,
        only_solver: Optional[str] = None,
    ) -> None:
        """
        Run test set.

        Args:
            solver_settings: Keyword arguments for each solver.
            only_problem: If set, only run that specific problem in the set.
            only_solver: If set, only run that specific solver.
        """
        problem_number = 1
        if self.sparse_only:
            solver_settings = {
                solver: solver_settings[solver] for solver in sparse_solvers
            }
        if only_solver:
            solver_settings = {only_solver: solver_settings[only_solver]}
        for problem in self:
            if only_problem and problem.name != only_problem:
                continue
            for solver, settings in solver_settings.items():
                print(f"Running problem {problem.name} with {solver}...")
                solution, duration_us = problem.solve(
                    solver=solver, **settings
                )
                self.results.update(problem, solver, solution, duration_us)
            problem_number += 1
            if problem_number > 1:
                break

    def write_results(self) -> None:
        """
        Write persistent results to a CSV file in the results directory.
        """
        self.results.write()
