# SPDX-License-Identifier: Apache-2.0

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
        rounding: Factor ``c`` of the floating-point rounding floor added to
            the primal, dual and gap tolerances. A metric with tolerance
            ``tol`` passes when it is below ``tol + c * eps * scale``, where
            ``eps`` is the machine epsilon and ``scale`` is the magnitude of
            the terms involved in evaluating the metric (see
            ``qpbenchmark.scales``). This floor is negligible on well-scaled
            problems, and avoids requiring more accuracy than double
            precision can resolve on badly-scaled ones.
    """

    primal: float
    dual: float
    gap: float
    runtime: float
    rounding: float = 10.0

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
