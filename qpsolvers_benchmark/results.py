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

import pandas


class Results:
    def __init__(self, path):
        df = pandas.DataFrame(
            [], columns=["problem", "solver", "found", "primal"]
        )
        df = pandas.concat([df, pandas.read_csv(path)])
        self.df = df
        self.path = path

    def append_result(self, problem, solver: str, solution):
        df = self.df
        row = df.loc[
            (df["problem"] == problem.name) & (df["solver"] == solver)
        ]
        found = solution is not None
        primal = self.validator.check_primal(problem, solution)
        if row.empty:
            df = pandas.concat(
                df,
                {
                    "problem": problem.name,
                    "solver": solver,
                    "found": found,
                    "primal": primal,
                },
            )
        df.loc[
            (df["problem"] == problem.name) & (df["solver"] == solver), ["found", "primal"]
        ] = (found, primal)

    def write(self):
        self.df.to_csv(self.path, index=False)
