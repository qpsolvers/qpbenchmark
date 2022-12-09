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
Problems related to "Geometric and numerical aspects of redundancy", Wieber,
Escande, Dimitrov and Sherikov (2017).
"""

import numpy as np

from ..problem import Problem


def __get_problem(alpha: float):
    return Problem(
        P=np.array([[1.0, 0.0], [0.0, 1.0]]),
        q=np.zeros(2),
        G=None,
        h=None,
        A=np.array([1.0, alpha]),
        b=np.array([1.0]),
        lb=None,
        ub=None,
        name=f"weds_{alpha=}",
        optimal_cost=12.42,  # TODO
    )


problems = [__get_problem(alpha) for alpha in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]]

__all__ = [
    "problems",
]
