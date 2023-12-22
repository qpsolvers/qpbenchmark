#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2022 Stéphane Caron and the qpsolvers contributors.
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for test sets."""

import unittest

import numpy as np

import qpbenchmark


def custom_problem(name: str) -> qpbenchmark.Problem:
    return qpbenchmark.Problem(
        P=np.eye(3),
        q=np.ones(3),
        G=None,
        h=None,
        A=None,
        b=None,
        lb=None,
        ub=None,
        name=name,
    )


class CustomTestSet(qpbenchmark.TestSet):
    @property
    def description(self) -> str:
        return "Unit test test set"

    @property
    def title(self) -> str:
        return "Unit test test set"

    @property
    def sparse_only(self) -> bool:
        return False

    def __iter__(self):
        yield custom_problem(name="custom")


class TestTestSet(unittest.TestCase):
    def setUp(self):
        self.test_set = CustomTestSet()

    def test_skip_solver_issue(self):
        foo = custom_problem(name="foo")
        self.test_set.known_solver_issues.add(("foo", "bar"))
        self.assertTrue(self.test_set.skip_solver_issue(foo, "bar"))
        self.assertFalse(self.test_set.skip_solver_issue(foo, "baz"))
