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
Benchmark report generator.
"""

import datetime
import logging
import platform

from .utils import check_as_emoji
from .validator import Validator

CPU_INFO = platform.processor()

try:
    import cpuinfo

    CPU_INFO = cpuinfo.get_cpu_info()["brand_raw"]
except ImportError:
    logging.warn(
        f'CPU info set to "{CPU_INFO}", '
        "run ``pip install py-cpuinfo`` for a more accurate description"
    )


class Report:
    def __init__(self, fname: str, validator: Validator):
        """
        Initialize report written to file.

        Args:
            fname: File to write report to.
        """
        self.output = open(fname, "w")
        self.validator = validator
        self.results = []

    def start(self):
        self.output.write(
            f"""# Benchmark

- Date: {str(datetime.datetime.now(datetime.timezone.utc))}
- CPU: {CPU_INFO}

## Validation parameters

| Name | Value |
|------|-------|
"""
        )
        self.output.write(
            "\n".join(
                [
                    f"| ``{name}`` | {value} |"
                    for name, value in self.validator.list_params()
                ]
            )
        )
        self.output.write("\n\n")

    def append_result(self, problem, solver: str, solution):
        self.results.append(
            {
                "problem": problem.name,
                "solver": solver,
                "found": solution is not None,
                "primal": self.validator.check_primal(problem, solution),
            }
        )

    def finalize(self):
        self.output.write(
            """## Results

| Problem | Solver | Found solution? | Primal |
|---------|--------|-----------------|--------|
"""
        )
        for result in self.results:
            problem = result["problem"]
            solver = result["solver"]
            found = check_as_emoji(result["found"])
            primal = check_as_emoji(result["primal"])
            self.output.write(
                f"| {problem} | {solver} | {found} | {primal} |\n"
            )
