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

from typing import List

import matplotlib.pyplot as plt
import numpy as np
import pandas


def hist_metric(
    metric: str,
    df: pandas.DataFrame,
    settings: str,
    solvers: List[str] = [],
    nb_bins: int = 10,
    test_set: str = "",
    alpha: float = 0.5,
) -> None:
    found_df = df[df["found"]]
    settings_df = found_df[found_df["settings"] == settings]
    solvers = set(solvers if solvers else settings_df.solver)
    for solver in solvers:
        values = settings_df[settings_df["solver"] == solver][metric].values
        hist, bins = np.histogram(values, bins=nb_bins)
        logbins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
        plt.hist(values, bins=logbins, cumulative=True, alpha=0.5)
    plt.legend(solvers)
    plt.title(f"Comparing {metric} on {test_set} test set")
    plt.xlabel(metric)
    plt.xscale("log")
    plt.ylabel("# problems solved")
    plt.show(block=True)
