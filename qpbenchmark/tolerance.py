#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Tolerances on solver solution validation."""

from dataclasses import dataclass

from .exceptions import BenchmarkError


@dataclass
class Tolerance:
    """Tolerances on solver solution validation.

    Attributes:
        primal: Tolerance on primal residuals.
        dual: Tolerance on dual residuals.
        gap: Tolerance on duality gaps.
        runtime: Time limit in seconds.
    """

    primal: float
    dual: float
    gap: float
    runtime: float

    def from_metric(self, metric: str) -> float:
        """Get tolerance corresponding to a given metric.

        Args:
            metric: Metric to get the tolerance of.

        Returns:
            Corresponding tolerance.
        """
        if metric == "primal_residual":
            return self.primal
        if metric == "dual_residual":
            return self.dual
        if metric == "duality_gap":
            return self.gap
        if metric == "runtime":
            return self.runtime
        raise BenchmarkError(f"unknown metric '{metric}'")
