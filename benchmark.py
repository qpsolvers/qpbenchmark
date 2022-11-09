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

from qpsolvers_benchmark import Report, Results, logging
from qpsolvers_benchmark.test_sets import MarosMeszaros, MarosMeszarosDense

TEST_CLASSES = {
    "maros_meszaros": MarosMeszaros,
    "maros_meszaros_dense": MarosMeszarosDense,
}


def parse_command_line_arguments():
    test_sets = list(TEST_CLASSES.keys())
    parser = argparse.ArgumentParser(
        description="Benchmark quadratic programming solvers"
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
        help="analyze a given test set problem in interactive mode",
    )
    parser_check_problem.add_argument(
        "test_set",
        choices=test_sets,
        help="test set to get problem from",
    )
    parser_check_problem.add_argument(
        "problem",
        help="name of the problem in the test set",
    )

    # check_results
    parser_check_results = subparsers.add_parser(
        "check_results",
        help="evaluate results from an existing run",
    )
    parser_check_results.add_argument(
        "results_file",
        help="path to the results CSV file",
    )

    # report
    parser_report = subparsers.add_parser(
        "report",
        help="write report from stored results",
    )
    parser_report.add_argument(
        "test_set",
        choices=test_sets,
        help="test set to report on",
    )
    parser_report.add_argument(
        "results_file",
        help="path to the corresponding results CSV file",
    )
    parser_report.add_argument(
        "--author",
        help="author field in the report",
    )

    # run
    parser_run = subparsers.add_parser(
        "run",
        help="run all tests from a test set",
    )
    parser_run.add_argument(
        "test_set",
        choices=test_sets,
        help="test set to execute command on",
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

    return parser.parse_args()


def find_results_file(args):
    if args.command in ["check_results", "report"]:
        results_file = args.results_file
        if not os.path.exists(results_file):
            raise FileNotFoundError(f"results file '{results_file}' not found")
    else:
        results_dir = os.path.join(os.path.dirname(__file__), "results")
        results_file = os.path.join(results_dir, f"{args.test_set}.csv")
    return results_file


if __name__ == "__main__":
    args = parse_command_line_arguments()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    results = Results(find_results_file(args))

    test_set = None
    if args.command in ["check_problem", "report", "run"]:
        TestClass = TEST_CLASSES[args.test_set]
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        test_set = TestClass(data_dir)

    if args.command == "run":
        args.solver = args.solver.lower() if args.solver else None
        args.settings = args.settings.lower() if args.settings else None
        test_set.run(
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

    if args.command in ["report", "run"]:
        logging.info("Writing the overall report...")
        author = (
            args.author
            if args.author
            else input("GitHub username to write in the report? ")
        )
        report = Report(author, test_set, results)
        md_path = results.csv_path.replace(".csv", ".md")
        report.write(md_path)
