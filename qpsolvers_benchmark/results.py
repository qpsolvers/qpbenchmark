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
            [], columns=["problem", "solver", "found", "primal"]
        )
        if os.path.exists(csv_path):
            df = pandas.concat([df, pandas.read_csv(csv_path)])
        self.df = df
        self.csv_path = csv_path

    def update(self, problem: Problem, solver: str, solution):
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
                        "found": [solution is not None],
                        "primal_error": [problem.primal_error(solution)],
                    }
                ),
            ],
        )

    def write(self):
        self.df.to_csv(self.csv_path, index=False)
