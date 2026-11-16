# SPDX-License-Identifier: Apache-2.0

"""Magnitudes involved in the evaluation of optimality conditions.

Residuals and duality gaps are evaluated in floating-point arithmetic, from
primal and dual vectors that are themselves rounded to floating-point numbers.
The rounding error in each evaluation is bounded by a small multiple of the
machine epsilon times the magnitudes of the terms involved. The functions in
this module compute these magnitudes, so that tolerance checks can account for
the resolution of floating-point arithmetic. See issue #142 for details:
https://github.com/qpsolvers/qpbenchmark/issues/142
"""

from typing import Optional

import numpy as np
import qpsolvers


def _abs_dot(M, v: np.ndarray) -> np.ndarray:
    """Compute :math:`|M| |v|` for a dense or sparse matrix M.

    Args:
        M: Dense or sparse matrix.
        v: Vector.

    Returns:
        Product of the elementwise absolute values of M and v.
    """
    return np.asarray(abs(M).dot(np.abs(v))).flatten()


def _max_or_zero(v: np.ndarray) -> float:
    """Maximum of a vector, or zero if the vector is empty.

    Args:
        v: Vector.

    Returns:
        Maximum value, or zero for an empty vector.
    """
    return float(np.max(v)) if v.size > 0 else 0.0


def _vector_or_zeros(v: Optional[np.ndarray], n: int) -> np.ndarray:
    """Return a vector, or zeros if it is undefined.

    Some solvers return empty dual vectors for constraints that are not in
    the problem, so that we also return zeros when dimensions do not match.

    Args:
        v: Vector, or None.
        n: Expected dimension of the vector.

    Returns:
        The vector v if it has dimension n, zeros otherwise.
    """
    if v is None or np.asarray(v).shape != (n,):
        return np.zeros(n)
    return np.asarray(v)


def primal_scale(solution: qpsolvers.Solution) -> float:
    r"""Compute the magnitude of terms in the primal residual.

    The primal scale is the maximum over constraint rows of:

    .. math::

        |A| |x| + |b|, \quad |G| |x| + |h|, \quad |x| + |lb|, \quad |x| + |ub|

    where box rows with infinite bounds are skipped.

    Args:
        solution: Solution to evaluate.

    Returns:
        Primal scale, or NaN if the solution has no primal vector.
    """
    if solution.x is None:
        return np.nan
    _, _, G, h, A, b, lb, ub = solution.problem.unpack()
    x = np.asarray(solution.x)
    scales = [0.0]
    if A is not None:
        scales.append(_max_or_zero(_abs_dot(A, x) + np.abs(b)))
    if G is not None:
        finite = np.isfinite(h)
        scales.append(_max_or_zero((_abs_dot(G, x) + np.abs(h))[finite]))
    for bound in (lb, ub):
        if bound is not None:
            finite = np.isfinite(bound)
            scales.append(
                _max_or_zero(np.abs(x[finite]) + np.abs(bound[finite]))
            )
    return max(scales)


def dual_scale(solution: qpsolvers.Solution) -> float:
    r"""Compute the magnitude of terms in the dual residual.

    The dual scale is the maximum over components of:

    .. math::

        |P| |x| + |q| + |A^T| |y| + |G^T| |z| + |z_{box}|

    Args:
        solution: Solution to evaluate.

    Returns:
        Dual scale, or NaN if the solution has no primal vector.
    """
    if solution.x is None:
        return np.nan
    P, q, G, _, A, _, _, _ = solution.problem.unpack()
    x = np.asarray(solution.x)
    n = x.shape[0]
    scale = _abs_dot(P, x) + np.abs(q)
    if A is not None:
        scale += _abs_dot(A.T, _vector_or_zeros(solution.y, A.shape[0]))
    if G is not None:
        scale += _abs_dot(G.T, _vector_or_zeros(solution.z, G.shape[0]))
    scale += np.abs(_vector_or_zeros(solution.z_box, n))
    return _max_or_zero(scale)


def gap_scale(solution: qpsolvers.Solution) -> float:
    r"""Compute the magnitude of terms in the duality gap.

    The duality gap is a single sum, so its scale is the sum of the absolute
    values of all its terms:

    .. math::

        |x|^T |P| |x| + |q|^T |x| + |b|^T |y| + |h|^T |z|
        + |lb|^T |z_{box}^-| + |ub|^T |z_{box}^+|

    where box terms with infinite bounds are skipped. These terms cancel each
    other at the optimum, so that the gap scale can be much larger than the
    objective value.

    Args:
        solution: Solution to evaluate.

    Returns:
        Gap scale, or NaN if the solution has no primal vector.
    """
    if solution.x is None:
        return np.nan
    P, q, G, h, A, b, lb, ub = solution.problem.unpack()
    x = np.asarray(solution.x)
    abs_x = np.abs(x)
    scale = float(abs_x.dot(_abs_dot(P, x))) + float(np.abs(q).dot(abs_x))
    if A is not None:
        y = _vector_or_zeros(solution.y, b.shape[0])
        scale += float(np.abs(b).dot(np.abs(y)))
    if G is not None:
        z = _vector_or_zeros(solution.z, h.shape[0])
        finite = np.isfinite(h)
        scale += float(np.abs(h[finite]).dot(np.abs(z[finite])))
    if lb is not None or ub is not None:
        z_box = _vector_or_zeros(solution.z_box, x.shape[0])
        for bound, z_bound in (
            (lb, np.minimum(z_box, 0.0)),
            (ub, np.maximum(z_box, 0.0)),
        ):
            if bound is not None:
                finite = np.isfinite(bound)
                scale += float(
                    np.abs(bound[finite]).dot(np.abs(z_bound[finite]))
                )
    return scale
