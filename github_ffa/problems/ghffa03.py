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

"""GHFFA03 problem.

This problem is described at:
https://github.com/stephane-caron/qpsolvers_benchmark/issues/29.
"""

import numpy as np

from qpsolvers_benchmark.problem import Problem


def get_problem(n: int):
    """Get problem instance.

    Args:
        n: Number of optimization variables.
    """
    M = np.array(range(n * n), dtype=float).reshape((n, n))
    P = np.dot(M.T, M)  # this is a positive definite matrix
    q = np.dot(np.ones(n, dtype=float), M)
    return Problem(
        P=P,
        q=q,
        G=None,
        h=None,
        A=None,
        b=None,
        lb=None,
        ub=None,
        name=f"GHFFA03_{n=}",
        optimal_cost=0.0,
    )


problems = [get_problem(n=1000)]

__all__ = [
    "problems",
]
