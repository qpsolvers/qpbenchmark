#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Benchmark for quadratic programming solvers available in Python."""

from .problem import Problem
from .report import Report
from .results import Results
from .run import run
from .spdlog import logging
from .test_set import TestSet
from .tolerance import Tolerance
from .version import get_version

__version__ = get_version()

__all__ = [
    "Problem",
    "Report",
    "Results",
    "TestSet",
    "Tolerance",
    "logging",
    "run",
]
