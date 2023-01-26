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

    """
    Subset of the Maros-Meszaros test set restricted to smaller dense problems.
    """

    @property
    def description(self) -> str:
        """
        Description of the test set.
        """
        return (
            "Subset of the Maros-Meszaros test set "
            "restricted to smaller dense problems."
        )

    @property
    def title(self) -> str:
        return "Maros-Meszaros dense subset"

    @property
    def sparse_only(self) -> bool:
        return False

    @staticmethod
    def count_constraints(problem: Problem):
        """
        Count inequality and equality constraints.

        Notes:
            We only count box inequality constraints once, and only from lower
            bounds. That latter part is specific to this test set.
        """
        m = 0
        if problem.G is not None:
            m += problem.G.shape[0]
        if problem.A is not None:
            m += problem.A.shape[0]
        if problem.lb is not None:
            m += problem.lb.shape[0]
        return m

    def __iter__(self) -> Iterator[Problem]:
        for problem in super().__iter__():
            nb_variables = problem.P.shape[0]
            nb_constraints = self.count_constraints(problem)
            if nb_variables <= 1000 and nb_constraints <= 1000:
                yield problem.to_dense()
