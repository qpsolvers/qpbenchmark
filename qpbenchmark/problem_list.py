#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

"""List of problems saved to and read from Parquet files."""

from typing import List, Union

import pandas

from .problem import Problem


class ProblemList:
    """List of problems saved to and read from Parquet files."""

    KEYS = ("P", "q", "G", "h", "A", "b", "lb", "ub", "name")

    def __init__(self):
        """Initialize to an empty list."""
        self.data = {key: [] for key in self.KEYS}

    def append(self, problem: Problem) -> None:
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

    def extend(
        self, problem_list: Union["ProblemList", List[Problem]]
    ) -> None:
        """Extend problem list with another.

        Args:
            problem_list: Other problem list.
        """
        if isinstance(problem_list, ProblemList):
            for key in self.KEYS:
                self.data[key].extend(problem_list.data[key])
        elif isinstance(problem_list, list):
            for problem in problem_list:
                self.append(problem)
        else:  # invalid type
            raise TypeError(
                f"problem list has unknown type {type(problem_list)}"
            )

    def to_parquet(self, path: str) -> None:
        """Save sequence of problems to a Parquet file.

        Args:
            path: Path to the Parquet file to save problems to.
        """
        df = pandas.DataFrame(self.data)
        df.to_parquet(
            path,
            engine="pyarrow",
            index=False,
        )
