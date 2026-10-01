# SPDX-License-Identifier: Apache-2.0

"""Test the run function."""

import tempfile
import unittest

import qpbenchmark
from qpbenchmark import Results
from qpsolvers import SolverNotFound, available_solvers

from .custom_test_set import CustomTestSet


class TestRun(unittest.TestCase):
    """Test fixture for the run function."""

    def setUp(self):
        """Create empty results and a test set."""
        csv_path = tempfile.mktemp(".csv")
        self.results = Results(file_path=csv_path, test_set=CustomTestSet())
        self.test_set = CustomTestSet()

    def test_run_available_solvers(self):
        """Run adds one result per available solver."""
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
        """Run restricted to one solver adds a single result."""
        self.assertEqual(len(self.results.df), 0)
        qpbenchmark.run(
            self.test_set,
            self.results,
            only_problem="custom",
            only_settings="default",
            only_solver="daqp",  # installed by the "test" pixi feature
            rerun=False,
            rerun_timeouts=False,
        )
        self.assertEqual(len(self.results.df), 1)

    def test_settings_not_found(self):
        """Run raises an error on unknown settings."""
        with self.assertRaises(ValueError):
            qpbenchmark.run(
                self.test_set,
                self.results,
                only_settings="unknown",
                rerun=False,
                rerun_timeouts=False,
            )

    def test_solver_not_found(self):
        """Run raises an error on an unknown solver."""
        with self.assertRaises(SolverNotFound):
            qpbenchmark.run(
                self.test_set,
                self.results,
                only_solver="unknown",
                rerun=False,
                rerun_timeouts=False,
            )
