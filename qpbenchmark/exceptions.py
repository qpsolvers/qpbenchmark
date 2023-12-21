#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
# SPDX-License-Identifier: Apache-2.0

"""Benchmark exceptions."""


class BenchmarkError(Exception):
    """Base class for benchmark exceptions."""


class ProblemNotFound(BenchmarkError):
    """Exception raised when a requested problem is not part of a test set."""


class ResultsError(BenchmarkError):
    """Exception raised when results formatting is wrong."""
