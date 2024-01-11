#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

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

    def test_skip_solver_timeout_specific(self):
        foo = custom_problem(name="foo")
        self.test_set.known_solver_timeouts[("foo", "bar", "default")] = 1.0
        self.assertFalse(
            self.test_set.skip_solver_timeout(
                1.0, foo, "unknown_solver", "settings"
            )
        )
        self.assertFalse(
            self.test_set.skip_solver_timeout(
                2.0,  # greater than 1.0
                foo,
                "bar",
                "default",
            )
        )
        self.assertTrue(
            self.test_set.skip_solver_timeout(
                0.5,  # lower than 1.0
                foo,
                "bar",
                "default",
            )
        )

    def test_skip_solver_timeout_pattern(self):
        foo = custom_problem(name="foo")
        self.test_set.known_solver_timeouts[("foo", "bar", "*")] = 1.0
        self.assertFalse(
            self.test_set.skip_solver_timeout(
                2.0,  # greater than 1.0
                foo,
                "bar",
                "flip",
            )
        )
        self.assertTrue(
            self.test_set.skip_solver_timeout(
                0.5,  # lower than 1.0
                foo,
                "bar",
                "flop",
            )
        )
