#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Report written from test set results."""

import datetime
import io
from importlib import metadata
from typing import Dict

import pandas

from .results import Results
from .solver_settings import SolverSettings
from .spdlog import logging
from .test_set import TestSet
from .utils import (
    capitalize_settings,
    get_cpu_info_summary,
    get_cpu_info_table,
    get_gpu_info_summary,
    get_solver_versions,
)
from .version import get_version


class Report:
    """Report generated from benchmark results.

    Attributes:
        author: GitHub username of the person who generated the report.
        results: Results from which the report should be generated.
        solver_settings: Dictionary of solver parameters for each settings.
        test_set: Test set from which results were generated.
    """

    # pylint: disable=R0902
    # Reports are big and linear, thus with many instance attributes.

    __correct_rate_df: pandas.DataFrame
    __dual_df: pandas.DataFrame
    __gap_df: pandas.DataFrame
    __primal_df: pandas.DataFrame
    __runtime_df: pandas.DataFrame
    __success_rate_df: pandas.DataFrame
    author: str
    results: Results
    solver_settings: Dict[str, SolverSettings]
    test_set: TestSet

    def __init__(self, author: str, results: Results):
        """Initialize report.

        Args:
            author: GitHub username of the person who generated the report.
            results: Results from which the report should be generated.
        """
        self.__correct_rate_df = pandas.DataFrame()
        self.__dual_df = pandas.DataFrame()
        self.__gap_df = pandas.DataFrame()
        self.__primal_df = pandas.DataFrame()
        self.__runtime_df = pandas.DataFrame()
        self.__success_rate_df = pandas.DataFrame()
        self.author = author
        self.results = results
        self.solver_settings = results.test_set.solver_settings
        self.test_set = results.test_set

    def get_tolerances_table(self) -> str:
        """Get tolerances Markdown table.

        Returns:
            Tolerances Markdown table.
        """
        names = list(self.test_set.tolerances.keys())
        df = pandas.DataFrame(
            [],
            columns=["tolerance"] + names,
        )
        tolerances = ["primal", "dual", "gap", "runtime"]
        for tolerance in tolerances:
            row = {
                "tolerance": [f"``{tolerance}``"],
            }
            row.update(
                {
                    name: [self.test_set.tolerances[name].__dict__[tolerance]]
                    for name in names
                }
            )
            row_df = pandas.DataFrame(row)
            df = (
                row_df
                if df.empty
                else pandas.concat(
                    [
                        df,
                        row_df,
                    ],
                    ignore_index=True,
                )
            )
        df = df.sort_values(by="tolerance")
        return df.to_markdown(index=False)

    def get_solver_settings_table(self) -> str:
        """Get Markdown table for solver settings.

        Returns:
            Solver settings Markdown table.
        """
        solver_settings = self.test_set.solver_settings
        names = list(solver_settings.keys())
        df = pandas.DataFrame(
            [],
            columns=["solver", "parameter"] + names,
        )
        keys = set()
        for name, settings in solver_settings.items():
            for solver in settings.solvers:
                if solver not in self.test_set.solvers:
                    # Skip solvers that are configured but not in test set
                    continue
                for param in settings[solver]:
                    keys |= {(solver, param)}
        for solver, param in keys:
            row = {
                "solver": [solver],
                "parameter": [
                    f"``{str(param) if isinstance(param, bool) else param}``"
                ],
            }
            row.update(
                {
                    name: [solver_settings[name].get_param(solver, param, "-")]
                    for name in names
                }
            )
            row_df = pandas.DataFrame(row)
            df = (
                row_df
                if df.empty
                else pandas.concat(
                    [
                        df,
                        row_df,
                    ],
                    ignore_index=True,
                )
            )
        df = df.sort_values(by=["solver", "parameter"])
        return df.to_markdown(index=False)

    def get_solver_versions_table(self):
        """Get Markdown table for solver versions.

        Returns:
            Solver versions Markdown table.
        """
        versions = get_solver_versions(self.test_set.solvers)
        versions_df = pandas.DataFrame(
            {
                "solver": list(versions.keys()),
                "version": list(versions.values()),
            },
        )
        versions_df = versions_df.set_index("solver")
        versions_df = versions_df.sort_index()
        versions_table = versions_df.to_markdown(index=True)
        return versions_table

    def __compute_dataframes(self) -> None:
        """Compute dataframes used in the report."""
        primal_tolerances = {
            name: tolerance.primal
            for name, tolerance in self.test_set.tolerances.items()
        }
        dual_tolerances = {
            name: tolerance.dual
            for name, tolerance in self.test_set.tolerances.items()
        }
        gap_tolerances = {
            name: tolerance.gap
            for name, tolerance in self.test_set.tolerances.items()
        }
        runtime_tolerances = {
            name: tolerance.runtime
            for name, tolerance in self.test_set.tolerances.items()
        }
        self.__success_rate_df = self.results.build_success_rate_df(
            primal_tolerances,
            dual_tolerances,
            gap_tolerances,
        )
        self.__correct_rate_df = self.results.build_correct_rate_df(
            primal_tolerances,
            dual_tolerances,
            gap_tolerances,
        )
        self.__runtime_df = self.results.build_shgeom_df(
            metric="runtime",
            shift=10.0,
            not_found_values=runtime_tolerances,
        )
        self.__primal_df = self.results.build_shgeom_df(
            metric="primal_residual",
            shift=10.0,
            not_found_values=primal_tolerances,
        )
        self.__dual_df = self.results.build_shgeom_df(
            metric="dual_residual",
            shift=10.0,
            not_found_values=dual_tolerances,
        )
        self.__gap_df = self.results.build_shgeom_df(
            metric="duality_gap",
            shift=10.0,
            not_found_values=gap_tolerances,
        )

    def write(self, path: str) -> None:
        """Write report to a given path.

        Args:
            path: Path to the Markdown file to write the report to.

        Note:
            We make sure each table in the report is preceded by a single line
            title, for instance "Precentage of problems each solver is able to
            solve:". This comes in handy for ``@@`` anchorage when doing the
            ``diff`` of two reports.
        """
        assert path.endswith(".md")
        self.__compute_dataframes()
        with open(path, "w", encoding="UTF-8") as fh:
            self.__write_header(fh)
            self.__write_toc(fh)
            self.__write_description(fh)
            self.__write_solvers_section(fh)
            self.__write_cpu_info_section(fh)
            self.__write_settings_section(fh)
            self.__write_limitations_section(fh)
            self.__write_results_by_settings(fh)
            self.__write_results_by_metric(fh)
        logging.info(f"Wrote report to {path}")

    def __write_header(self, fh: io.TextIOWrapper) -> None:
        """Write report header.

        Args:
            fh: Output file handle.
        """
        nb_problems = len(set(self.results.df["problem"]))
        benchmark_version = get_version()
        cpu_info_summary = get_cpu_info_summary()
        gpu_info_summary = get_gpu_info_summary()
        optional_gpu_line = (
            f"\n| GPU                | {gpu_info_summary} |"
            if gpu_info_summary
            else ""
        )
        date = str(datetime.datetime.now(datetime.timezone.utc))
        fh.write(
            f"""# {self.test_set.title}

| Number of problems | {nb_problems} |
|:-------------------|:--------------------|
| Benchmark version  | {benchmark_version} |
| Date               | {date} |
| CPU                | [{cpu_info_summary}](#cpu-info) |{optional_gpu_line}
| Run by             | [@{self.author}](https://github.com/{self.author}/) |

"""
        )
        fh.write(
            "Benchmark reports are copious as we aim to document "
            "comparison factors as much as possible. You can also "
            "[jump to results](#results-by-settings) directly.\n\n"
        )

    def __write_toc(self, fh: io.TextIOWrapper) -> None:
        """Write table of contents.

        Args:
            fh: Output file handle.
        """
        fh.write("## Contents\n\n")
        if self.test_set.description is not None:
            fh.write("* [Description](#description)\n")
        fh.write(
            """* [Solvers](#solvers)
* [Settings](#settings)
* [CPU info](#cpu-info)
* [Known limitations](#known-limitations)
* [Results by settings](#results-by-settings)\n"""
        )
        for name in self.solver_settings:
            link = name.replace("_", "-")
            fh.write(f"    * [{capitalize_settings(name)}](#{link})\n")
        fh.write(
            """* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)\n\n"""
        )

    def __write_description(self, fh: io.TextIOWrapper) -> None:
        """Write optional Description section.

        Args:
            fh: Output file handle.
        """
        if self.test_set.description is not None:
            fh.write(f"## Description\n\n{self.test_set.description}\n\n")

    def __write_solvers_section(self, fh: io.TextIOWrapper) -> None:
        """Write Solvers section.

        Args:
            fh: Output file handle.
        """
        qpsolvers_version = metadata.version("qpsolvers")
        fh.write("## Solvers\n\n")
        fh.write(f"{self.get_solver_versions_table()}\n\n")
        fh.write(
            "All solvers were called via "
            "[qpsolvers](https://github.com/qpsolvers/qpsolvers) "
            f"v{qpsolvers_version}.\n\n"
        )

    def __write_cpu_info_section(self, fh: io.TextIOWrapper) -> None:
        """Write CPU info section.

        Args:
            fh: Output file handle.
        """
        fh.write(f"## CPU info\n\n{get_cpu_info_table()}\n")

    def __write_settings_section(self, fh: io.TextIOWrapper) -> None:
        """Write Settings section.

        Args:
            fh: Output file handle.
        """
        italics_settings = [f"*{x}*" for x in self.solver_settings]
        fh.write("## Settings\n\n")
        fh.write(
            f"There are {len(italics_settings)} settings: "
            f'{", ".join(italics_settings[:-1])} '
            f"and {italics_settings[-1]}. "
            "They validate solutions using the following tolerances:\n\n"
        )
        fh.write(f"{self.get_tolerances_table()}\n\n")
        fh.write("Solvers for each settings are configured as follows:\n\n")
        fh.write(f"{self.get_solver_settings_table()}\n\n")

    def __write_limitations_section(self, fh: io.TextIOWrapper) -> None:
        """Write Known limitations section.

        Args:
            fh: Output file handle.
        """
        repo = "https://github.com/qpsolvers/qpbenchmark"
        fh.write("## Known limitations\n\n")
        fh.write(
            "The following "
            f"[issues]({repo}/issues) have "
            "been identified as impacting the fairness of this benchmark. "
            "Keep them in mind when drawing conclusions from the results.\n\n"
        )
        for number, desc in (
            (60, "Conversion to SOCP limits performance of ECOS"),
            (88, "CPU thermal throttling"),
        ):
            link = f"{repo}/issues/{number}"
            fh.write(f"- [#{number}]({link}): {desc}\n")
        fh.write("\n")

    def __write_results_by_settings(self, fh: io.TextIOWrapper) -> None:
        """Write Results by settings.

        Args:
            fh: Output file handle.
        """
        fh.write("""## Results by settings\n\n""")
        for settings in self.solver_settings:
            cols = {
                "[Success rate](#success-rate) (%)": self.__success_rate_df[
                    settings
                ],
                "[Runtime](#computation-time) (shm)": self.__runtime_df[
                    settings
                ],
                "[Primal residual](#primal-residual) (shm)": self.__primal_df[
                    settings
                ],
                "[Dual residual](#dual-residual) (shm)": self.__dual_df[
                    settings
                ],
                "[Duality gap](#duality-gap) (shm)": self.__gap_df[settings],
            }
            df = pandas.DataFrame([], index=self.__gap_df.index).assign(**cols)
            repo = "https://github.com/qpsolvers/qpbenchmark"
            shm_desc = (
                "Solvers are compared over the whole test set by "
                f"[shifted geometric mean]({repo}#shifted-geometric-mean) "
                "(shm). Lower is better, 1.0 is the best."
            )
            fh.write(f"### {capitalize_settings(settings)}\n\n")
            fh.write(f"{shm_desc}\n\n")
            fh.write(f'{df.to_markdown(index=True, floatfmt=".1f")}\n\n')

    def __write_results_by_metric(self, fh: io.TextIOWrapper) -> None:
        """Write Results by metric.

        Args:
            fh: Output file handle.
        """
        repo = "https://github.com/qpsolvers/qpbenchmark"

        fh.write("## Results by metric\n\n")
        fh.write("### Success rate\n\n")
        fh.write("Precentage of problems each solver is able to solve:\n\n")

        success_rate_table = self.__success_rate_df.to_markdown(
            index=True, floatfmt=".0f"
        )
        fh.write(f"{success_rate_table}\n\n")

        success_rate_table_desc = (
            "Rows are [solvers](#solvers) and "
            "columns are [settings](#settings). "
            "We consider that a solver successfully solved a problem when "
            "(1) it returned with a success status and "
            "(2) its solution satisfies optimality conditions "
            "within [tolerance](#settings). "
            "The second table below summarizes the frequency at which solvers "
            "return success (1) and the corresponding solution did indeed "
            "pass tolerance checks."
        )

        fh.write(f"{success_rate_table_desc}\n\n")
        fh.write(
            'Percentage of problems where "solved" return '
            "codes are correct:\n\n"
        )

        correct_rate_table = self.__correct_rate_df.to_markdown(
            index=True, floatfmt=".0f"
        )

        fh.write(f"{correct_rate_table}\n\n")
        fh.write("### Computation time\n\n")

        comp_times_shm_desc = (
            "We compare solver computation times over the whole test set "
            "using the shifted geometric mean. Intuitively, a solver with a "
            "shifted-geometric-mean runtime of Y is Y times slower than the "
            "best solver over the test set. "
            f"See [Metrics]({repo}#metrics) for details."
        )

        fh.write(f"{comp_times_shm_desc}\n\n")
        fh.write(
            "Shifted geometric mean of solver computation times "
            "(1.0 is the best):\n\n"
        )
        fh.write(
            f'{self.__runtime_df.to_markdown(index=True, floatfmt=".1f")}\n\n'
        )

        comp_times_table_desc = (
            "Rows are solvers and columns are solver settings. "
            "The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, "
            "we assume a solver's run time is at the "
            "[time limit](#settings) when it fails to solve a problem."
        )

        fh.write(f"{comp_times_table_desc}\n\n")
        fh.write("### Optimality conditions\n\n")
        fh.write("#### Primal residual\n\n")

        primal_residual_shm_desc = (
            "The primal residual measures the maximum "
            "(equality and inequality) constraint violation in the solution "
            "returned by a solver. We use the shifted geometric mean to "
            "compare solver primal residuals over the whole test set. "
            "Intuitively, a solver with a shifted-geometric-mean primal "
            "residual of Y is Y times less precise on constraints than the "
            "best solver over the test set. "
            f"See [Metrics]({repo}#metrics) for details."
        )

        fh.write(f"{primal_residual_shm_desc}\n\n")
        fh.write(
            "Shifted geometric means of primal residuals "
            "(1.0 is the best):\n\n"
        )
        fh.write(
            f'{self.__primal_df.to_markdown(index=True, floatfmt=".1f")}\n\n'
        )

        primal_residual_table_desc = (
            "Rows are solvers and columns are solver settings. "
            "The shift is $sh = 10$. A solver that fails to find a solution "
            "receives a primal residual equal to the full "
            "[primal tolerance](#settings)."
        )

        fh.write(f"{primal_residual_table_desc}\n\n")
        fh.write("#### Dual residual\n\n")

        dual_residual_shm_desc = (
            "The dual residual measures the maximum violation of the dual "
            "feasibility condition in the solution returned by a solver. "
            "We use the shifted geometric mean to compare solver dual "
            "residuals over the whole test set. Intuitively, a solver with "
            "a shifted-geometric-mean dual residual of Y is Y times less "
            "precise on the dual feasibility condition than the best solver "
            "over the test set. "
            f"See [Metrics]({repo}#metrics) for details."
        )

        fh.write(f"{dual_residual_shm_desc}\n\n")
        fh.write(
            "Shifted geometric means of dual residuals "
            "(1.0 is the best):\n\n"
        )
        fh.write(
            f'{self.__dual_df.to_markdown(index=True, floatfmt=".1f")}\n\n'
        )

        dual_residual_table_desc = (
            "Rows are solvers and columns are solver settings. "
            "The shift is $sh = 10$. A solver that fails to find a solution "
            "receives a dual residual equal to the full "
            "[dual tolerance](#settings)."
        )

        fh.write(f"{dual_residual_table_desc}\n\n")
        fh.write("#### Duality gap\n\n")

        duality_gap_shm_desc = (
            "The duality gap measures the consistency of the primal "
            "and dual solutions returned by a solver. "
            "A duality gap close to zero ensures that the complementarity "
            "slackness optimality condition is satisfied. We use the "
            "shifted geometric mean to compare solver duality gaps over "
            "the whole test set. Intuitively, a solver with a "
            "shifted-geometric-mean duality gap of Y is Y times "
            "less precise on the complementarity slackness condition than "
            "the best solver over the test set. "
            f"See [Metrics]({repo}#metrics) for details."
        )

        fh.write(f"{duality_gap_shm_desc}\n\n")
        fh.write(
            "Shifted geometric means of duality gaps " "(1.0 is the best):\n\n"
        )
        fh.write(
            f'{self.__gap_df.to_markdown(index=True, floatfmt=".1f")}\n\n'
        )

        duality_gap_table_desc = (
            "Rows are solvers and columns are solver settings. "
            "The shift is $sh = 10$. A solver that fails to find a solution "
            "receives a duality gap equal to the full "
            "[gap tolerance](#settings)."
        )

        fh.write(f"{duality_gap_table_desc}")
        fh.write("\n")  # newline at end of file
