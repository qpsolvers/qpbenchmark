#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
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

import argparse
import os
from importlib import import_module  # type: ignore

from qpsolvers_benchmark import Report, Results, TestSet, logging, run
from qpsolvers_benchmark.plot_metric import plot_metric

TEST_SETS = [
    "github_ffa",
    "maros_meszaros",
    "maros_meszaros_dense",
    "maros_meszaros_dense_posdef",
]

TEST_ARGS = {
    "maros_meszaros": {
        "data_dir": os.path.join(os.path.dirname(__file__), "data"),
    },
    "maros_meszaros_dense": {
        "data_dir": os.path.join(os.path.dirname(__file__), "data"),
    },
    "maros_meszaros_dense_posdef": {
        "data_dir": os.path.join(os.path.dirname(__file__), "data"),
    },
}


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description="Benchmark quadratic programming solvers"
    )
    parser.add_argument(
        "test_set",
        choices=TEST_SETS,
        help="test set from the benchmark to consider",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="verbose mode",
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
    parser_check_results = subparsers.add_parser(
        "check_results",
        help="evaluate test set results interactively",
    )
    parser_check_results.add_argument(
        "--results-file",
        help="path to the results CSV file",
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
        "--results-file",
        help="report test set results from this specific CSV file",
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
        "--include-timeouts",
        default=False,
        action="store_true",
        help="include timeouts when --rerunning the test set",
    )
    parser_run.add_argument(
        "--problem",
        help="limit run to a specific problem",
    )
    parser_run.add_argument(
        "--rerun",
        default=False,
        action="store_true",
        help="rerun test set even on problems with saved results",
    )
    parser_run.add_argument(
        "--settings",
        help="limit run to a specific group of solver settings",
    )
    parser_run.add_argument(
        "--solver",
        help="limit run to a specific solver",
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


def find_results_file(args):
    if args.command in ["check_results", "report"]:
        results_file = (
            args.results_file
            if args.results_file
            else f"results/{args.test_set}.csv"
        )
        if not os.path.exists(results_file):
            raise FileNotFoundError(f"results file '{results_file}' not found")
    else:
        results_dir = os.path.join(os.path.dirname(__file__), "results")
        results_file = os.path.join(results_dir, f"{args.test_set}.csv")
    return results_file


def load_test_set(name: str) -> TestSet:
    """
    Load a test set.

    Args:
        name: Name of the test set.

    Returns:
        Test set.
    """
    module = import_module(f"qpsolvers_benchmark.test_sets.{name}")
    class_name = name.title().replace("_", "")
    TestClass = getattr(module, class_name)
    kwargs = TEST_ARGS.get(name, {})
    return TestClass(**kwargs)


if __name__ == "__main__":
    args = parse_command_line_arguments()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    test_set = load_test_set(args.test_set)
    results = Results(find_results_file(args), test_set)

    if args.command == "run":
        run(
            test_set,
            results,
            only_problem=args.problem,
            only_settings=args.settings,
            only_solver=args.solver,
            rerun=args.rerun,
            include_timeouts=args.include_timeouts,
        )

    if args.command == "check_problem":
        problem = test_set.get_problem(args.problem)
        logging.info(f"Check out `problem` for the {args.problem} problem")

    if args.command == "check_results":
        logging.info("Check out `results` for the full results data")
        df = results.df
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
        logging.info("Writing the overall report...")
        author = (
            args.author
            if args.author
            else input("GitHub username to write in the report? ")
        )
        report = Report(author, results)
        md_path = results.csv_path.replace(".csv", ".md")
        report.write(md_path)
