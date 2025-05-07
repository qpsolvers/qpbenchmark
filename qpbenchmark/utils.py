#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Utility functions."""

from collections import OrderedDict
from importlib import import_module, metadata
from time import perf_counter
from typing import Set, Tuple

import cpuinfo
import numpy as np
import qpsolvers

from .problem import Problem
from .spdlog import logging


def capitalize_settings(name: str) -> str:
    """Capitalize settings name.

    Args:
        name: Settings name, e.g. "low_accuracy".

    Returns:
        Capitalized settings name to use as column title, e.g. "Low accuracy".
    """
    return name.replace("_", " ").capitalize()


def get_cpu_info_summary() -> str:
    """Get CPU information summary as a single string.

    Returns:
        CPU information as a single string.
    """
    return cpuinfo.get_cpu_info()["brand_raw"]


def get_gpu_info_summary() -> str:
    """Get GPU information summary as a single string.

    Note:
        This function only works if PyTorch is installed (for instance via
        `conda install pytorch`).

    Returns:
        GPU information string, if available, empty string otherwise.
    """
    try:
        import torch

        return torch.cuda.get_device_name()
    except ModuleNotFoundError:
        return ""


def get_cpu_info_table() -> str:
    """Get CPU information as a Markdown table.

    Returns:
        CPU information as a Markdown table.
    """
    info = OrderedDict(sorted(cpuinfo.get_cpu_info().items()))
    skips = set(
        [
            "cpuinfo_version",
            "cpuinfo_version_string",
            "hz_actual",
            "hz_actual_friendly",
            "hz_advertised",
            "hz_advertised_friendly",
        ]
    )
    table = "| Property | Value |\n"
    table += "|----------|-------|\n"
    for key, value in info.items():
        if key in skips:
            continue
        if key == "flags":
            value = ", ".join(f"`{flag}`" for flag in value)
        table += f"| `{key}` | {value} |\n"
    return table


def get_solver_versions(solvers: Set[str]):
    """Get version numbers for a given set of solvers.

    Args:
        solvers: Names of solvers to get the version of.

    Returns:
        Dictionary mapping solver names to their versions.
    """
    diff = {
        "gurobi": "gurobipy",
        "highs": "highspy",
        "hpipm": "hpipm_python",
        "jaxopt_osqp": "jaxopt",
        "proxqp": "proxsuite",
    }
    package_names = {solver: diff.get(solver, solver) for solver in solvers}
    versions = {}
    for solver, package_name in package_names.items():
        try:
            versions[solver] = metadata.version(package_name)
        except metadata.PackageNotFoundError:
            pass
        if solver in versions and solver != "cvxopt":
            # For some reason, metadata.versions("cvxopt") returns 0.0.0
            continue
        try:
            module = import_module(package_name)
            versions[solver] = module.__version__
        except AttributeError:
            pass
        except ModuleNotFoundError:
            pass
    if "qpoases" in solvers and "qpoases" not in versions:
        # See https://github.com/coin-or/qpOASES/issues/140
        versions["qpoases"] = "3.2.1"
    if "gurobi" in versions:
        versions["gurobi"] += " (size-limited)"
    return versions


def time_solve_problem(
    problem: Problem, solver: str, **kwargs
) -> Tuple[qpsolvers.Solution, float]:
    """Solve quadratic program.

    Args:
        problem: Quadratic program to solve.
        solver: Name of the backend QP solver to call.
        kwargs: Keyword arguments forwarded to underlying solver.

    Returns:
        Solution to the quadratic program, along with the time the solver took
        to compute it.
    """
    # Don't time matrix conversions for solvers that require sparse inputs
    if (
        solver in qpsolvers.sparse_solvers
        and solver not in qpsolvers.dense_solvers
    ):
        problem = problem.to_sparse()
    start_time = perf_counter()
    try:
        solution = qpsolvers.solve_problem(problem, solver=solver, **kwargs)
    except Exception as e:  # pylint: disable=W0703
        # TODO(scaron): wait for qpsolvers update regarding exceptions
        # See https://github.com/qpsolvers/qpsolvers/pull/139
        logging.warning(
            "Caught solver %s exception from solver '%s' on problem '%s': %s",
            type(e).__name__,
            solver,
            problem.name,
            str(e),
        )
        solution = qpsolvers.Solution(problem)
    runtime = perf_counter() - start_time
    return solution, runtime


def is_posdef(M: np.ndarray) -> bool:
    """Test whether a matrix is positive-definite.

    Args:
        M: Matrix to test.
    """
    return all(np.linalg.eigvals(M) > 0)
