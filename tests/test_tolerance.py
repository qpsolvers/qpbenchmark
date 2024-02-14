#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Unit tests for tolerance settings."""

import unittest

from qpbenchmark import Tolerance, BenchmarkError


class TestTolerance(unittest.TestCase):
    def test_from_metric(self):
        tolerance = Tolerance(
            primal=1.0,
            dual=2.0,
            gap=3.0,
            runtime=4.0,
        )
        self.assertAlmostEqual(tolerance.from_metric("primal_residual"), 1.0)
        self.assertAlmostEqual(tolerance.from_metric("dual_residual"), 2.0)
        self.assertAlmostEqual(tolerance.from_metric("duality_gap"), 3.0)
        self.assertAlmostEqual(tolerance.from_metric("runtime"), 4.0)
        with self.assertRaises(BenchmarkError):
            tolerance.from_metric("foo")
