# SPDX-License-Identifier: Apache-2.0

"""Unit tests for problems."""

import os
import tempfile
import unittest

import numpy as np

from qpbenchmark.problem import Problem


class TestProblem(unittest.TestCase):
    """Test fixture for the Problem class."""

    def test_load(self):
        """Load a saved problem, named after its file."""
        problem = Problem(
            P=np.eye(3),
            q=np.zeros(3),
            G=None,
            h=None,
            A=None,
            b=None,
            lb=None,
            ub=None,
            name="TEST",
        )
        fpath = os.path.join(tempfile.gettempdir(), "FOOBAR.npz")
        problem.save(fpath)
        loaded = Problem.load(fpath)
        self.assertEqual(loaded.name, "FOOBAR")
