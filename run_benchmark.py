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

from qpsolvers_benchmark import Problem, Report, Validator


def maros_meszaros_files():
    mm_dir = os.path.join(os.path.dirname(__file__), "data", "maros_meszaros")
    for fname in os.listdir(mm_dir):
        if fname.endswith(".mat"):
            yield os.path.join(mm_dir, fname)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Benchmark quadratic programming solvers"
    )
    parser.add_argument(
        "--solver",
        "-s",
        help="Only test a specific solver",
    )
    args = parser.parse_args()

    solvers = [args.solver] if args.solver is not None else available_solvers

    validator = Validator(eps_abs=1e-5)
    solver_settings = {"osqp": {"eps_abs": 1e-5, "eps_rel": 0.0}}

    report = Report("results/README.md", validator)
    report.start()

    problem_number = 1
    for solver in solvers:
        for fname in maros_meszaros_files():
            problem_name = os.path.basename(fname)[:-4]
            print(
                f"Running problem #{problem_number} ({problem_name}) "
                f"with {solver}..."
            )
            problem = Problem.from_mat_file(fname)
            solution = problem.solve(solver=solver, **solver_settings[solver])
            report.append_result(problem, solver, solution)
            problem_number += 1
            if problem_number > 5:
                pass

    report.finalize()
