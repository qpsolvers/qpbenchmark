#!/usr/bin/env python
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

import argparse
import os

import IPython

from qpsolvers_benchmark import Report, Results, SolverSettings
from qpsolvers_benchmark.spdlog import logging
from qpsolvers_benchmark.test_sets import MarosMeszaros, MarosMeszarosDense


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description="Benchmark quadratic programming solvers"
    )
    parser.add_argument(
        "command",
        choices=["run", "eval", "report"],
        help="Run test set? Evaluate its results? Write its report?",
    )
    parser.add_argument(
        "test_set",
        choices=["maros_meszaros", "maros_meszaros_dense"],
        help="Test set to execute command on",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Turn on verbose solver outputs",
    )

    # Filtering
    parser.add_argument(
        "--problem",
        help="Limit tests to a specific problem",
    )
    parser.add_argument(
        "--settings",
        help="Limit tests to a specific group of solver settings",
    )
    parser.add_argument(
        "--solver",
        help="Limit tests to a specific solver",
    )

    # Rerun
    parser.add_argument(
        "--rerun",
        default=False,
        action="store_true",
        help="Rerun test set even on problems with a saved result",
    )
    parser.add_argument(
        "--include-timeouts",
        default=False,
        action="store_true",
        help="Also include timeouts when re-running test set",
    )

    parser.add_argument
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line_arguments()

    data_dir = os.path.join(os.path.dirname(__file__), "data")

    TestClass = {
        "maros_meszaros": MarosMeszaros,
        "maros_meszaros_dense": MarosMeszarosDense,
    }[args.test_set]
    test_set = TestClass(data_dir=os.path.join(data_dir))

    solver_settings = {
        "default": SolverSettings(
            time_limit=test_set.time_limit,
            verbose=args.verbose,
        ),
        "high_accuracy": SolverSettings(
            time_limit=test_set.time_limit,
            absolute_tolerance=1e-9,
            verbose=args.verbose,
        ),
    }

    results_dir = os.path.join(os.path.dirname(__file__), "results")
    results = Results(os.path.join(results_dir, f"{args.test_set}.csv"))

    if args.command == "run":
        test_set.run(
            solver_settings,
            results,
            only_problem=args.problem,
            only_settings=args.settings,
            only_solver=args.solver,
            rerun=args.rerun,
            include_timeouts=args.include_timeouts,
        )
        results.write()

    if args.command == "eval":
        df = results.df
        logging.info("Check out `results` and the pandas DataFrame `df`")
        if not IPython.get_ipython():
            IPython.embed()

    if args.command in ["report", "run"]:
        report = Report(test_set, solver_settings, results)
        report.write(os.path.join(results_dir, f"{args.test_set}.md"))
