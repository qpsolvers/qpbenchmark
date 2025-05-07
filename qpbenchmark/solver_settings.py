#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Solver settings."""

from typing import Any, Dict, Iterator, Set

import numpy as np


class SolverSettings:
    """Settings for multiple solvers."""

    IMPLEMENTED_SOLVERS: Set[str] = set(
        [
            "clarabel",
            "cvxopt",
            "daqp",
            "ecos",
            "gurobi",
            "highs",
            "hpipm",
            "jaxopt_osqp",
            "kvxopt",
            "nppro",
            "osqp",
            "piqp",
            "proxqp",
            "qpalm",
            "qpax",
            "qpoases",
            "qpswift",
            "quadprog",
            "scs",
        ]
    )

    @classmethod
    def is_implemented(cls, solver: str):
        """Check whether a solver is implemented by this class."""
        return solver in cls.IMPLEMENTED_SOLVERS

    def __init__(self) -> None:
        """Initialize settings."""
        self.__settings: Dict[str, Dict[str, Any]] = {
            solver: {} for solver in self.IMPLEMENTED_SOLVERS
        }

    def __getitem__(self, solver: str) -> Dict[str, Any]:
        """Get settings dictionary of a given solver.

        Args:
            solver: Name of the QP solver.

        Returns:
            Dictionary of custom solver settings.
        """
        return self.__settings[solver]

    def set_eps_abs(self, eps_abs: float) -> None:
        r"""Set absolute tolerances for solvers that support it.

        Args:
            eps_abs: Absolute primal, dual and duality-gap tolerance.

        Notes:
            When we set an absolute tolerance :math:`\epsilon_{abs}` on
            residuals, we ask the solver to find an approximation of the
            optimum such that the primal residual, dual residual and duality
            gap are below :math:`\epsilon_{abs}`, that is:

            .. math::

                \begin{align}
                r_p := \max(\| A x - b \|_\infty, [G x - h]^+, [lb - x]^+,
                [x - ub]^+) & \leq \epsilon_{abs} \\
                r_d := \| P x + q + A^T y + G^T z + z_{box} \|_\infty &
                \leq \epsilon_{abs} \\
                r_g := | x^T P x + q^T x + b^T y + h^T z + lb^T z_{box}^- +
                ub^T z_{box}^+ | & \leq \epsilon_{abs}
                \end{align}

            were :math:`v^- = \min(v, 0)` and :math:`v^+ = \max(v, 0)`. The
            tolerance on the primal residual is called "feasibility tolerance"
            by some solvers, for instance CVXOPT and ECOS. See `this note
            <https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html>`__
            for more details.
        """
        self.__settings["clarabel"]["tol_feas"] = eps_abs
        self.__settings["clarabel"]["tol_gap_abs"] = eps_abs
        self.__settings["cvxopt"]["feastol"] = eps_abs
        self.__settings["daqp"]["dual_tol"] = eps_abs
        self.__settings["daqp"]["primal_tol"] = eps_abs
        self.__settings["ecos"]["feastol"] = eps_abs
        self.__settings["gurobi"]["FeasibilityTol"] = eps_abs  # primal
        self.__settings["gurobi"]["OptimalityTol"] = eps_abs  # dual
        self.__settings["highs"]["dual_feasibility_tolerance"] = eps_abs

        # Note on primal feasibility with HiGHS: "Primal feasibility is
        # maintained rather than achieved (in contrast to IPM or ADMM based
        # solvers) [...] changing the primal feasibility tolerance setting
        # doesn't have any effect on QPs at the moment".
        # https://github.com/ERGO-Code/HiGHS/issues/996#issuecomment-1561890995
        self.__settings["highs"]["primal_feasibility_tolerance"] = eps_abs

        self.__settings["hpipm"]["tol_dual_gap"] = eps_abs
        self.__settings["hpipm"]["tol_eq"] = eps_abs
        self.__settings["hpipm"]["tol_ineq"] = eps_abs
        self.__settings["hpipm"]["tol_stat"] = eps_abs
        self.__settings["jaxopt_osqp"]["tol"] = eps_abs
        self.__settings["kvxopt"]["feastol"] = eps_abs
        self.__settings["osqp"]["eps_abs"] = eps_abs
        self.__settings["piqp"]["eps_abs"] = eps_abs
        self.__settings["piqp"]["eps_duality_gap_abs"] = eps_abs
        self.__settings["proxqp"]["eps_abs"] = eps_abs
        self.__settings["proxqp"]["eps_duality_gap_abs"] = eps_abs
        self.__settings["qpalm"]["eps_abs"] = eps_abs

        # QPAX checks KKT residuals, so this setting will suffer from the same
        # issue as https://github.com/qpsolvers/qpbenchmark/issues/122
        self.__settings["qpax"]["solver_tol"] = eps_abs

        self.__settings["qpswift"]["RELTOL"] = eps_abs * np.sqrt(3.0)
        self.__settings["scs"]["eps_abs"] = eps_abs

    def set_eps_rel(self, eps_rel: float) -> None:
        """Set relative tolerances for solvers that support it.

        Args:
            eps_rel: Relative primal, dual and duality-gap tolerance.
        """
        self.__settings["clarabel"]["tol_gap_rel"] = eps_rel
        self.__settings["osqp"]["eps_rel"] = eps_rel
        self.__settings["piqp"]["eps_duality_gap_rel"] = eps_rel
        self.__settings["piqp"]["eps_rel"] = eps_rel
        self.__settings["proxqp"]["eps_duality_gap_rel"] = eps_rel
        self.__settings["proxqp"]["eps_rel"] = eps_rel
        self.__settings["qpalm"]["eps_rel"] = eps_rel
        self.__settings["scs"]["eps_rel"] = eps_rel

    def set_time_limit(self, time_limit: float) -> None:
        """Apply time limits to all solvers that support it.

        Args:
            time_limit: Time limit in seconds.
        """
        self.__settings["gurobi"]["TimeLimit"] = time_limit
        self.__settings["highs"]["time_limit"] = time_limit
        self.__settings["osqp"]["time_limit"] = time_limit
        self.__settings["qpalm"]["time_limit"] = time_limit
        self.__settings["qpoases"]["time_limit"] = time_limit
        self.__settings["scs"]["time_limit_secs"] = time_limit

    def set_verbosity(self, verbose: bool) -> None:
        """Apply verbosity settings to all solvers.

        Args:
            verbose: Verbosity boolean.
        """
        for solver in self.IMPLEMENTED_SOLVERS:
            self.__settings[solver]["verbose"] = verbose

    @property
    def solvers(self) -> Iterator[str]:
        """List solvers configured in these settings."""
        for solver in self.__settings:
            yield solver

    def get_param(self, solver: str, param: str, default: str) -> Any:
        """Get solver parameter in these settings.

        Args:
            solver: QP solver.
            param: Parameter name.
            default: Value to return if the parameter is not configured.

        Returns:
            Corresponding solver parameter, or default value.
        """
        if solver not in self.__settings:
            return default
        return self.__settings[solver].get(param, default)

    def set_param(self, solver: str, param: str, value: Any) -> None:
        """Set solver parameter.

        Args:
            solver: QP solver.
            param: Parameter name.
            value: Parameter value.
        """
        self.__settings[solver][param] = value
