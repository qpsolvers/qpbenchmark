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

from qpsolvers_benchmark import Report, Results, SolverSettings
from qpsolvers_benchmark.test_sets import MarosMeszaros


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description="Benchmark quadratic programming solvers"
    )
    parser.add_argument(
        "--problem",
        "-p",
        help="Limit tests to a specific problem",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        default=False,
        help="Only write the output report from saved test set results",
    )
    parser.add_argument(
        "--solver",
        "-s",
        help="Limit tests to a specific solver",
    )
    parser.add_argument(
        "--test-set",
        choices=["maros_meszaros"],
        default="maros_meszaros",
        help="Test set to run",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Turn on verbose solver outputs",
    )
    parser.add_argument
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line_arguments()

    data_dir = os.path.join(os.path.dirname(__file__), "data")
    test_set = MarosMeszaros(
        data_dir=os.path.join(data_dir, args.test_set),
    )

    solver_settings = {
        "default": SolverSettings(
            time_limit=test_set.time_limit, verbose=args.verbose
        ),
        # "low_accuracy": SolverSettings(
        #     time_limit=test_set.time_limit,
        #     eps_abs=1e-3,
        #     eps_rel=0.0,
        # ),
        # "high_accuracy": SolverSettings(
        #     time_limit=test_set.time_limit,
        #     eps_abs=1e-8,
        #     eps_rel=0.0,
        # ),
    }

    results_dir = os.path.join(os.path.dirname(__file__), "results")
    results = Results(os.path.join(results_dir, f"{args.test_set}.csv"))

    if not args.report_only:
        test_set.run(
            solver_settings,
            results,
            only_problem=args.problem,
            only_solver=args.solver,
        )
        results.write()

    report = Report(test_set, solver_settings, results)
    report.write(os.path.join(results_dir, f"{args.test_set}.md"))
