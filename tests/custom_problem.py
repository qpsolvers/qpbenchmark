#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

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
