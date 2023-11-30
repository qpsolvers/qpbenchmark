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

"""Dense subset with positive definite P of the Maros-Meszaros test set."""

from typing import Iterator

from maros_meszaros_dense import MarosMeszarosDense

from qpbenchmark.problem import Problem
from qpbenchmark.utils import is_posdef


class MarosMeszarosDensePosdef(MarosMeszarosDense):
    """Subset of Maros-Meszaros restricted to smaller dense problems."""

    @property
    def description(self) -> str:
        """Description of the test set."""
        return (
            "Subset of the Maros-Meszaros test set "
            "restricted to smaller dense problems "
            "with positive definite Hessian matrix."
        )

    @property
    def title(self) -> str:
        """Test set title."""
        return "Maros-Meszaros dense positive definite subset"

    @property
    def sparse_only(self) -> bool:
        """Test set is dense."""
        return False

    def __iter__(self) -> Iterator[Problem]:
        """Iterate on test set problems."""
        for problem in super().__iter__():
            if is_posdef(problem.P):
                yield problem
