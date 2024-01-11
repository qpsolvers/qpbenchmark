#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2023 Inria

"""Plots for analysis of test set results."""

from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas

from .test_set import TestSet


def plot_metric(
    metric: str,
    df: pandas.DataFrame,
    settings: str,
    test_set: TestSet,
    solvers: Optional[List[str]] = None,
    linewidth: float = 3.0,
    savefig: Optional[str] = None,
    title: Optional[str] = None,
) -> None:
    """Plot comparing solvers on a given metric.

    Args:
        metric: Metric to compare solvers on.
        df: Test set results data frame.
        settings: Settings to compare solvers on.
        test_set: Test set.
        solvers: Names of solvers to compare (default: all).
        linewidth: Width of output lines, in px.
        savefig: If set, save plot to this path rather than displaying it.
        title: Plot title, set to "" to disable.
    """
    assert issubclass(df[metric].dtype.type, np.floating)
    nb_problems = test_set.count_problems()
    settings_df = df[df["settings"] == settings]
    metric_tol = test_set.tolerances[settings].from_metric(metric)
    found_df = settings_df[settings_df["found"]]
    solved_df = found_df[found_df[metric] <= metric_tol]
    plot_solvers: List[str] = (
        solvers if solvers is not None else list(set(solved_df.solver))
    )
    for solver in plot_solvers:
        values = solved_df[solved_df["solver"] == solver][metric].values
        nb_solved = len(values)
        if nb_solved < 1:
            plt.step([0.0, metric_tol], [0.0, 0.0], linewidth=linewidth)
            continue
        sorted_values = np.sort(values)
        y = np.arange(1, 1 + nb_solved)
        last_value = max(metric_tol, sorted_values[-1])
        padded_values = np.hstack([sorted_values, [last_value]])
        padded_y = np.hstack([y, [nb_solved]])
        plt.step(padded_values, padded_y, linewidth=linewidth)
    plt.legend(plot_solvers)
    if title is None:
        plt.title(
            f"Comparing {metric} on {test_set.title} with {settings} settings"
        )
    elif title != "":
        plt.title(title)
    plt.xlabel(metric)
    plt.xscale("log")
    plt.axhline(y=nb_problems, color="gray", linestyle=":")
    plt.axvline(x=metric_tol, color="gray", linestyle=":")
    plt.ylabel("# problems solved")
    plt.grid(True)
    if savefig:
        plt.savefig(fname=savefig)
    else:  # display figure
        plt.show(block=True)
