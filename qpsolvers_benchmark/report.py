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
Report written from test set results.
"""

import datetime
from importlib import metadata

import pandas

from .results import Results
from .spdlog import logging
from .test_set import TestSet
from .utils import get_cpu_info, get_solver_versions


class Report:

    author: str
    cpu_info: str
    date: str
    results: Results
    test_set: TestSet

    def __init__(
        self,
        author: str,
        test_set: TestSet,
        results: Results,
    ):
        cpu_info = get_cpu_info()
        date = str(datetime.datetime.now(datetime.timezone.utc))
        self.author = author
        self.cpu_info = cpu_info
        self.date = date
        self.results = results
        self.solver_settings = test_set.solver_settings
        self.test_set = test_set

    def get_tolerances_table(self):
        names = list(self.solver_settings.keys())
        df = pandas.DataFrame(
            [],
            columns=["tolerance"] + names,
        )
        tolerances = ["cost_tolerance", "primal_tolerance", "time_limit"]
        for tolerance in tolerances:
            row = {
                "tolerance": [f"``{tolerance}``"],
            }
            row.update(
                {
                    name: [self.solver_settings[name].__dict__[tolerance]]
                    for name in names
                }
            )
            df = pandas.concat(
                [
                    df,
                    pandas.DataFrame(row),
                ],
                ignore_index=True,
            )
        df = df.sort_values(by="tolerance")
        return df.to_markdown(index=False)

    def get_solver_settings_table(self):
        solver_settings = self.test_set.solver_settings
        names = list(solver_settings.keys())
        df = pandas.DataFrame(
            [],
            columns=["solver", "parameter"] + names,
        )
        keys = set()
        for name, settings in solver_settings.items():
            for solver in settings.solvers:
                if solver not in self.test_set.solvers:
                    # Skip solvers that are configured but not in test set
                    continue
                for param in settings[solver]:
                    keys |= {(solver, param)}
        for solver, param in keys:
            row = {
                "solver": [solver],
                "parameter": [f"``{param}``"],
            }
            row.update(
                {
                    name: [solver_settings[name].get_param(solver, param, "-")]
                    for name in names
                }
            )
            df = pandas.concat(
                [
                    df,
                    pandas.DataFrame(row),
                ],
                ignore_index=True,
            )
        df = df.sort_values(by=["solver", "parameter"])
        return df.to_markdown(index=False)

    def get_solver_versions_table(self):
        versions = get_solver_versions(self.test_set.solvers)
        versions_df = pandas.DataFrame(
            {
                "solver": list(versions.keys()),
                "version": list(versions.values()),
            },
        )
        versions_df = versions_df.set_index("solver")
        versions_df = versions_df.sort_index()
        versions_table = versions_df.to_markdown(index=True)
        return versions_table

    def write(self, path: str) -> None:
        qpsolvers_version = metadata.version("qpsolvers")
        cost_tolerances = {
            name: settings.cost_tolerance
            for name, settings in self.solver_settings.items()
        }
        primal_tolerances = {
            name: settings.primal_tolerance
            for name, settings in self.solver_settings.items()
        }
        time_limits = {
            name: settings.time_limit
            for name, settings in self.solver_settings.items()
        }
        success_rate_df, correct_rate_df = self.results.build_success_frames(
            self.test_set.cost_tolerance, self.test_set.primal_tolerance
        )
        success_rate_table = success_rate_df.to_markdown(
            index=True, floatfmt=".0f"
        )
        correct_rate_table = correct_rate_df.to_markdown(
            index=True, floatfmt=".0f"
        )
        settings_names = [f"``{x}``" for x in self.solver_settings]
        with open(path, "w") as fh:
            fh.write(
                f"""# {self.test_set.title}

- Author: [@{self.author}](https://github.com/{self.author}/)
- CPU: {self.cpu_info}
- Date: {self.date}

## Solvers

{self.get_solver_versions_table()}

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v{qpsolvers_version}.

## Settings

There are {len(settings_names)} settings: {", ".join(settings_names[:-1])} and
{settings_names[-1]}. They validate solutions using the following tolerances:

{self.get_tolerances_table()}

Solvers for each group of settings are configured as follows:

{self.get_solver_settings_table()}

## Metrics

We look at the following statistics:

- [Success rate](#success-rate)
- [Computation time](#computation-time)
- [Primal error](#primal-error)
- [Cost error](#cost-error)

They are presented in more detail in [Metrics](../README.md#metrics).

## Results

### Success rate

Precentage of problems each solver is able to solve:

{success_rate_table}

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). Here is a summary of the frequency at which solvers
returned success (1) but the corresponding solution did not pass tolerance
checks:

{solve_is_success_table}

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

{self.results.build_shifted_geometric_mean_df(
    column="runtime",
    shift=10.0,
    not_found_value=self.test_set.time_limit,
).to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal errors over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal error of Y is Y times less precise
on constraints than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver primal errors (1.0 is the best):

{self.results.build_shifted_geometric_mean_df(
    column="primal_error",
    shift=10.0,
    not_found_value=self.test_set.primal_tolerance,
).to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal tolerance](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

{self.results.build_shifted_geometric_mean_df(
    column="cost_error",
    shift=10.0,
    not_found_value=self.test_set.cost_tolerance,
).to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
"""
            )
        logging.info(f"Wrote report to {path}")
