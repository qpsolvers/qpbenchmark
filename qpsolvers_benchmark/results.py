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
Test case results.
"""

import os.path

import numpy as np
import pandas

from .problem import Problem
from .utils import shgeom


class Results:

    """
    Test case results.
    """

    def __init__(self, csv_path: str):
        """
        Initialize results.

        Args:
            csv_path: Persistent CSV file to load previous results from.
        """
        df = pandas.DataFrame(
            [],
            columns=[
                "problem",
                "solver",
                "duration",
                "found",
                "cost_error",
                "primal_error",
            ],
        )
        if os.path.exists(csv_path):
            df = pandas.concat([df, pandas.read_csv(csv_path)])
        self.df = df
        self.csv_path = csv_path
        self.__found_df = None

    def write(self) -> None:
        """
        Write results to their CSV file for persistence.
        """
        self.df.to_csv(self.csv_path, index=False)

    def update(
        self, problem: Problem, solver: str, solution, duration: float
    ) -> None:
        """
        Update entry for a given (problem, solver) pair.

        Args:
            problem: Problem solved.
            solver: Solver name.
            solution: Solution found by the solver.
            runtime: Duration the solver took, in seconds.
        """
        self.df = self.df.drop(
            self.df.index[
                (self.df["problem"] == problem.name)
                & (self.df["solver"] == solver)
            ]
        )
        self.df = pandas.concat(
            [
                self.df,
                pandas.DataFrame(
                    {
                        "problem": [problem.name],
                        "solver": [solver],
                        "duration": [duration],
                        "found": [solution is not None],
                        "cost_error": [problem.cost_error(solution)],
                        "primal_error": [problem.primal_error(solution)],
                    }
                ),
            ],
            ignore_index=True,
        )

    def build_found_df(self) -> pandas.DataFrame:
        """
        Build the (solver, problem) found table.

        Returns:
            Found table data frame.
        """
        problems = set(self.df["problem"].to_list())
        solvers = set(self.df["solver"].to_list())
        found = {
            solver: {problem: None for problem in problems}
            for solver in solvers
        }
        for row in self.df.to_dict(orient="records"):
            found[row["solver"]][row["problem"]] = row["found"]
        self.__found_df = pandas.DataFrame.from_dict(found)
        return self.__found_df

    def build_success_rate_df(self) -> pandas.DataFrame:
        found_df = self.__found_df
        solvers = list(found_df)
        # problems = found_df.index.tolist()
        return pandas.DataFrame(
            {
                "Success rate (%)": {
                    solver: 100.0 * found_df[solver].astype(float).mean()
                    for solver in solvers
                }
            }
        )

    def build_geometric_mean_df(self, time_limit=10.0) -> pandas.DataFrame:
        solvers = set(self.df["solver"].to_list())
        means = {solver: 1e20 for solver in solvers}
        for solver in solvers:
            solver_df = self.df[self.df["solver"] == solver]
            durations = np.array(
                [
                    solver_df.at[i, "duration"]
                    if solver_df.at[i, "found"]
                    else time_limit
                    for i in solver_df.index
                ]
            )
            means[solver] = shgeom(durations)
        best_mean = np.min(list(means.values()))
        label = "Shifted geometric mean"
        mean_df = pandas.DataFrame(
            {
                label: {
                    solver: means[solver] / best_mean for solver in solvers
                }
            }
        )
        return mean_df.sort_values(by=label)
