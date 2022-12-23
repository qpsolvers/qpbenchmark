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

from .spdlog import logging

try:
    import cpuinfo
except ImportError:
    cpuinfo = None
    logging.warning(
        "Run ``pip install py-cpuinfo`` for more accurate CPU info"
    )


def get_cpu_info() -> str:
    """
    Get CPU information.

    Returns:
        CPU information.
    """
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
    versions = {}
    for solver, package in package_name.items():
        try:
            versions[solver] = metadata.version(package)
        except metadata.PackageNotFoundError:
            continue
    if "qpoases" in solvers and "qpoases" not in versions:
        # Repository: https://github.com/stephane-caron/qpOASES
        # Commit: 11363a25cf4eab579c287e78bcb17273f314a2e0
        # Install: https://scaron.info/doc/qpsolvers/installation.html#qpoases
        versions["qpoases"] = "3.2.0"
    return versions
