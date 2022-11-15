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
Inverse kinematics test set.
"""

import json
import os.path
from typing import Iterator

from ..problem import Problem
from ..solver_settings import SolverSettings
from ..test_set import TestSet
from ..tolerance import Tolerance

try:
    from robot_descriptions.loaders.pinocchio import load_robot_description
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "This test set requires 'robot_descriptions', "
        "which can be installed by ``pip install robot_descriptions``"
    ) from e

try:
    import pink
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "This test set requires 'pink', "
        "which can be installed by ``pip install pin-pink``"
    ) from e


ROBOT_DESCRIPTIONS = ["upkie_description"]


class InverseKinematics(TestSet):
    @property
    def title(self) -> str:
        return "Inverse kinematics test set"

    @property
    def sparse_only(self) -> bool:
        return False

    def define_tolerances(self) -> None:
        self.tolerances = {
            "default": Tolerance(
                cost=1000.0,
                primal=1e-2,
                runtime=1.0,
            ),
        }

    def define_solver_settings(self) -> None:
        default = SolverSettings()
        default.set_time_limit(self.tolerances["default"].runtime)

        self.solver_settings = {
            "default": default,
        }

    def __iter__(self) -> Iterator[Problem]:
        for desc in ROBOT_DESCRIPTIONS:
            robot = load_robot_description(desc)

            problem = Problem.from_mat_file(mat_path)
            if problem.name in self.optimal_costs:
                problem.optimal_cost = self.optimal_costs[problem.name]
            yield problem
