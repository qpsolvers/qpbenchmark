#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Main function of the benchmark."""

from time import perf_counter
from typing import Optional

import qpsolvers
from qpsolvers.exceptions import SolverNotFound
from tqdm import tqdm

from .results import Results
from .spdlog import logging
from .test_set import TestSet
from .utils import time_solve_problem


def run(
    test_set: TestSet,
    results: Results,
    only_problem: Optional[str] = None,
    only_settings: Optional[str] = None,
    only_solver: Optional[str] = None,
    rerun: bool = False,
    rerun_timeouts: bool = False,
    verbose: bool = False,
) -> None:
    """Run a given test set and store results.

    Args:
        test_set: Test set to run.
        results: Results instance to write to.
        only_problem: If set, only run that specific problem in the set.
        only_settings: If set, only run with these solver settings.
        only_solver: If set, only run that specific solver.
        rerun: If set, rerun instances that already have a result.
        rerun_timeouts: If set, also rerun known timeouts.
        verbose: If set, log info messages for each QP solver call.
    """
    if only_settings and only_settings not in test_set.solver_settings:
        raise ValueError(
            f"settings '{only_settings}' not in the list of settings "
            f"for this test set: {list(test_set.solver_settings.keys())}"
        )
    if only_solver and only_solver not in test_set.solvers:
        raise SolverNotFound(
            f"solver '{only_solver}' not in the list of "
            f"available solvers for this test set: {test_set.solvers}"
        )

    filtered_solvers = [
        solver
        for solver in test_set.solvers
        if only_solver is None or solver == only_solver
    ]
    filtered_settings = [
        settings
        for settings in test_set.solver_settings
        if only_settings is None or settings == only_settings
    ]

    nb_calls = 0
    nb_calls_since_last_save = 0
    start_counter = perf_counter()
    last_save = perf_counter()

    progress_bar = None
    if not verbose:
        nb_problems = 1 if only_problem else test_set.count_problems()
        nb_solvers = len(filtered_solvers)
        nb_settings = len(filtered_settings)
        progress_bar = tqdm(
            total=nb_problems * nb_solvers * nb_settings,
            initial=0,
        )

    for problem in test_set:
        if only_problem and problem.name != only_problem:
            continue
        for solver in filtered_solvers:
            for settings in filtered_settings:
                time_limit = test_set.tolerances[settings].runtime
                if results.has(problem, solver, settings):
                    if not rerun:
                        logging.debug(
                            f"{problem.name} already solved by {solver} "
                            f"with {settings} settings..."
                        )
                        if progress_bar is not None:
                            # We don't count existing results beforehand
                            progress_bar.update(1)
                        continue
                    if not rerun_timeouts and results.is_timeout(
                        problem, solver, settings, time_limit
                    ):
                        logging.info(
                            f"Skipping {problem.name} with {solver} and "
                            f"{settings} settings as a previous timeout..."
                        )
                        if progress_bar is not None:
                            # We don't count existing results beforehand
                            progress_bar.update(1)
                        continue
                if test_set.skip_solver_issue(problem, solver):
                    failure = (
                        problem,
                        solver,
                        settings,
                        qpsolvers.Solution(problem),
                        0.0,
                    )
                    results.update(*failure)
                    if progress_bar is not None:
                        progress_bar.update(1)
                    continue
                if test_set.skip_solver_timeout(
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
                    if progress_bar is not None:
                        progress_bar.update(1)
                    continue
                if verbose:
                    logging.info(
                        f"Solving {problem.name} by {solver} "
                        f"with {settings} settings..."
                    )
                kwargs = test_set.solver_settings[settings][solver]
                solution, runtime = time_solve_problem(
                    problem, solver, **kwargs
                )
                nb_calls += 1
                nb_calls_since_last_save += 1
                results.update(problem, solver, settings, solution, runtime)
                if progress_bar is not None:
                    progress_bar.update(1)

        # Save results to file after problem has been fully processed
        if perf_counter() - last_save > 10.0 and nb_calls_since_last_save > 0:
            results.write()
            last_save = perf_counter()
            nb_calls_since_last_save = 0

    duration = perf_counter() - start_counter
    logging.info(f"Ran the test set in {duration:.0f} seconds")
    logging.info(f"Made {nb_calls} QP solver calls")
    if progress_bar is not None:
        progress_bar.close()
