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

"""GHFFA01 problem.

This problem is inspired by "Geometric and numerical aspects of redundancy",
Wieber, Escande, Dimitrov and Sherikov (2017).

See https://github.com/stephane-caron/qpsolvers_benchmark/issues/25
"""

import numpy as np

from ..problem import Problem


def get_problem(alpha: float):
    """Get problem instance.

    Args:
        alpha: Inverse condition number of the problem.
    """
    return Problem(
        P=np.eye(2),
        q=np.zeros(2),
        G=None,
        h=None,
        A=np.array([1.0, alpha]).reshape((1, 2)),
        b=np.array([1.0]),
        lb=None,
        ub=None,
        name=f"GHFFA01_{alpha=}",
        optimal_cost=0.5 / (1 + alpha ** 2),
    )


problems = [get_problem(alpha) for alpha in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]]

__all__ = [
    "problems",
]
