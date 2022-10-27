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

from qpsolvers import available_solvers

from qpsolvers_benchmark import Report, Results, Validator, run_test_set
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
        "--solver",
        "-s",
        help="Limit tests to a specific solver",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line_arguments()
    solver_settings = {solver: {} for solver in available_solvers}

    # Time limit
    solver_settings["highs"]["time_limit"] = 10.0

    validator = Validator(eps_abs=1e-5)
    solver_settings["osqp"] = {"eps_abs": 1e-5, "eps_rel": 0.0}

    test_set = MarosMeszaros(
        data_dir=os.path.join(
            os.path.dirname(__file__), "data", "maros_meszaros"
        )
    )

    results = Results(f"results/{test_set.name}.csv")
    run_test_set(
        test_set,
        solver_settings,
        results,
        only_problem=args.problem,
        only_solver=args.solver,
    )
    results.write()

    report = Report(validator)
    report.title(test_set.title)
    report.write(results, f"results/{test_set.name}.md")
