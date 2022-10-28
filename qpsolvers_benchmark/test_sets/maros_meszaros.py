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
from ..test_set import TestSet
from ..utils import bool_as_emoji, get_cpu_info


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
    ):
        super().__init__(data_dir, results_dir)
        with open(os.path.join(data_dir, "OPTCOSTS.yaml"), "r") as fh:
            file_dict = yaml.load(fh)
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
        found_df = self.results.build_found_df()
        found_summary_df = self.results.build_found_summary_df()

        found_table = found_df.to_markdown(index=True)
        found_table = found_table.replace(
            "False", bool_as_emoji(False) + " " * 3
        )
        found_table = found_table.replace(
            "True", bool_as_emoji(True) + " " * 3
        )

        found_summary_table = found_summary_df.to_markdown(index=True)
        found_summary_table = found_summary_table.replace(" 100    ", " **100**")

        with open(self.report_path, "w") as fh:
            fh.write(
                f"""# Maros and Meszaros Convex Quadratic Programming Test Set

- Date: {date}
- CPU: {cpu_info}

## Success rate

Since this is a benchmark of difficult problems, we first look at how many
problems each solver is able to solve:

{found_summary_table}

### Details

{found_table}
"""
            )
