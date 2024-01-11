#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Shifted geometric mean."""

import numpy as np

from .exceptions import BenchmarkError


def shgeom(v: np.ndarray, sh: float) -> float:
    """`Shifted geometric mean <http://plato.asu.edu/ftp/shgeom.html>`_.

    Args:
        v: Nonnegative values.
        sh: Shift parameter.

    Note:
        The mean is computed as exponential of sum of logs to avoid memory
        overflows. This is common practice.

    Notes:
        Quoting from `A Note on #fairbenchmarking
        <https://community.fico.com/s/blog-post/a5Q2E000000Dt0JUAS/fico1421>`_:
        "The geometric mean of n numbers is defined as the n-th root of their
        product. For the shifted geometric mean, a positive shift value s is
        added to each of the numbers before multiplying them and subtracted
        from the root afterwards. Shifted geometric means have the advantage to
        neither be compromised by very large outliers (in contrast to
        arithmetic means) nor by very small outliers (in contrast to geometric
        means)."
    """
    if (v < 0.0).any():
        raise BenchmarkError(
            "Cannot compute shifted geometric mean, "
            f"negative values detected: {v[v < 0.0]}"
        )
    if sh < 1.0:
        raise BenchmarkError(f"Invalid shift parameter {sh=}")
    return np.exp(np.sum(np.log(v + sh)) / len(v)) - sh
