#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Unit tests for report generation."""

import unittest

from qpbenchmark import Report


class TestReport(unittest.TestCase):
    def test_report(self):
        report = Report(author="foobar", results=None)
        self.assertEqual(report.name, "foobar")
