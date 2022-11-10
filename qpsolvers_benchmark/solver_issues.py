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
Some solvers fail on some problems. Make sure we handle and report those.
"""

from .problem import Problem
from .spdlog import logging


def skip_solver_issue(problem: Problem, solver: str) -> bool:
    """
    Check whether a solver is known to fail at solving a given problem.

    Args:
        problem: Problem to solve.
        solver: QP solver.

    Returns:
        True if solver is known to fail at solving the problem.
    """
    if solver == "proxqp" and problem.name == "QGFRDXPN":
        # https://github.com/Simple-Robotics/proxsuite/issues/63
        return True
    elif solver == "highs" and problem.name == "STADAT1":
        # https://github.com/ERGO-Code/HiGHS/issues/995
        return True
    return False


def skip_solver_timeout(
    time_limit: float, problem: Problem, solver: str, settings: str
) -> bool:
    """
    Skip known solver timeouts.

    Args:
        time_limit: Time limit in seconds.
        problem: Problem to solve.
        solver: QP solver.

    Note:
        This function only checks for timeouts that the solvers are not able to
        handle by themselves, e.g. for those who provide a time limit
        parameter.

    Returns:
        True if `solver` is known to take more than `time_limit` seconds on
        `problem`.
    """
    minutes = 60.0
    known_timeout_settings = {
        ("AUG2D", "highs", "default"): 40 * minutes,
        ("AUG2D", "highs", "high_accuracy"): 40 * minutes,
        ("AUG2DC", "highs", "default"): 40 * minutes,
        ("AUG2DC", "highs", "high_accuracy"): 40 * minutes,
        ("BOYD1", "proxqp", "default"): 30 * minutes,
        ("BOYD1", "proxqp", "high_accuracy"): 30 * minutes,
        ("BOYD2", "proxqp", "default"): 20 * minutes,
        ("BOYD2", "proxqp", "high_accuracy"): 20 * minutes,
        ("CONT-101", "proxqp", "default"): 30 * minutes,
        ("CONT-101", "proxqp", "high_accuracy"): 30 * minutes,
        ("CONT-200", "proxqp", "default"): 20 * minutes,
        ("CONT-200", "proxqp", "high_accuracy"): 20 * minutes,
        ("CONT-201", "proxqp", "default"): 30 * minutes,
        ("CONT-201", "proxqp", "high_accuracy"): 30 * minutes,
        ("CONT-300", "cvxopt", "default"): 20 * minutes,
        ("CONT-300", "cvxopt", "high_accuracy"): 20 * minutes,
        ("CONT-300", "highs", "default"): 30 * minutes,
        ("CONT-300", "highs", "high_accuracy"): 30 * minutes,
        ("CONT-300", "proxqp", "default"): 60 * minutes,
        ("CONT-300", "proxqp", "high_accuracy"): 60 * minutes,
        ("CVXQP1_L", "proxqp", "default"): 20 * minutes,
        ("CVXQP1_L", "proxqp", "high_accuracy"): 20 * minutes,
        ("CVXQP3_L", "cvxopt", "default"): 20 * minutes,
        ("CVXQP3_L", "cvxopt", "high_accuracy"): 20 * minutes,
        ("CVXQP3_L", "proxqp", "default"): 30 * minutes,
        ("CVXQP3_L", "proxqp", "high_accuracy"): 30 * minutes,
        ("EXDATA", "proxqp", "default"): 30 * minutes,
        ("EXDATA", "proxqp", "high_accuracy"): 30 * minutes,
        ("LISWET1", "proxqp", "default"): 20 * minutes,
        ("LISWET1", "proxqp", "high_accuracy"): 20 * minutes,
        ("LISWET10", "proxqp", "default"): 50 * minutes,
        ("LISWET10", "proxqp", "high_accuracy"): 50 * minutes,
        ("LISWET11", "proxqp", "high_accuracy"): 40 * minutes,
        ("LISWET12", "proxqp", "high_accuracy"): 20 * minutes,
        ("LISWET2", "proxqp", "high_accuracy"): 20 * minutes,
        ("LISWET3", "proxqp", "high_accuracy"): 20 * minutes,
        ("LISWET4", "proxqp", "high_accuracy"): 20 * minutes,
        ("LISWET5", "proxqp", "high_accuracy"): 20 * minutes,
        ("LISWET6", "proxqp", "high_accuracy"): 20 * minutes,
        ("LISWET7", "proxqp", "high_accuracy"): 30 * minutes,
        ("LISWET8", "proxqp", "high_accuracy"): 30 * minutes,
        ("LISWET9", "proxqp", "high_accuracy"): 30 * minutes,
        ("POWELL20", "proxqp", "default"): 30 * minutes,
        ("POWELL20", "proxqp", "high_accuracy"): 30 * minutes,
        ("QSHIP08L", "proxqp", "default"): 20 * minutes,
        ("QSHIP08L", "proxqp", "high_accuracy"): 20 * minutes,
        ("QSHIP12L", "proxqp", "default"): 20 * minutes,
        ("QSHIP12L", "proxqp", "high_accuracy"): 20 * minutes,
        ("QGFRDXPN", "proxqp", "default"): 20 * minutes,
        ("QGFRDXPN", "proxqp", "high_accuracy"): 20 * minutes,
        ("STADAT1", "proxqp", "default"): 20 * minutes,
        ("STADAT1", "proxqp", "high_accuracy"): 20 * minutes,
        ("STADAT2", "proxqp", "default"): 20 * minutes,
        ("STADAT2", "proxqp", "high_accuracy"): 20 * minutes,
        ("STADAT3", "proxqp", "default"): 20 * minutes,
        ("STADAT3", "proxqp", "high_accuracy"): 20 * minutes,
        ("UBH1", "proxqp", "default"): 20 * minutes,
        ("UBH1", "proxqp", "high_accuracy"): 20 * minutes,
        ("YAO", "proxqp", "default"): 20 * minutes,
        ("YAO", "proxqp", "high_accuracy"): 20 * minutes,
    }
    if (problem.name, solver, settings) in known_timeout_settings:
        timeout = known_timeout_settings[(problem.name, solver, settings)]
        if timeout > time_limit:
            logging.warning(
                f"Skipping {problem.name} with {solver} at {settings} "
                f"as it is known to take {timeout} > {time_limit} seconds..."
            )
            return True
    return False
