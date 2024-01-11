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

    def to_dense(self):
        """Return dense version.

        Returns:
            Dense version of the present problem.
        """
        return Problem(
            self.P.toarray().astype(float),
            self.q,
            self.G.toarray().astype(float) if self.G is not None else None,
            self.h,
            self.A.toarray().astype(float) if self.A is not None else None,
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
            spa.csc_matrix(P) if isinstance(P, np.ndarray) else P,
            self.q,
            spa.csc_matrix(G) if isinstance(G, np.ndarray) else G,
            self.h,
            spa.csc_matrix(A) if isinstance(A, np.ndarray) else A,
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
