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
from typing import Dict

import pandas

from .results import Results
from .solver_settings import SolverSettings
from .spdlog import logging
from .test_set import TestSet
from .utils import get_cpu_info, get_solver_versions


class Report:
    def __init__(
        self,
        test_set: TestSet,
        solver_settings: Dict[str, SolverSettings],
        results: Results,
    ):
        self.cpu_info = get_cpu_info()
        self.date = str(datetime.datetime.now(datetime.timezone.utc))
        self.results = results
        self.solver_settings = solver_settings
        self.test_set = test_set

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
        maintainer = self.test_set.maintainer
        primal_not_found_value = 1.0
        with open(path, "w") as fh:
            fh.write(
                f"""# {self.test_set.title}

- CPU: {self.cpu_info}
- Date: {self.date}
- Maintainer: [@{maintainer}](https://github.com/{maintainer}/)

## Settings

{self.get_versions_table()}

## Metrics

### Shifted geometric mean

For each metric (computation time, solution accuracy, ...), every problem in
the test set produces a different ranking of solvers. To aggregate those
rankings into a single metric over the whole test set, we use the shifted
geometric mean, which is a standard to aggregate computation times in
[benchmarks for optimization software](http://plato.asu.edu/bench.html).

The shifted geometric mean is a slowdown/loss factor compared to the best
solver over the whole test set. It has the advantage of being compromised by
neither large outliers (as opposed to the arithmetic mean) nor by small
outliers (in contrast to the geometric geometric mean). The best solvers have a
shifted geometric mean close to one.

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
violation in the solution returned by a solver. As with runtimes, we use the
[shifted geometric mean](#shifted-geometric-mean) to aggregate primal errors
over the whole test set.

Shifted geometric mean of solver primal errors (1.0 is the best):

{self.results.build_shifted_geometric_mean_df(
    column="primal_error",
    shift=10.0,
    not_found_value=primal_not_found_value,
).to_markdown(index=True, floatfmt=".1f")}

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error of
{primal_not_found_value}.

### Cost errors

...

### See also

- [How not to lie with statistics: the correct way to summarize benchmark
  results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf):
  why geometric means should always be used to summarize normalized results.
"""
            )
        logging.info(f"Wrote report to {path}")
