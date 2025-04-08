#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Matrix-vector representation of a quadratic program."""

import os
from typing import Optional, Union

import numpy as np
import qpsolvers
import scipy.sparse as spa


def ensure_dense(
    M: Optional[Union[np.ndarray, spa.csc_matrix]],
) -> Optional[np.ndarray]:
    """Get dense representation of a matrix.

    Args:
        M: Matrix to get a dense representation of.

    Returns:
        Dense representation of the matrix.
    """
    if M is None:
        return None
    elif isinstance(M, np.ndarray):
        return M
    else:  # isinstance(M, spa.csc_matrix):
        return M.toarray().astype(float)


def ensure_sparse(
    M: Optional[Union[np.ndarray, spa.csc_matrix]],
) -> Optional[spa.csc_matrix]:
    """Get sparse representation of a matrix.

    Args:
        M: Matrix to get a sparse representation of.

    Returns:
        Sparse representation of the matrix.
    """
    if M is None:
        return None
    elif isinstance(M, np.ndarray):
        return spa.csc_matrix(M)
    else:  # isinstance(M, spa.csc_matrix):
        return M


class Problem(qpsolvers.Problem):
    """Quadratic program.

    Attributes:
        name: Name of the problem, for reporting.
    """

    name: str

    def __init__(
        self,
        P: Union[np.ndarray, spa.csc_matrix],
        q: np.ndarray,
        G: Optional[Union[np.ndarray, spa.csc_matrix]],
        h: Optional[np.ndarray],
        A: Optional[Union[np.ndarray, spa.csc_matrix]],
        b: Optional[np.ndarray],
        lb: Optional[np.ndarray],
        ub: Optional[np.ndarray],
        name: str,
    ):
        """Quadratic program in qpsolvers format."""
        super().__init__(P, q, G, h, A, b, lb, ub)
        self.name = name

    @staticmethod
    def from_qpsolvers(qp: qpsolvers.Problem, name: str) -> "Problem":
        """Stick a name to a generic problem from qpsolvers.

        Args:
            qp: Quadratic program.
            name: Name of the problem.

        Returns:
            Benchmark version of the problem.
        """
        return Problem(
            qp.P,
            qp.q,
            qp.G,
            qp.h,
            qp.A,
            qp.b,
            qp.lb,
            qp.ub,
            name=name,
        )

    def to_dense(self):
        """Return dense version.

        Returns:
            Dense version of the present problem.
        """
        return Problem(
            ensure_dense(self.P),
            self.q,
            ensure_dense(self.G),
            self.h,
            ensure_dense(self.A),
            self.b,
            self.lb,
            self.ub,
            name=self.name,
        )

    def to_sparse(self):
        """Return sparse version.

        Returns:
            Sparse version of the present problem.
        """
        P, G, A = self.P, self.G, self.A
        return Problem(
            ensure_sparse(P),
            self.q,
            ensure_sparse(G),
            self.h,
            ensure_sparse(A),
            self.b,
            self.lb,
            self.ub,
            name=self.name,
        )

    @staticmethod
    def load(file: str):
        """Load problem from file.

        Args:
            file: Path to the file to read.
        """
        name = os.path.splitext(os.path.basename(file))[0]
        loaded = qpsolvers.Problem.load(file)
        return Problem(
            loaded.P,
            loaded.q,
            loaded.G,
            loaded.h,
            loaded.A,
            loaded.b,
            loaded.lb,
            loaded.ub,
            name,
        )
