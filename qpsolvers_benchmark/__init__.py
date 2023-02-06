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

"""Benchmark for quadratic programming solvers available in Python."""

from .report import Report
from .results import Results
from .run import run
from .spdlog import logging
from .test_set import TestSet
from .version import get_version

__version__ = get_version()

__all__ = [
    "Report",
    "Results",
    "TestSet",
    "logging",
    "run",
]
