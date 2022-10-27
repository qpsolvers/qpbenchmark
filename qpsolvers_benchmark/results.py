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
Benchmark results.
"""

import os.path

import pandas

from .problem import Problem


class Results:
    def __init__(self, csv_path: str):
        df = pandas.DataFrame(
            [],
            columns=[
                "problem",
                "solver",
                "duration_us",
                "found",
                "cost_error",
                "primal_error",
            ],
        )
        if os.path.exists(csv_path):
            df = pandas.concat([df, pandas.read_csv(csv_path)])
        self.__df = df
        self.csv_path = csv_path
        self.__found = {}

    def write(self):
        self.__df.to_csv(self.csv_path, index=False)

    def update(
        self, problem: Problem, solver: str, solution, duration_us: float
    ):
        found = solution is not None
        self.update_found(problem.name, solver, found)
        self.__df = self.__df.drop(
            self.__df.index[
                (self.__df["problem"] == problem.name)
                & (self.__df["solver"] == solver)
            ]
        )
        self.__df = pandas.concat(
            [
                self.__df,
                pandas.DataFrame(
                    {
                        "problem": [problem.name],
                        "solver": [solver],
                        "duration_us": [duration_us],
                        "found": [solution is not None],
                        "cost_error": [problem.cost_error(solution)],
                        "primal_error": [problem.primal_error(solution)],
                    }
                ),
            ],
            ignore_index=True,
        )

    def update_found(self, problem: str, solver: str, found: bool):
        if solver not in self.__found:
            self.__found[solver] = {}
        if problem not in self.__found[solver]:
            self.__found[solver][problem] = []
        self.__found[solver][problem].append(found)

    @property
    def found_df(self):
        found_summary = {
            solver: {
                problem: [all(outcomes)]
                for problem, outcomes in self.__found[solver].items()
            }
            for solver in self.__found
        }
        return pandas.DataFrame.from_dict(found_summary)
