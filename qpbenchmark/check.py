# SPDX-License-Identifier: Apache-2.0

"""Check that test-set problems are well-formed."""

from collections import Counter
from typing import List, Optional, Union

import numpy as np
import scipy.sparse as spa

from .problem import Problem
from .spdlog import logging
from .test_set import TestSet


def get_values(M: Union[np.ndarray, spa.spmatrix]) -> np.ndarray:
    """Get the array of values stored in a dense or sparse matrix.

    Args:
        M: Dense or sparse matrix.

    Returns:
        Values of a dense matrix, or non-zero values of a sparse matrix.
    """
    return np.asarray(M.data if spa.issparse(M) else M)


def check_matrix(
    name: str,
    M: Union[np.ndarray, spa.spmatrix],
    shape: tuple,
) -> List[str]:
    """Check the shape and values of a problem matrix or vector.

    Args:
        name: Name of the matrix or vector in the problem.
        M: Matrix or vector to check.
        shape: Expected shape.

    Returns:
        List of issues found, empty if there is none.
    """
    issues = []
    if M.shape != shape:
        issues.append(f"{name} has shape {M.shape}, expected {shape}")
    if not np.isfinite(get_values(M)).all():
        issues.append(f"{name} has infinite or NaN values")
    return issues


def check_bound(
    name: str,
    v: np.ndarray,
    shape: tuple,
    disabled: float,
) -> List[str]:
    """Check the shape and values of an inequality-constraint vector.

    Args:
        name: Name of the vector in the problem.
        v: Vector to check.
        shape: Expected shape.
        disabled: Infinite value that disables a constraint, that is
            ``+np.inf`` for upper bounds and ``-np.inf`` for lower bounds.

    Returns:
        List of issues found, empty if there is none.
    """
    issues = []
    if v.shape != shape:
        issues.append(f"{name} has shape {v.shape}, expected {shape}")
    if np.isnan(v).any():
        issues.append(f"{name} has NaN values")
    if (v == -disabled).any():
        issues.append(
            f"{name} has {-disabled} values, only {disabled} values "
            "are allowed to disable constraints"
        )
    return issues


def check_constraint(
    matrix_name: str,
    M: Optional[Union[np.ndarray, spa.spmatrix]],
    vector_name: str,
    v: Optional[np.ndarray],
    n: int,
    disabled: Optional[float] = None,
) -> List[str]:
    """Check a linear constraint defined by a matrix and a vector.

    Args:
        matrix_name: Name of the constraint matrix in the problem.
        M: Constraint matrix.
        vector_name: Name of the constraint vector in the problem.
        v: Constraint vector.
        n: Number of optimization variables.
        disabled: Infinite value that disables an inequality constraint, or
            None for an equality constraint.

    Returns:
        List of issues found, empty if there is none.
    """
    if M is None and v is None:
        return []
    if M is None:
        return [f"{vector_name} is set but {matrix_name} is missing"]
    if v is None:
        return [f"{matrix_name} is set but {vector_name} is missing"]
    m = M.shape[0]
    issues = check_matrix(matrix_name, M, (m, n))
    if disabled is None:
        issues.extend(check_matrix(vector_name, v, (m,)))
    else:
        issues.extend(check_bound(vector_name, v, (m,), disabled))
    return issues


def check_problem(problem: Problem) -> List[str]:
    """Check that a problem is well-formed.

    Matrices and vectors should have consistent dimensions, and their values
    should be finite. Infinite values are allowed in inequality vectors to
    disable the corresponding constraints, that is, ``+np.inf`` in ``h`` and
    ``ub``, and ``-np.inf`` in ``lb``.

    Args:
        problem: Problem to check.

    Returns:
        List of issues found, empty if the problem is well-formed.
    """
    if problem.q.ndim != 1:
        return [f"q has shape {problem.q.shape}, expected a flat vector"]
    n = problem.q.shape[0]
    issues = check_matrix("P", problem.P, (n, n))
    issues.extend(check_matrix("q", problem.q, (n,)))
    issues.extend(
        check_constraint("G", problem.G, "h", problem.h, n, disabled=np.inf)
    )
    issues.extend(check_constraint("A", problem.A, "b", problem.b, n))
    if problem.lb is not None:
        issues.extend(check_bound("lb", problem.lb, (n,), -np.inf))
    if problem.ub is not None:
        issues.extend(check_bound("ub", problem.ub, (n,), np.inf))
    return issues


def check_test_set(test_set: TestSet) -> List[str]:
    """Check that all problems in a test set are well-formed.

    Args:
        test_set: Test set to check.

    Returns:
        List of issues found, each prefixed by the name of its problem, or
        empty if all problems are well-formed.
    """
    issues: List[str] = []
    names: Counter = Counter()
    for problem in test_set:
        names[problem.name] += 1
        issues.extend(
            f"{problem.name}: {issue}" for issue in check_problem(problem)
        )
    for name, count in names.items():
        if count > 1:
            issues.append(f"{name}: problem name appears {count} times")
    logging.info(
        "Checked %d problems from the %s test set",
        sum(names.values()),
        test_set.__class__.__name__,
    )
    return issues
