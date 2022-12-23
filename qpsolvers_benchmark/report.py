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
        names = list(self.test_set.tolerances.keys())
        df = pandas.DataFrame(
            [],
            columns=["tolerance"] + names,
        )
        tolerances = ["cost", "primal", "dual", "gap", "runtime"]
        for tolerance in tolerances:
            row = {
                "tolerance": [f"``{tolerance}``"],
            }
            row.update(
                {
                    name: [self.test_set.tolerances[name].__dict__[tolerance]]
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
        """
        Write report to a given path.

        Args:
            path: Path to the Markdown file to write the report to.

        Note:
            We make sure each table in the report is preceded by a single line
            title, for instance "Precentage of problems each solver is able to
            solve:". This comes in handy for ``@@`` anchorage when doing the
            ``diff`` of two reports.
        """
        assert path.endswith(".md")
        qpsolvers_version = metadata.version("qpsolvers")
        primal_tolerances = {
            name: tolerance.primal
            for name, tolerance in self.test_set.tolerances.items()
        }
        dual_tolerances = {
            name: tolerance.dual
            for name, tolerance in self.test_set.tolerances.items()
        }
        gap_tolerances = {
            name: tolerance.gap
            for name, tolerance in self.test_set.tolerances.items()
        }
        cost_tolerances = {
            name: tolerance.cost
            for name, tolerance in self.test_set.tolerances.items()
        }
        runtime_tolerances = {
            name: tolerance.runtime
            for name, tolerance in self.test_set.tolerances.items()
        }
        success_rate_df = self.results.build_success_rate_df(
            primal_tolerances,
            dual_tolerances,
            gap_tolerances,
            cost_tolerances,
        )
        correct_rate_df = self.results.build_correct_rate_df(
            primal_tolerances,
            dual_tolerances,
            gap_tolerances,
            cost_tolerances,
        )
        runtime_df = self.results.build_shifted_geometric_mean_df(
            column="runtime",
            shift=10.0,
            not_found_values=runtime_tolerances,
        )
        primal_df = self.results.build_shifted_geometric_mean_df(
            column="primal_residual",
            shift=10.0,
            not_found_values=primal_tolerances,
        )
        dual_df = self.results.build_shifted_geometric_mean_df(
            column="dual_residual",
            shift=10.0,
            not_found_values=dual_tolerances,
        )
        gap_df = self.results.build_shifted_geometric_mean_df(
            column="duality_gap",
            shift=10.0,
            not_found_values=gap_tolerances,
        )
        cost_df = self.results.build_shifted_geometric_mean_df(
            column="cost_error",
            shift=10.0,
            not_found_values=cost_tolerances,
        )
        italics_settings = [f"*{x}*" for x in self.solver_settings]
        upper_settings = {
            name: name.replace("_", " ").capitalize()
            for name in self.solver_settings
        }
        with open(path, "w") as fh:
            fh.write(
                f"""# {self.test_set.title}

- CPU: {self.cpu_info}
- Date: {self.date}
- Run by: [@{self.author}](https://github.com/{self.author}/)

## Contents

"""
            )
            if self.test_set.description is not None:
                fh.write("* [Description](#description)\n")
            fh.write(
                """* [Solvers](#solvers)
* [Settings](#settings)
* [Results by settings](#results-by-settings)\n"""
            )
            for name in self.solver_settings:
                fh.write(f"    * [{upper_settings[name]}](#{name})\n")
            fh.write(
                """* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Primal residual](#primal-residual)
    * [Dual residual](#dual-residual)
    * [Duality gap](#duality-gap)
    * [Cost error](#cost-error)

"""
            )
            if self.test_set.description is not None:
                fh.write(f"## Description\n\n{self.test_set.description}\n\n")
            fh.write(
                f"""## Solvers

{self.get_solver_versions_table()}

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v{qpsolvers_version}.

## Settings

There are {len(italics_settings)} settings: {", ".join(italics_settings[:-1])}
and {italics_settings[-1]}. They validate solutions using the following
tolerances:

{self.get_tolerances_table()}

Solvers for each settings are configured as follows:

{self.get_solver_settings_table()}

## Results by settings\n\n"""
            )
            for settings in self.solver_settings:
                cols = {
                    "Success rate (%)": success_rate_df[settings],
                    "Runtime (shm)": runtime_df[settings],
                    "Primal residual (shm)": primal_df[settings],
                    "Dual residual (shm)": dual_df[settings],
                    "Duality gap (shm)": gap_df[settings],
                    "Cost error (shm)": cost_df[settings],
                }
                df = pandas.DataFrame([], index=gap_df.index).assign(**cols)
                fh.write(
                    f"""### {upper_settings[settings]}

{df.to_markdown(index=True, floatfmt=".1f")}\n\n"""
                )

            fh.write(
                f"""## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

{success_rate_df.to_markdown(index=True, floatfmt=".0f")}

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution satisfies optimality conditions within
[tolerance](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

{correct_rate_df.to_markdown(index=True, floatfmt=".0f")}

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

{runtime_df.to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time
limit](#settings) when it fails to solve a problem.

### Primal residual

The primal residual measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal residuals over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal residual of Y is Y times less
precise on constraints than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

{primal_df.to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal residual equal to the
full [primal tolerance](#settings).

### Dual residual

The dual residual measures the maximum violation of the dual feasibility
condition in the solution returned by a solver. We use the shifted geometric
mean to compare solver dual residuals over the whole test set. Intuitively, a
solver with a shifted-geometric-mean dual residual of Y is Y times less precise
on the dual feasibility condition than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

{dual_df.to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a dual residual equal to the full
[dual tolerance](#settings).

### Duality gap

The duality gap measures the consistency of the primal and dual solutions
returned by a solver. A duality gap close to zero ensures that the
complementarity slackness optimality condition is satisfied. We use the shifted
geometric mean to compare solver duality gaps over the whole test set.
Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times
less precise on the complementarity slackness condition than the best solver
over the test set. See [Metrics](../README.md#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

{gap_df.to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a duality gap equal to the full
[gap tolerance](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

{cost_df.to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
"""
            )
        logging.info(f"Wrote report to {path}")
