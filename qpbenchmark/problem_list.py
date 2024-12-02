#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""List of problems saved to and read from Parquet files."""

from pathlib import Path
from typing import Iterator, Union

import numpy as np
import pandas

from .problem import Problem


class ProblemList:

    KEYS = ("P", "q", "G", "h", "A", "b", "lb", "ub", "name")

    def __init__(self):
        """Initialize to an empty list."""
        self.data = {key: [] for key in self.KEYS}

    def append(self, problem: Problem):
        """Append a problem to the list.

        Args:
            problem: Problem to append.
            time: Optional time (in seconds) corresponding to the problem.
        """
        for key in self.KEYS:
            value = problem.__dict__[key]
            if hasattr(value, "flatten"):  # only for NumPy arrays
                value = value.flatten()
            self.data[key].append(value)

    def to_parquet(self, path: str) -> None:
        """Save sequence of problems to a Parquet file.

        Args:
            path: Path to the Parquet file to save problems to.
        """
        df = pandas.DataFrame(self.data)
        df.to_parquet(
            path,
            engine="pyarrow",
            index=None,  # save the RangeIndex as a range
        )

    @classmethod
    def yield_from_parquet(cls, path: Union[str, Path]) -> Iterator[Problem]:
        """Yield sequence of problems from a Parquet file.

        Args:
            file: Path to the Parquet file to read problems from.

        Yields:
            Problem object read from file.
        """
        df = pandas.read_parquet(path, engine="pyarrow")
        for index, row in df.iterrows():
            n = row["q"].size
            pb_data = {}
            for key in cls.KEYS:
                if isinstance(row[key], np.ndarray):
                    # Make a copy as DAQP doesn't support read-only inputs
                    # TODO(scaron): check separately and report an issue
                    pb_data[key] = row[key].copy()
                    if key in ("P", "G", "A"):
                        m = pb_data[key].size // n
                        pb_data[key] = pb_data[key].reshape((m, n))
                else:  # name or None values
                    pb_data[key] = row[key]
            yield Problem(**pb_data)
