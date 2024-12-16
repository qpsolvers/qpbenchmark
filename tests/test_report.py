#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Unit tests for report generation."""

import unittest

from qpbenchmark import Report, Results

from .custom_test_set import CustomTestSet


class TestReport(unittest.TestCase):
    def setUp(self):
        self.results = Results(file_path=None, test_set=CustomTestSet())
        self.report = Report(author="foobar", results=self.results)

    def test_author(self):
        self.assertEqual(self.report.author, "foobar")
