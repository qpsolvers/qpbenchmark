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

from typing import Iterator

from ..problem import Problem
from ..test_set import TestSet
from ..tolerance import Tolerance
from .github_ffa_problems import github_ffa_problems


class GithubFfa(TestSet):

    """
    GitHub free-for-all test set.

    Note:
        This test set is open to proposals from the community. Feel free to
        `submit a new problem
        <https://github.com/stephane-caron/qpsolvers_benchmark/issues/new?template=new_problem.md>`__.
    """

    @property
    def description(self) -> str:
        """
        Description of the test set.
        """
        issues = "https://github.com/stephane-caron/qpsolvers_benchmark/issues"
        problems = (
            (
                "GHFFA01",
                25,
                "Project the origin on a 2D line that becomes vertical.",
            ),
            (
                "GHFFA02",
                27,
                "Linear system with two variables and a large "
                "condition number.",
            ),
            (
                "GHFFA03",
                29,
                "Ill-conditioned unconstrained least squares.",
            ),
        )
        return "Problems in this test set:\n\n" + "\n".join(
            f"- [{name}]({issues}/{inum}): {desc}"
            for name, inum, desc in problems
        )

    @property
    def title(self) -> str:
        return "GitHub free-for-all test set"

    @property
    def sparse_only(self) -> bool:
        return False

    def define_tolerances(self) -> None:
        self.tolerances = {
            "default": Tolerance(
                cost=1000.0,
                primal=1.0,
                dual=1.0,
                gap=1.0,
                runtime=100.0,
            ),
            "low_accuracy": Tolerance(
                cost=1000.0,
                primal=1e-3,
                dual=1e-3,
                gap=1e-3,
                runtime=100.0,
            ),
            "high_accuracy": Tolerance(
                cost=1000.0,
                primal=1e-9,
                dual=1e-9,
                gap=1e-9,
                runtime=100.0,
            ),
        }

    def __iter__(self) -> Iterator[Problem]:
        for problem in github_ffa_problems:
            yield problem
