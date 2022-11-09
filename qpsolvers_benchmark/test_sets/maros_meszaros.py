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

import json
import os.path
from typing import Dict, Iterator

from ..problem import Problem
from ..solver_settings import SolverSettings
from ..test_set import TestSet


class MarosMeszaros(TestSet):

    data_dir: str
    optimal_costs: Dict[str, float]

    def define_settings(self) -> Dict[str, SolverSettings]:
        default = SolverSettings(
            cost_tolerance=1000.0,
            primal_tolerance=1.0,
            time_limit=1000.0,
        )

        high_accuracy = SolverSettings(
            cost_tolerance=1000.0,
            primal_tolerance=1e-9,
            time_limit=1000.0,
        )
        high_accuracy.set_eps_abs(1e-9)
        high_accuracy.set_eps_rel(0.0)
        high_accuracy.set_param("qpoases", "termination_tolerance", 1e-7)

        self.solver_settings = {
            "default": default,
            "high_accuracy": high_accuracy,
        }

    @property
    def sparse_only(self) -> bool:
        return True

    @property
    def title(self) -> str:
        return "Maros-Meszaros test set"

    def __init__(self, data_dir: str):
        super().__init__()
        data_dir = os.path.join(data_dir, "maros_meszaros")
        cost_path = os.path.join(data_dir, "OPTCOSTS.json")
        with open(cost_path, "r") as fh:
            file_dict = json.load(fh)
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
