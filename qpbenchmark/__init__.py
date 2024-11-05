#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Benchmark for quadratic programming solvers available in Python."""

from .exceptions import BenchmarkError, ProblemNotFound, ResultsError
from .parquet_test_set import ParquetTestSet
from .problem import Problem
from .problem_list import ProblemList
from .report import Report
from .results import Results
from .run import run
from .spdlog import logging
from .test_set import TestSet
from .tolerance import Tolerance
from .version import get_version

__version__ = get_version()

__all__ = [
    "BenchmarkError",
    "ParquetTestSet",
    "Problem",
    "ProblemList",
    "ProblemNotFound",
    "Report",
    "Results",
    "ResultsError",
    "TestSet",
    "Tolerance",
    "logging",
    "run",
]
