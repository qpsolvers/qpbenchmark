#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""Test the run function."""

import tempfile
import unittest

from qpsolvers import SolverNotFound, available_solvers

import qpbenchmark
from qpbenchmark import Results

from .custom_test_set import CustomTestSet


class TestRun(unittest.TestCase):
    def setUp(self):
        csv_path = tempfile.mktemp(".csv")
        self.results = Results(file_path=csv_path, test_set=CustomTestSet())
        self.test_set = CustomTestSet()

    def test_run_available_solvers(self):
        self.assertEqual(len(self.results.df), 0)
        qpbenchmark.run(
            self.test_set,
            self.results,
            only_problem="custom",
            only_settings="default",
            rerun=False,
            rerun_timeouts=False,
        )
        self.assertEqual(len(self.results.df), len(available_solvers))

    def test_only_solver(self):
        self.assertEqual(len(self.results.df), 0)
        qpbenchmark.run(
            self.test_set,
            self.results,
            only_problem="custom",
            only_settings="default",
            only_solver="daqp",  # listed in tox.ini
            rerun=False,
            rerun_timeouts=False,
        )
        self.assertEqual(len(self.results.df), 1)

    def test_settings_not_found(self):
        with self.assertRaises(ValueError):
            qpbenchmark.run(
                self.test_set,
                self.results,
                only_settings="unknown",
                rerun=False,
                rerun_timeouts=False,
            )

    def test_solver_not_found(self):
        with self.assertRaises(SolverNotFound):
            qpbenchmark.run(
                self.test_set,
                self.results,
                only_solver="unknown",
                rerun=False,
                rerun_timeouts=False,
            )
