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
Maros-Meszaros test set.
"""

import datetime
import os.path
from typing import Dict, Iterator

import yaml

from ..problem import Problem
from ..solver_settings import SolverSettings
from ..spdlog import logging
from ..test_set import TestSet
from ..utils import get_cpu_info


class MarosMeszaros(TestSet):

    data_dir: str
    optimal_costs: Dict[str, float]

    @property
    def name(self) -> str:
        return "maros_meszaros"

    @property
    def sparse_only(self) -> bool:
        return True

    def __init__(
        self,
        data_dir: str,
        results_dir: str,
        solver_settings: Dict[str, SolverSettings],
    ):
        super().__init__(data_dir, results_dir, solver_settings)
        with open(os.path.join(data_dir, "OPTCOSTS.yaml"), "r") as fh:
            file_dict = yaml.load(fh, Loader=yaml.SafeLoader)
            optimal_costs = {k: float(v) for k, v in file_dict.items()}
        self.data_dir = data_dir
        self.optimal_costs = optimal_costs

    def __iter__(self) -> Iterator[Problem]:
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".mat"):
                mat_path = os.path.join(self.data_dir, fname)
                problem = Problem.from_mat_file(mat_path)
                if problem.name in self.optimal_costs:
                    problem.optimal_cost = self.optimal_costs[problem.name]
                yield problem

    def write_report(self) -> None:
        date = str(datetime.datetime.now(datetime.timezone.utc))
        cpu_info = get_cpu_info()

        success_rate_df = self.results.build_success_rate_df()
        success_rate_table = success_rate_df.to_markdown(index=True)
        success_rate_table = success_rate_table.replace(" 100    ", " **100**")

        geometric_mean_df = self.results.build_geometric_mean_df(
            time_limits={
                key: settings.time_limit
                for key, settings in self.solver_settings.items()
            }
        )
        geometric_mean_table = geometric_mean_df.to_markdown(
            index=True, floatfmt=".1f"
        )

        with open(self.report_path, "w") as fh:
            fh.write(
                f"""# Maros and Meszaros Convex Quadratic Programming Test Set

- Date: {date}
- CPU: {cpu_info}

## Success rate

Precentage of problems each solver is able to solve:

{success_rate_table}

Rows are solvers and columns are solver settings.

## Computation time

We compare solver computation times using the shifted geometric mean.

**Intuition:** a solver with a shifted geometric mean of Y is Y times slower
than the best solver over the test set.

### Details

There is a different ranking of solver runtimes for each problem in the test
set. To aggregate those rankings into a single metric over the whole test set,
we use the shifted geometric mean, which is a standard in [benchmarks for
optimization software](http://plato.asu.edu/bench.html).

The shifted geometric mean is a slowdown factor compared to the best solver
over the whole test set. It has the advantage of being compromised by neither
large outliers (as opposed to the arithmetic mean) nor by small outliers (in
contrast to the geometric geometric mean). The best solvers have a shifted
geometric mean close to one:

### Results

{geometric_mean_table}

Rows are solvers and columns are solver settings.

## Precision

### Cost errors

### Constraint errors

"""
            )

        logging.info(f"Wrote report to {self.report_path}")
