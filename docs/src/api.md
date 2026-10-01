# API documentation

A test set is a Python script defining a subclass of [`TestSet`][qpbenchmark.test_set.TestSet], whose class name should match the name of the test-set script in PascalCase. Running the `qpbenchmark` command on this script solves its [problems][qpbenchmark.problem.Problem] with all available solvers and [settings][qpbenchmark.solver_settings.SolverSettings], stores [results][qpbenchmark.results.Results] and writes a [report][qpbenchmark.report.Report].

## Test sets

::: qpbenchmark.test_set.TestSet

::: qpbenchmark.parquet_test_set.ParquetTestSet

::: qpbenchmark.solver_settings.SolverSettings

::: qpbenchmark.tolerance.Tolerance

## Problems

::: qpbenchmark.problem.Problem

::: qpbenchmark.problem_list.ProblemList

## Running a test set

::: qpbenchmark.run.run

::: qpbenchmark.benchmark.main

## Results

::: qpbenchmark.results.Results

::: qpbenchmark.report.Report

## Exceptions

::: qpbenchmark.exceptions.BenchmarkError

::: qpbenchmark.exceptions.ProblemNotFound

::: qpbenchmark.exceptions.ResultsError
