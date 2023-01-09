#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Inria
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Plots for analysis of test set results.
"""

from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas

from .test_set import TestSet


def hist(
    metric: str,
    df: pandas.DataFrame,
    settings: str,
    test_set: TestSet,
    solvers: Optional[List[str]] = None,
    nb_bins: int = 10,
    alpha: float = 0.5,
) -> None:
    """
    Histogram comparing solvers on a given metric.

    Args:
        metric: Metric to compare solvers on.
        df: Test set results data frame.
        settings: Settings to compare solvers on.
        test_set: Test set.
        solvers: Names of solvers to compare (default: all).
        nb_bins: Number of bins in the histogram.
        alpha: Histogram transparency.
    """
    settings_df = df[df["settings"] == settings]
    hist_df = settings_df.assign(
        **{
            metric: settings_df[metric].mask(
                ~settings_df["found"],
                test_set.tolerances[settings].from_metric(metric),
            ),
        }
    )
    plot_solvers: List[str] = (
        solvers if solvers is not None else list(set(hist_df.solver))
    )
    for solver in plot_solvers:
        values = hist_df[hist_df["solver"] == solver][metric].values
        _, bins = np.histogram(values, bins=nb_bins)
        logbins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
        plt.hist(values, bins=logbins, cumulative=True, alpha=alpha)
    plt.legend(plot_solvers)
    plt.title(
        f"Comparing {metric} on {test_set.title} with {settings} settings"
    )
    plt.xlabel(metric)
    plt.xscale("log")
    plt.ylabel("# problems solved")
    plt.show(block=True)
