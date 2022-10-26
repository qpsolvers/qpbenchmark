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

import yaml
from qpsolvers import available_solvers

from qpsolvers_benchmark import Problem, Report, Results, Validator


def list_mat_files(data_dir):
    for fname in os.listdir(data_dir):
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

    results = Results("results/data.csv")

    mm_dir = os.path.join(os.path.dirname(__file__), "data", "maros_meszaros")
    with open(os.path.join(mm_dir, "OPTCOSTS.yaml"), "r") as fh:
        file_dict = yaml.load(fh)
        optimal_costs = {key: float(value) for key, value in file_dict.items()}

    problem_number = 1
    for solver in solvers:
        for fname in list_mat_files(mm_dir):
            problem_name = os.path.basename(fname)[:-4]
            print(
                f"Running problem #{problem_number} ({problem_name}) "
                f"with {solver}..."
            )
            problem = Problem.from_mat_file(fname)
            if problem.name in optimal_costs:
                problem.optimal_cost = optimal_costs[problem.name]
            solution = problem.solve(solver=solver, **solver_settings[solver])
            results.update(problem, solver, solution)
            problem_number += 1
            if problem_number > 5:
                break

    results.write()
    report = Report(validator)
    report.write(results, "results/README.md")
