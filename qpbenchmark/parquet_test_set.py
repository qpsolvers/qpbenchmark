#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024

"""Test set read from a Parquet file."""

from pathlib import Path
from typing import Iterator, Union

import numpy as np
import pandas

from .problem import Problem
from .problem_list import ProblemList
from .test_set import TestSet


class ParquetTestSet(TestSet):
    """Test set read from a Parquet file."""

    def __init__(self, path: Union[Path, str]):
        """Initialize test set.

        Args:
            path: Path to Parquet file to read problems from.
        """
        super().__init__()
        self.__df = pandas.read_parquet(path, engine="pyarrow")

    def __iter__(self) -> Iterator[Problem]:
        """Yield test-set problems one by one."""
        for _, row in self.__df.iterrows():
            n = row["q"].size
            pb_data = {}
            for key in ProblemList.KEYS:
                if isinstance(row[key], np.ndarray):
                    # Make a copy as DAQP doesn't support read-only inputs
                    # TODO(scaron): check separately and report an issue
                    pb_data[key] = row[key].copy()
                    if key in ("P", "G", "A"):
                        m = pb_data[key].size // n
                        pb_data[key] = pb_data[key].reshape((m, n))
                else:  # string or None
                    pb_data[key] = row[key]
            yield Problem(**pb_data)
