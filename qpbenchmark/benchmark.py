#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2022 Stéphane Caron

"""Main script for the `qpbenchmark` command-line utility.

It provides tools to benchmark different Quadratic Programming (QP) solvers.
"""

import argparse
import os
import sys
from importlib import import_module  # type: ignore
from pathlib import Path
from typing import Optional, Union

import qpsolvers

from .exceptions import BenchmarkError
from .plot_metric import plot_metric
from .report import Report
from .results import Results
from .run import run
from .spdlog import logging
from .test_set import TestSet


def parse_command_line_arguments(
    test_set_path: Optional[Union[Path, str]] = None,
) -> argparse.Namespace:
    """Extracts and interprets command line arguments passed to the script.

    Args:
        test_set_path: If set, don't add test set path argument.

    Returns:
        args: arguments of the command line.
    """
    parser = argparse.ArgumentParser(
        description="Benchmark quadratic programming solvers"
    )
    if test_set_path is None:
        parser.add_argument(
            "test_set_path", help="path to the test set Python source"
        )
    parser.add_argument(
        "--results-path",
        help="path to a specific results CSV file to work with",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="verbose mode",
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        default=False,
        action="store_true",
        help="even more verbose than the verbose mode",
    )
    subparsers = parser.add_subparsers(
        title="command", dest="command", required=True
    )

    # check_problem
    parser_check_problem = subparsers.add_parser(
        "check_problem",
        help="analyze a given problem in interactive mode",
    )
    parser_check_problem.add_argument(
        "problem",
        help="name of the problem in the test set",
    )

    # check_results
    subparsers.add_parser(
        "check_results",
        help="evaluate test set results interactively",
    )

    # list_problems
    subparsers.add_parser(
        "list_problems",
        help="list all problems contained in the test set",
    )

    # plot
    parser_plot = subparsers.add_parser(
        "plot",
        help="compare how solvers performed on a given metric",
    )
    parser_plot.add_argument(
        "metric",
        help='name of the metric to evaluate (e.g. "duality_gap")',
    )
    parser_plot.add_argument(
        "settings",
        help='settings to compare solvers on (e.g. "high_accuracy")',
    )
    parser_plot.add_argument(
        "--linewidth",
        help="width of plotted lines in px",
        type=int,
        default=3,
    )
    parser_plot.add_argument(
        "--savefig",
        help="path to a file to save the plot to (rather than displaying it)",
    )
    parser_plot.add_argument(
        "--solvers",
        help="solvers to limit the histogram to",
        nargs="+",
    )
    parser_plot.add_argument(
        "--title",
        help='plot title (set to "" to disable)',
    )

    # report
    parser_report = subparsers.add_parser(
        "report",
        help="write report from test set results",
    )
    parser_report.add_argument(
        "--author",
        help="author field in the report",
    )

    # run
    parser_run = subparsers.add_parser(
        "run",
        help="run all tests from the test set",
    )
    parser_run.add_argument(
        "--problem",
        help="limit run to a specific problem",
    )
    parser_run.add_argument(
        "--rerun",
        default=False,
        action="store_true",
        help="rerun problems that are already in results (except timeouts)",
    )
    parser_run.add_argument(
        "--rerun-timeouts",
        default=False,
        action="store_true",
        help="include timeouts when rerunning all problems of the test set",
    )
    parser_run.add_argument(
        "--settings",
        help="limit run to a specific group of solver settings",
    )
    parser_run.add_argument(
        "--solver",
        help="limit run to a specific solver",
        choices=qpsolvers.available_solvers,
    )
    parser_run.add_argument(
        "--author",
        help="author field in the post-run report",
    )

    args = parser.parse_args()
    if "settings" in args and args.settings is not None:
        args.settings = args.settings.lower()
    if "solver" in args and args.solver is not None:
        args.solver = args.solver.lower()
    if "solvers" in args and args.solvers is not None:
        lowercase_solvers = [name.lower() for name in args.solvers]
        args.solvers = lowercase_solvers
    return args


def load_test_set(path: str) -> TestSet:
    """Load a test set.

    Args:
        path: path to the .py file containing the class definition
                of the TestSet

    Returns:
        Test set
    """
    dir_path, full_name = os.path.split(path)
    name = full_name.replace(".py", "")
    sys.path.append(
        dir_path
    )  # Add directory path to system path so import_module can find the module
    module = import_module(name)
    class_name = name.title().replace("_", "")
    TestClass = getattr(module, class_name)
    return TestClass()


def report(args, results: Results, test_set_path: Union[Path, str]):
    """Write report to file.

    Args:
        args: Command-line arguments.
        results: Benchmark results.
        test_set_path: Path to the test set Python source.
    """
    logging.info("Writing the overall report...")
    author = (
        args.author
        if args.author
        else input("GitHub username to write in the report? ")
    )
    report = Report(author, results)
    if results.file_path is None:
        raise BenchmarkError("not sure where to save report: no results file")
    results_file = Path(results.file_path)
    results_dir = results_file.parent
    test_set_name = Path(test_set_path).name.replace(".py", "")
    md_path = f"{results_dir}/{test_set_name}.md"
    report.write(md_path)


def main(
    test_set_path: Optional[Union[Path, str]] = None,
    results_path: Optional[Union[Path, str]] = None,
):
    """Main function of the script.

    Args:
        test_set_path: If set, load test set from this Python file.
        results_path: Path to the results CSV file.
    """
    if test_set_path is not None:
        test_set_path = Path(test_set_path)
        if test_set_path.suffix != ".py":
            raise BenchmarkError(
                "Test set path '{test_set_path}' is not a Python script"
            )

    args = parse_command_line_arguments(test_set_path)
    if test_set_path is None:
        test_set_path = args.test_set_path
    if args.very_verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    test_set = load_test_set(os.path.abspath(test_set_path))
    results = Results(results_path or args.results_path, test_set)

    if args.command == "run":
        run(
            test_set,
            results,
            only_problem=args.problem,
            only_settings=args.settings,
            only_solver=args.solver,
            rerun=args.rerun,
            rerun_timeouts=args.rerun_timeouts,
            verbose=args.verbose,
        )

    if args.command == "check_problem":
        problem = test_set.get_problem(args.problem)
        _ = problem  # dummy variable, to pass ruff linting
        logging.info(f"Check out `problem` for the {args.problem} problem")

    if args.command == "list_problems":
        test_set_name = str(test_set.__class__.__name__)
        logging.info(
            "Listing problems from the %s test set to the standard output",
            test_set_name,
        )
        print("\n".join(problem.name for problem in test_set))

    if args.command == "check_results":
        logging.info("Check out `results` for the full results data")
        df = results.df
        _ = df  # dummy variable, to pass ruff linting
        logging.info("Check out `df` for results as a pandas DataFrame")

    if args.command in ["check_problem", "check_results"]:
        try:
            import IPython

            if not IPython.get_ipython():
                IPython.embed()
        except ImportError:
            logging.error(
                "IPython not found, run this script in interactive mode"
            )

    if args.command == "plot":
        plot_metric(
            args.metric,
            results.df,
            args.settings,
            test_set,
            solvers=args.solvers,
            linewidth=args.linewidth,
            savefig=args.savefig,
            title=args.title,
        )

    if args.command in ["report", "run"]:
        report(args, results, test_set_path)


if __name__ == "__main__":
    main()
