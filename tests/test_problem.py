#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Unit tests for utility functions."""

import os
import tempfile
import unittest

import numpy as np

from qpbenchmark.problem import Problem


class TestUtils(unittest.TestCase):
    def test_load(self):
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
