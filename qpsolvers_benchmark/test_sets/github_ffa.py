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
GitHub free-for-all test set.
"""

import json
import os.path
from typing import Dict, Iterator

from ..problem import Problem
from ..solver_settings import SolverSettings
from ..test_set import TestSet
from ..tolerance import Tolerance
from .problems.github_ffa import available_problems


class GitHubFFA(TestSet):
    @property
    def title(self) -> str:
        return "GitHub QP test set"

    @property
    def sparse_only(self) -> bool:
        return False

    def define_tolerances(self) -> None:
        self.tolerances = {
            "default": Tolerance(
                cost=1000.0,
                primal=1.0,
                runtime=100.0,
            ),
            "low_accuracy": Tolerance(
                cost=1000.0,
                primal=1e-3,
                runtime=100.0,
            ),
            "high_accuracy": Tolerance(
                cost=1000.0,
                primal=1e-9,
                runtime=100.0,
            ),
        }

    def define_solver_settings(self) -> None:
        default = SolverSettings()
        default.set_time_limit(self.tolerances["default"].runtime)

        low_accuracy = SolverSettings()
        low_accuracy.set_time_limit(self.tolerances["low_accuracy"].runtime)
        low_accuracy.set_eps_abs(1e-3)
        low_accuracy.set_eps_rel(0.0)

        high_accuracy = SolverSettings()
        high_accuracy.set_time_limit(self.tolerances["high_accuracy"].runtime)
        high_accuracy.set_eps_abs(1e-9)
        high_accuracy.set_eps_rel(0.0)

        self.solver_settings = {
            "default": default,
            "low_accuracy": low_accuracy,
            "high_accuracy": high_accuracy,
        }

    def __init__(self, data_dir: str):
        super().__init__()

    def __iter__(self) -> Iterator[Problem]:
        for function in get_wieber2017geometric_problems():
            yield problem
