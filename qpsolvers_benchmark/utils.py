#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Utility functions.
"""

import platform
from importlib import metadata
from typing import Set

import numpy as np

from .spdlog import logging

try:
    import cpuinfo
except ImportError:
    cpuinfo = None
    logging.warn("Run ``pip install py-cpuinfo`` for more accurate CPU info")


def bool_as_emoji(b: bool):
    return "\U00002714" if b else "\U0000274C"


def shgeom(v: np.ndarray, sh: float) -> float:
    """
    `Shifted geometric mean <http://plato.asu.edu/ftp/shgeom.html>`_.

    Args:
        v: Nonnegative values.
        sh: Shift parameter.

    Note:
        The mean is computed as exponential of sum of logs to avoid memory
        overflows. This is common practice.

    Notes:
        Quoting from `A Note on #fairbenchmarking
        <https://community.fico.com/s/blog-post/a5Q2E000000Dt0JUAS/fico1421>`_:
        "The geometric mean of n numbers is defined as the n-th root of their
        product. For the shifted geometric mean, a positive shift value s is
        added to each of the numbers before multiplying them and subtracted
        from the root afterwards. Shifted geometric means have the advantage to
        neither be compromised by very large outliers (in contrast to
        arithmetic means) nor by very small outliers (in contrast to geometric
        means)."
    """
    assert (v >= 0.0).all() and sh >= 1.0
    return np.exp(np.sum(np.log(v + sh)) / len(v)) - sh


def get_cpu_info():
    return (
        platform.processor()
        if cpuinfo is None
        else cpuinfo.get_cpu_info()["brand_raw"]
    )


def get_solver_versions(solvers: Set[str]):
    """
    Get version numbers for a given set of solvers.

    Args:
        solvers: Names of solvers to get the version of.

    Returns:
        Dictionary mapping solver names to their versions.
    """
    package_name = {solver: solver for solver in solvers}
    package_name.update(
        {
            "highs": "highspy",
            "proxqp": "proxsuite",
        }
    )
    versions = {
        solver: metadata.version(package)
        for solver, package in package_name.items()
    }
    return versions
