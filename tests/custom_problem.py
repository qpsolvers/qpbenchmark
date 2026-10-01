# SPDX-License-Identifier: Apache-2.0

"""Small QP problem used in unit tests."""

import numpy as np

import qpbenchmark


def custom_problem(name: str) -> qpbenchmark.Problem:
    """Build an unconstrained three-dimensional QP problem.

    Args:
        name: Name of the problem.

    Returns:
        Problem with an identity cost matrix and no constraints.
    """
    return qpbenchmark.Problem(
        P=np.eye(3),
        q=np.ones(3),
        G=None,
        h=None,
        A=None,
        b=None,
        lb=None,
        ub=None,
        name=name,
    )
