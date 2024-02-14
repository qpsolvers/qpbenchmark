#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

import qpbenchmark

from .custom_problem import custom_problem


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
        yield custom_problem(name="custom_again")  # test only_problem
