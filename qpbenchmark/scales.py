# SPDX-License-Identifier: Apache-2.0

"""Magnitudes of the terms involved in optimality conditions.

Rounding errors when evaluating a residual or duality gap are bounded by a
small multiple of the machine epsilon times these magnitudes. See
https://github.com/qpsolvers/qpbenchmark/issues/142 for details.
"""

from typing import Tuple

import numpy as np
import qpsolvers


def _or_zeros(v, n: int) -> np.ndarray:
    """Vector v, or zeros if it is undefined or has the wrong dimension."""
    return np.zeros(n) if v is None or np.shape(v) != (n,) else np.asarray(v)


def _finite_abs(v: np.ndarray) -> np.ndarray:
    """Absolute values of v, with zeros where v is infinite."""
    return np.where(np.isfinite(v), np.abs(v), 0.0)


def compute_scales(
    solution: qpsolvers.Solution,
) -> Tuple[float, float, float]:
    """Compute the scales of the primal residual, dual residual and gap.

    The primal and dual scales are maxima over rows of the absolute values of
    the terms in each row, e.g. ``|A| |x| + |b|``. The duality gap is a single
    sum, so its scale is the sum of the absolute values of all its terms, e.g.
    ``|x|^T |P| |x| + |q|^T |x| + ...``

    Args:
        solution: Solution to evaluate.

    Returns:
        Primal, dual and gap scales, or NaNs if there is no primal vector.
    """
    if solution.x is None:
        return np.nan, np.nan, np.nan
    P, q, G, h, A, b, lb, ub = solution.problem.unpack()
    x = np.abs(solution.x)
    n = x.shape[0]
    primal = [0.0]
    dual = abs(P) @ x + np.abs(q)
    gap = x @ (abs(P) @ x) + np.abs(q) @ x
    if A is not None and b is not None:
        y = np.abs(_or_zeros(solution.y, b.shape[0]))
        primal.append(np.max(abs(A) @ x + np.abs(b), initial=0.0))
        dual += abs(A.T) @ y
        gap += np.abs(b) @ y
    if G is not None and h is not None:
        z = np.abs(_or_zeros(solution.z, h.shape[0]))
        G_rows = np.where(np.isfinite(h), abs(G) @ x + np.abs(h), 0.0)
        primal.append(np.max(G_rows, initial=0.0))
        dual += abs(G.T) @ z
        gap += _finite_abs(h) @ z
    z_box = _or_zeros(solution.z_box, n)
    dual += np.abs(z_box)
    for bound, z_bound in (
        (lb, np.minimum(z_box, 0.0)),
        (ub, np.maximum(z_box, 0.0)),
    ):
        if bound is not None:
            box_rows = np.where(np.isfinite(bound), x + np.abs(bound), 0.0)
            primal.append(np.max(box_rows, initial=0.0))
            gap += _finite_abs(bound) @ np.abs(z_bound)
    return float(max(primal)), float(np.max(dual, initial=0.0)), float(gap)
