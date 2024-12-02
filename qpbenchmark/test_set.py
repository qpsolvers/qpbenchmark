#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Base class for test sets."""

import abc
from typing import Dict, Iterator, Optional, Set, Tuple

import qpsolvers

from .exceptions import ProblemNotFound
from .problem import Problem
from .solver_settings import SolverSettings
from .spdlog import logging
from .tolerance import Tolerance


class TestSet(abc.ABC):
    """Abstract base class for a test set.

    A test set is a collection of problems with solver settings.

    Attributes:
        solver_settings: Dictionary of solver parameters for each settings.
        tolerances: Validation tolerances.
    """

    known_solver_issues: Set[Tuple[str, str]]
    known_solver_timeouts: Dict[Tuple[str, str, str], float]
    solver_settings: Dict[str, SolverSettings]
    tolerances: Dict[str, Tolerance]

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Problem]:
        """Yield test-set problems one by one."""

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """Test set description."""

    @property
    @abc.abstractmethod
    def sparse_only(self) -> bool:
        """If True, restrict test set to solvers with a sparse matrix API."""

    @property
    @abc.abstractmethod
    def title(self) -> str:
        """Report title."""

    def define_tolerances(self, runtime: float = 10.0) -> None:
        """Define validation tolerances.

        This function can be overridden by child test-set classes.

        Args:
            runtime: Maximum QP solver runtime in seconds.
        """
        self.tolerances = {
            "default": Tolerance(
                primal=1.0,
                dual=1.0,
                gap=1.0,
                runtime=runtime,
            ),
            "high_accuracy": Tolerance(
                primal=1e-9,
                dual=1e-9,
                gap=1e-9,
                runtime=runtime,
            ),
            "low_accuracy": Tolerance(
                primal=1e-3,
                dual=1e-3,
                gap=1e-3,
                runtime=runtime,
            ),
            "mid_accuracy": Tolerance(
                primal=1e-6,
                dual=1e-6,
                gap=1e-6,
                runtime=runtime,
            ),
        }

    def define_solver_settings(self) -> None:
        """Define solver settings.

        This function can be overridden by child test-set classes.
        """
        default = SolverSettings()
        default.set_param("qpoases", "predefined_options", "default")
        default.set_time_limit(self.tolerances["default"].runtime)
        self.solver_settings["default"] = default

        high_accuracy = SolverSettings()
        high_accuracy.set_eps_abs(1e-9)
        high_accuracy.set_eps_rel(0.0)
        high_accuracy.set_param("piqp", "check_duality_gap", True)
        high_accuracy.set_param("proxqp", "check_duality_gap", True)
        high_accuracy.set_param("qpoases", "predefined_options", "reliable")
        high_accuracy.set_time_limit(self.tolerances["high_accuracy"].runtime)

        low_accuracy = SolverSettings()
        low_accuracy.set_eps_abs(1e-3)
        low_accuracy.set_eps_rel(0.0)
        low_accuracy.set_param("piqp", "check_duality_gap", True)
        low_accuracy.set_param("proxqp", "check_duality_gap", True)
        low_accuracy.set_param("qpoases", "predefined_options", "fast")
        low_accuracy.set_time_limit(self.tolerances["low_accuracy"].runtime)

        mid_accuracy = SolverSettings()
        mid_accuracy.set_eps_abs(1e-6)
        mid_accuracy.set_eps_rel(0.0)
        mid_accuracy.set_param("piqp", "check_duality_gap", True)
        mid_accuracy.set_param("proxqp", "check_duality_gap", True)
        mid_accuracy.set_time_limit(self.tolerances["mid_accuracy"].runtime)

        self.solver_settings = {
            "default": default,
            "high_accuracy": high_accuracy,
            "low_accuracy": low_accuracy,
            "mid_accuracy": mid_accuracy,
        }

    def __init__(self):
        """Initialize test set."""
        candidate_solvers = set(
            qpsolvers.sparse_solvers
            if self.sparse_only
            else qpsolvers.available_solvers
        )
        solvers = set(
            solver
            for solver in candidate_solvers
            if SolverSettings.is_implemented(solver)
        )
        for solver in candidate_solvers - solvers:
            logging.warning(
                f"Solver '{solver}' is available but skipped "
                "as its settings are unknown"
            )
        self.known_solver_issues = set()
        self.known_solver_timeouts = {}
        self.solver_settings = {}
        self.solvers = solvers
        self.tolerances = {}

        # Definitions that can be customized by child classes
        self.define_tolerances()
        self.define_solver_settings()

        # Check that in fine settings are consistent
        self.__check_definitions()

    def __check_definitions(self):
        """Check that settings and tolerance definitions are consistent.

        Raises:
            ValueError: in case of inconsistency.
        """
        tolerances = set(self.tolerances.keys())
        settings = set(self.solver_settings.keys())
        if tolerances != settings:
            logging.error("Settings are not consistent with tolerances")
            logging.info(f"Settings: {settings}")
            logging.info(f"Tolerances: {tolerances}")
            raise ValueError("Settings are not consistent with tolerances")

    def count_problems(self) -> int:
        """Count the number of problems in the set.

        Returns:
            Number of problems in the test set.
        """
        nb_problems = 0
        for _ in self:
            nb_problems += 1
        return nb_problems

    def get_problem(self, name: str) -> Optional[Problem]:
        """Get a specific test set problem.

        Args:
            name: Problem name.

        Returns:
            Problem if found, None otherwise.
        """
        for problem in self:
            if problem.name == name:
                return problem
        raise ProblemNotFound(
            f"problem '{name}' not found "
            f"in the {self.__class__.__name__} test set"
        )

    def skip_solver_issue(self, problem: Problem, solver: str) -> bool:
        """Skip known solver issue.

        Args:
            problem: Problem to solve.
            solver: QP solver.

        Returns:
            True if `solver` is known to fail on `problem`.
        """
        if (problem.name, solver) not in self.known_solver_issues:
            return False
        logging.warning(
            "Skipping %s with %s as a known solver issue...",
            problem.name,
            solver,
        )
        return True

    def skip_solver_timeout(
        self, time_limit: float, problem: Problem, solver: str, settings: str
    ) -> bool:
        """Skip known solver timeouts.

        Args:
            time_limit: Time limit in seconds.
            problem: Problem to solve.
            solver: QP solver.
            settings: QP solver settings.

        Note:
            This function only checks for timeouts that the solvers are not
            able to handle by themselves, e.g. for those who do not provide a
            time limit parameter.

        Returns:
            True if `solver` is known to take more than `time_limit` seconds on
            `problem` when using the solver parameters defined in `settings`.
        """
        timeout = (
            self.known_solver_timeouts[(problem.name, solver, settings)]
            if (problem.name, solver, settings) in self.known_solver_timeouts
            else (
                self.known_solver_timeouts[(problem.name, solver, "*")]
                if (problem.name, solver, "*") in self.known_solver_timeouts
                else 0.0
            )
        )
        if timeout > time_limit:
            logging.warning(
                f"Skipping {problem.name} with {solver} at {settings} "
                f"as it is known to take {timeout} > {time_limit} seconds..."
            )
            return True
        return False
