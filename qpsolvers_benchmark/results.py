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
from typing import Dict, Tuple

import numpy as np
import pandas
import qpsolvers

from .problem import Problem
from .spdlog import logging
from .utils import shgeom


class Results:

    """
    Test case results.
    """

    def __init__(self, csv_path: str):
        """
        Initialize results.

        Args:
            csv_path: Path to the results CSV file.
        """
        df = pandas.DataFrame(
            [],
            columns=[
                "problem",
                "solver",
                "settings",
                "runtime",
                "found",
                "cost_error",
                "primal_residual",
                "dual_residual",
                "duality_gap",
            ],
        )
        if os.path.exists(csv_path):
            logging.info(f"Loading existing results from {csv_path}")
            df = pandas.concat([df, pandas.read_csv(csv_path)])
        self.csv_path = csv_path
        self.df = df

    def write(self) -> None:
        """
        Write results to their CSV file for persistence.
        """
        logging.debug(f"Test set results written to {self.csv_path}")
        self.df = self.df.sort_values(by=["problem", "solver", "settings"])
        self.df.to_csv(self.csv_path, index=False)

    def has(self, problem: Problem, solver: str, settings: str) -> bool:
        return (
            (self.df["problem"] == problem.name)
            & (self.df["solver"] == solver)
            & (self.df["settings"] == settings)
        ).any()

    def is_timeout(
        self, problem: Problem, solver: str, settings: str, time_limit: float
    ) -> bool:
        """
        Check whether a particular result was a timeout.
        """
        runtime = self.df[
            (self.df["problem"] == problem.name)
            & (self.df["solver"] == solver)
            & (self.df["settings"] == settings)
        ]["runtime"].iat[0]
        return runtime > 0.99 * time_limit

    def update(
        self,
        problem: Problem,
        solver: str,
        settings: str,
        solution: qpsolvers.Solution,
        runtime: float,
    ) -> None:
        """
        Update entry for a given (problem, solver) pair.

        Args:
            problem: Problem solved.
            solver: Solver name.
            settings: Solver settings.
            solution: Solution found by the solver.
            runtime: Duration the solver took, in seconds.
        """
        self.df = self.df.drop(
            self.df.index[
                (self.df["problem"] == problem.name)
                & (self.df["solver"] == solver)
                & (self.df["settings"] == settings)
            ]
        )
        self.df = pandas.concat(
            [
                self.df,
                pandas.DataFrame(
                    {
                        "problem": [problem.name],
                        "solver": [solver],
                        "settings": [settings],
                        "runtime": [runtime],
                        "found": [solution is not None],
                        "cost_error": [problem.cost_error(solution)],
                        "primal_residual": [solution.primal_residual()],
                        "dual_residual": [solution.dual_residual()],
                        "duality_gap": [solution.duality_gap()],
                    }
                ),
            ],
            ignore_index=True,
        )

    def build_success_frames(
        self,
        cost_tolerances: Dict[str, float],
        primal_tolerances: Dict[str, float],
    ) -> Tuple[pandas.DataFrame, pandas.DataFrame]:
        """
        Build the success-rate and correctness-rate data frames.

        Args:
            cost_tolerances: Cost tolerance for each settings.
            primal_tolerances: Primal tolerance for each settings.

        Returns:
            Success-rate and correctness-rate data frames.
        """
        solvers = set(self.df["solver"].to_list())
        all_settings = set(self.df["settings"].to_list())
        df = self.df.fillna(value=np.nan)  # replace None by NaN for abs()
        found_and_valid = {
            settings: df["found"]
            & (df["cost_error"].abs() < cost_tolerances[settings])
            & (df["primal_error"] < primal_tolerances[settings])
            for settings in all_settings
        }
        success_rate_df = (
            pandas.DataFrame(
                {
                    settings: {
                        solver: 100.0
                        * found_and_valid[settings][
                            (df["settings"] == settings)
                            & (df["solver"] == solver)
                        ]
                        .astype(float)
                        .mean()
                        for solver in solvers
                    }
                    for settings in all_settings
                }
            )
            .reindex(columns=sorted(all_settings))
            .sort_index()
        )
        correctness_rate_df = (
            pandas.DataFrame(
                {
                    settings: {
                        solver: 100.0
                        * (
                            df[
                                (df["settings"] == settings)
                                & (df["solver"] == solver)
                            ]["found"]
                            == found_and_valid[settings][
                                (df["settings"] == settings)
                                & (df["solver"] == solver)
                            ]
                        )
                        .astype(float)
                        .mean()
                        for solver in solvers
                    }
                    for settings in all_settings
                }
            )
            .reindex(columns=sorted(all_settings))
            .sort_index()
        )
        return success_rate_df, correctness_rate_df

    def build_shifted_geometric_mean_df(
        self, column: str, shift: float, not_found_values: Dict[str, float]
    ) -> pandas.DataFrame:
        """
        Compute the shifted geometric mean of a results column.

        Args:
            column: Name of the column to average.
            shift: Shift of the shifted geometric mean.
            not_found_values: Values to apply when a solver has not found a
                solution (one per settings). For instance, time limits are used
                for the runtime of a solver that fails to solve a problem.

        Returns:
            Shifted geometric mean of the prescribed column.
        """
        solvers = set(self.df["solver"].to_list())
        all_settings = set(self.df["settings"].to_list())

        def mean_for_settings(settings):
            means = {}
            for solver in solvers:
                solver_df = self.df[
                    (self.df["solver"] == solver)
                    & (self.df["settings"] == settings)
                ]
                # Cost errors can be negative because of primal errors. We
                # count that as errors as well using absolute values.
                column_values = np.array(
                    [
                        abs(solver_df.at[i, column])  # abs() for cost error
                        if solver_df.at[i, "found"]
                        else not_found_values[settings]
                        for i in solver_df.index
                    ]
                )
                means[solver] = shgeom(column_values, shift)
            best_mean = np.min(list(means.values()))
            return {solver: means[solver] / best_mean for solver in solvers}

        return (
            pandas.DataFrame(
                {
                    settings: mean_for_settings(settings)
                    for settings in all_settings
                }
            )
            .reindex(columns=sorted(all_settings))
            .sort_index()
        )
