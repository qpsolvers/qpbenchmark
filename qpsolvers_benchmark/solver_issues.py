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
    if solver == "proxqp":
        # https://github.com/Simple-Robotics/proxsuite/issues/62
        if problem.name == "HUESTIS":
            return True
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
            logging.warning("Skipping UNREPORTED issue")
            return True
        # https://github.com/Simple-Robotics/proxsuite/issues/63
        elif problem.name == "QGFRDXPN":
            return True
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
            logging.warning("Skipping UNREPORTED issue")
            return True
    elif solver == "highs":
        if problem.name == "STADAT1":
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
        ("CONT-300", "cvxopt", "default"): 20 * minutes,
        ("CONT-300", "cvxopt", "high_accuracy"): 20 * minutes,
        ("CONT-300", "highs", "default"): 30 * minutes,
        ("CONT-300", "highs", "high_accuracy"): 30 * minutes,
        ("CVXQP3_L", "cvxopt", "default"): 20 * minutes,
        ("CVXQP3_L", "cvxopt", "high_accuracy"): 20 * minutes,
    }
    if (problem.name, solver, settings) in known_timeout_settings:
        timeout = known_timeout_settings[(problem.name, solver, settings)]
        logging.warning(
            f"Problem {problem.name} with {solver} and settings {settings} "
            "is known to take more than 1000 seconds..."
        )
        return timeout > time_limit
    return False
