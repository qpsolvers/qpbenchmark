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
from .shgeom import shgeom
from .spdlog import logging
from .test_set import TestSet


class Results:

    """
    Test set results.

    Attributes:
        csv_path: Path to the results CSV file.
        df: Data frame storing the results.
        test_set: Test set from which results were produced.
    """

    csv_path: str
    df: pandas.DataFrame
    test_set: TestSet

    def __init__(self, csv_path: str, test_set: TestSet):
        """
        Initialize results.

        Args:
            csv_path: Path to the results CSV file.
            test_set: Test set from which results were produced.
        """
        df = pandas.DataFrame(
            [],
            columns=[
                "problem",
                "solver",
                "settings",
                "runtime",
                "found",
                "primal_residual",
                "dual_residual",
                "duality_gap",
                "cost_error",
            ],
        ).astype(
            {
                "problem": str,
                "solver": str,
                "settings": str,
                "runtime": float,
                "found": bool,
                "primal_residual": float,
                "dual_residual": float,
                "duality_gap": float,
                "cost_error": float,
            }
        )
        if os.path.exists(csv_path):
            logging.info(f"Loading existing results from {csv_path}")
            df = pandas.concat([df, pandas.read_csv(csv_path)])
        self.csv_path = csv_path
        self.df = df
        self.test_set = test_set

    def write(self) -> None:
        """
        Write results to their CSV file for persistence.
        """
        logging.debug(f"Test set results written to {self.csv_path}")
        self.df = self.df.sort_values(by=["problem", "solver", "settings"])
        self.df.to_csv(self.csv_path, index=False)

    def has(self, problem: Problem, solver: str, settings: str) -> bool:
        """
        Check if results contain a given run of a solver on a problem.

        Args:
            problem: Test set problem.
            solver: Name of the QP solver.
            settings: Name of the corresponding solver settings.

        Returns:
            True if a result for this instance is present.
        """
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
                        "found": [not solution.is_empty],
                        "primal_residual": [solution.primal_residual()],
                        "dual_residual": [solution.dual_residual()],
                        "duality_gap": [solution.duality_gap()],
                        "cost_error": [problem.cost_error(solution)],
                    }
                ),
            ],
            ignore_index=True,
        )

    def build_success_rate_df(
        self,
        primal_tolerances: Dict[str, float],
        dual_tolerances: Dict[str, float],
        gap_tolerances: Dict[str, float],
        cost_tolerances: Dict[str, float],
    ) -> Tuple[pandas.DataFrame, pandas.DataFrame]:
        """
        Build the success-rate data frame.

        Args:
            primal_tolerances: Primal-residual tolerance for each settings.
            dual_tolerances: Dual-residual tolerance for each settings.
            gap_tolerances: Duality-gap tolerance for each settings.
            cost_tolerances: Cost tolerance for each settings.

        Returns:
            Success-rate data frames.
        """
        solvers = set(self.df["solver"].to_list())
        all_settings = set(self.df["settings"].to_list())
        df = self.df.fillna(value=np.nan)  # replace None by NaN for abs()
        found_and_valid = {
            settings: df["found"]
            & (df["primal_residual"] < primal_tolerances[settings])
            & (df["dual_residual"] < dual_tolerances[settings])
            & (df["duality_gap"] < gap_tolerances[settings])
            & (df["cost_error"].abs() < cost_tolerances[settings])
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
        return success_rate_df

    def build_correct_rate_df(
        self,
        primal_tolerances: Dict[str, float],
        dual_tolerances: Dict[str, float],
        gap_tolerances: Dict[str, float],
        cost_tolerances: Dict[str, float],
    ) -> Tuple[pandas.DataFrame, pandas.DataFrame]:
        """
        Build the correctness-rate data frame.

        Args:
            primal_tolerances: Primal-residual tolerance for each settings.
            dual_tolerances: Dual-residual tolerance for each settings.
            gap_tolerances: Duality-gap tolerance for each settings.
            cost_tolerances: Cost tolerance for each settings.

        Returns:
            Correctness-rate data frames.
        """
        solvers = set(self.df["solver"].to_list())
        all_settings = set(self.df["settings"].to_list())
        df = self.df.fillna(value=np.nan)  # replace None by NaN for abs()
        found_and_valid = {
            settings: df["found"]
            & (df["primal_residual"] < primal_tolerances[settings])
            & (df["dual_residual"] < dual_tolerances[settings])
            & (df["duality_gap"] < gap_tolerances[settings])
            & (df["cost_error"].abs() < cost_tolerances[settings])
            for settings in all_settings
        }
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
        return correctness_rate_df

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
                column_values = np.array(
                    [
                        solver_df.at[i, column]
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
