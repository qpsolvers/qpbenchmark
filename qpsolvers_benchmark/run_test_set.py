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
Run a given test set.
"""

from typing import Any, Dict, Optional

from .results import Results
from .test_sets import TestSet


def run_test_set(
    test_set: TestSet,
    solver_settings: Dict[str, Dict[str, Any]],
    results: Results,
    only_problem: Optional[str] = None,
    only_solver: Optional[str] = None,
) -> None:
    """
    Run a given test set.

    Args:
        test_set: Test set to run.
        solver_settings: Keyword arguments for each solver.
        results: Results instance to write to.
        only_problem: If set, only run that specific problem in the test set.
        only_solver: If set, only run that specific solver.
    """
    problem_number = 1
    if only_solver:
        solver_settings = {only_solver: solver_settings[only_solver]}
    for problem in test_set:
        if only_problem and problem.name != only_problem:
            continue
        for solver, settings in solver_settings.items():
            print(f"Running problem {problem.name} with {solver}...")
            solution, duration_us = problem.solve(solver=solver, **settings)
            results.update(problem, solver, solution, duration_us)
        problem_number += 1
        if problem_number > 5:
            break
