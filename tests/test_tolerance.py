#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Unit tests for tolerance settings."""

import unittest

from qpbenchmark import Tolerance


class TestTolerance(unittest.TestCase):
    def test_tolerance(self):
        tolerance = (
            Tolerance(
                primal=1.0,
                dual=2.0,
                gap=3.0,
                runtime=4.0,
            )
        )
        self.assertAlmostEqual(tolerance.primal, 1.0)
        self.assertAlmostEqual(tolerance.dual, 2.0)
        self.assertAlmostEqual(tolerance.gap, 3.0)
        self.assertAlmostEqual(tolerance.runtime, 4.0)
