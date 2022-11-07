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
        self.test_set = test_set

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
                for param in settings[solver]:
                    keys |= {(solver, param)}
        for solver, param in keys:
            row = {
                "solver": [solver],
                "parameter": [f"``{param}``"],
            }
            row.update(
                {
                    name: [solver_settings[name].get(solver, param, "-")]
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

    def get_versions_table(self):
        versions = get_solver_versions(self.test_set.solvers)
        packages = ["qpsolvers"]
        versions.update({pkg: metadata.version(pkg) for pkg in packages})
        versions_df = pandas.DataFrame(
            {
                "package": list(versions.keys()),
                "version": list(versions.values()),
            },
        )
        versions_df = versions_df.set_index("package")
        versions_df = versions_df.sort_index()
        versions_table = versions_df.to_markdown(index=True)
        return versions_table

    def get_success_rate_table(self):
        success_rate_df = self.results.build_success_rate_df()
        success_rate_table = success_rate_df.to_markdown(
            index=True, floatfmt=".0f"
        )
        success_rate_table = success_rate_table.replace(" 100    ", " **100**")
        return success_rate_table

    def write(self, path: str) -> None:
        with open(path, "w") as fh:
            fh.write(
                f"""# {self.test_set.title}

- Author: [@{self.author}](https://github.com/{self.author}/)
- CPU: {self.cpu_info}
- Date: {self.date}

## Settings

- Cost error limit: {self.test_set.cost_error_limit}
- Primal error limit: {self.test_set.primal_error_limit}
- Time limit: {self.test_set.time_limit} seconds

{self.get_solver_settings_table()}

## Metrics

For each metric (computation time, primal error, cost error, ...), every
problem in the test set produces a different ranking of solvers. To aggregate
those rankings into a single metric over the whole test set, we use the
**shifted geometric mean**, which is a standard to aggregate computation times
in [benchmarks for optimization software](http://plato.asu.edu/bench.html).

The shifted geometric mean is a slowdown/loss factor compared to the best
solver over the whole test set. Hence, the best solvers for a given metric have
a shifted geometric mean close to one. This mean has the advantage of being
compromised by neither large outliers (as opposed to the arithmetic mean) nor
by small outliers (in contrast to the geometric geometric mean). Check out the
[references](#see-also) below for more information.

## Results

### Success rate

Precentage of problems each solver is able to solve:

{self.get_success_rate_table()}

Rows are solvers and columns are solver settings.

### Computation time

We compare solver computation times over the whole test set using the [shifted
geometric mean](#shifted-geometric-mean). Intuitively, a solver with a
shifted-geometric-mean runtime of Y is Y times slower than the best solver over
the test set.

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
violation in the solution returned by a solver. Here are the shifted geometric
means of solver primal errors (1.0 is the best):

{self.results.build_shifted_geometric_mean_df(
    column="primal_error",
    shift=10.0,
    not_found_value=self.test_set.primal_error_limit,
).to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal error limit](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. Here are the shifted
geometric means of solver cost errors (1.0 is the best):

{self.results.build_shifted_geometric_mean_df(
    column="cost_error",
    shift=10.0,
    not_found_value=self.test_set.cost_error_limit,
).to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
error limit](#settings).

## Package versions

Versions of all relevant packages used when running this test set:

{self.get_versions_table()}

## See also

- [How not to lie with statistics: the correct way to summarize benchmark
  results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf):
  why geometric means should always be used to summarize normalized results.
"""
            )
        logging.info(f"Wrote report to {path}")
