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
Dense subset of the Maros-Meszaros test set.
"""

from typing import Iterator

from ..problem import Problem
from .maros_meszaros import MarosMeszaros


class MarosMeszarosDense(MarosMeszaros):
    @property
    def title(self) -> str:
        return "Maros-Meszaros dense subset"

    @property
    def sparse_only(self) -> bool:
        return False

    def define_solver_settings(self) -> None:
        super().define_solver_settings()

        default = self.solver_settings["default"]
        default.set_param("qpoases", "predefined_options", "default")

        low_accuracy = self.solver_settings["low_accuracy"]
        low_accuracy.set_param("qpoases", "predefined_options", "fast")

        high_accuracy = self.solver_settings["high_accuracy"]
        high_accuracy.set_param("qpoases", "predefined_options", "reliable")

    def __init__(self, data_dir: str):
        super().__init__(data_dir)

    def __iter__(self) -> Iterator[Problem]:
        for problem in super().__iter__():
            nb_variables = problem.nb_variables
            nb_constraints = problem.nb_constraints
            if nb_variables <= 1000 and nb_constraints <= 1000:
                yield problem.to_dense()
