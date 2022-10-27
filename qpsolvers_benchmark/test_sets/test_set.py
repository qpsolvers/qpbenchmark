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
Base class for test sets.
"""

import abc
from typing import Iterator

from ..problem import Problem


class TestSet(abc.ABC):
    @abc.abstractproperty
    def name(self) -> str:
        """
        Name of the test set.
        """

    @abc.abstractproperty
    def title(self) -> str:
        """
        Full name, used as title for the output test report.
        """

    @abc.abstractproperty
    def sparse_only(self) -> bool:
        """
        If True, test set is restricted to solvers with a sparse matrix API.
        """

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Problem]:
        """
        Yield test test problems one by one.
        """
