# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [2.5.0] - 2025-05-07

### Added

- Add jaxopt.OSQP solver
- Add KVXOPT solver with the same settings as CVXOPT
- Add QPAX solver and document its choice of settings

### Changed

- CICD: Update checkout action to v4

## [2.4.0] - 2024-12-16

### Added

- Add `ParquetTestSet` class for test sets loaded from Parquet files
- Add `Problem.from_qpsolvers` shorthand function
- Add `ProblemList` class that can be saved to Parquet files
- Allow strings or paths as arguments to the main function
- CLI: Add `list_problems` command
- New dependency: tqdm
- Optionally add a GPU summary line to reports
- Results can now be read and save from and to Parquet files
- Results property to get the number of result rows
- Support Python 3.12
- Very-verbose mode for extra debug messages

### Changed

- Allow results file paths to be strings or pathlib paths
- Don't save results more frequently than every 10 seconds
- More informative solver exception warnings
- Refactor results loading and saving
- Save results to file after problem is done rather than at each solver call
- Update skip logic in CPU info table

### Fixed

- CLI: Only allow `--solver` to be an available solver for the `run` command

## [2.3.0] - 2024-09-03

### Added

- Add `results_path` argument to the `main` function
- Results: handle loading/saving CSV files with out-of-test-set problems
- Special handling to get CVXOPT version number properly

### Changed

- CLI: make results path an argument to all commands
- Rename "include timeouts" argument to "rerun timeouts"

## [2.2.3] - 2024-08-14

### Fixed

- Fix reporting of solver versions when some solvers are excluded

## [2.2.2] - 2024-07-31

### Added

- Expose exceptions from top-level module

### Fixed

- Bump Python version to actual requirement of 3.9 or above
- Handle no-op conversion from dense to dense properly
- Handle no-op conversion from sparse to sparse properly

## [2.2.1] - 2024-02-06

### Changed

- Update qpsolvers to v4.3.1 to fix the Gurobi interface (thanks @563925743)

## [2.2.0] - 2024-01-16

### Added

- Distribute [on conda-forge](https://anaconda.org/conda-forge/qpbenchmark)
- Test set path argument to the main function of the command-line interface

### Changed

- Update environment file to install from conda-forge

## [2.1.1] - 2023-12-22

### Changed

- Clarabel: set ``tol_gap_abs`` settings in ``set_eps_abs``
- Clarabel: set ``tol_gap_rel`` settings in ``set_eps_rel``
- Log a warning message when skipping known solver issue
- PIQP: set ``eps_duality_gap_abs`` settings in ``set_eps_abs``
- PIQP: set ``eps_duality_gap_rel`` settings in ``set_eps_rel``
- ProxQP: set ``eps_duality_gap_abs`` settings in ``set_eps_abs``
- ProxQP: set ``eps_duality_gap_rel`` settings in ``set_eps_rel``

### Fixed

- Handling of known solver issues

## [2.1.0] - 2023-12-21

### Added

- Expose `Problem` from top-level module
- Link in report header to go to results tables directly
- Number of problems in report header
- Utility function to load a problem from file

### Changed

- **Breaking:** Remove the cost error from benchmark metrics
- Include Python 3.8 in supported versions

### Removed

- Move the GitHub Free-for-all test set to [its own repository](https://github.com/qpsolvers/free_for_all_qpbenchmark)
- Move Maros-Meszaros test set to [its own repository](https://github.com/qpsolvers/maros_meszaros_qpbenchmark)

## [2.0.0] - 2023-12-11

### Added

- New solver: QPALM

### Changed

- **Breaking:** Rename the project to "qpbenchmark"
- Don't install solvers by default from PyPI
- Move solver issue and timeout listings to test-set themselves

### Removed

- Module-wide skip solver issue/timeout functions

## [1.2.0] - 2023-11-27

### Added

- Citation file to refer to the benchmark in scientific works
- Medium accuracy settings
- Note in the readme on CPU throttling

## [1.1.0] - 2023-09-08

### Added

- Check consistency after loading results
- More CPU information in reports
- New solver: HPIPM
- New solver: PIQP

### Changed

- Don't hard-wrap report lines, as it doesn't render well in Discussions
- Improve reporting of shifted geometric mean errors
- Make `cpuinfo` a proper dependency
- Refactor results class to allow finer `check_results` sessions
- Update to qpsolvers v4.0.0

### Fixed

- Correct `None` values to `False` in found column
- Make sure found column has only boolean values

## [1.0.0] - 2023-07-25

### Added

- Allow non-lowercase solver names in the command line (thanks to @ottapav)
- Command-line tool and standalone test sets (thanks to @ZAKIAkram)

### Changed

- Plot: trim solutions that don't fulfill tolerance requirements
- Rename ``hist`` command to ``plot``
- Update to qpsolvers v3.4.0

### Fixed

- Plot whiskers on solutions beyond tolerance requirements (thanks to @ottapav)

## [0.1.0-beta] - 2022-01-26

### Added

- Check dual residual
- Check duality gap
- Document all benchmark functions
- Main script: new ``hist`` plot command
- ProblemNotFound exception
- Results by settings in reports
- Write benchmark version in reports

### Changed

- Benchmark script takes test set as first argument
- Maros-Meszaros: empty equality constraints are now set to ``None``
- Re-run benchmark with ProxQP 0.3.2
- Refactor Report class and run function
- Report encoding is now UTF-8
- Switch to qpsolvers v2.7
- Test set descriptions are now mandatory

### Fixed

- Conform to linter standards
- Sparse matrix conversion

## [0.1.0-alpha] - 2022-12-21

### Added

- GitHub free-for-all test set
- Initial benchmark infrastructure
- List current solver issues
- Logging in spdlog-like format
- Maros-Meszaros dense subset
- Maros-Meszaros test set
- Problem class inherited from qpsolvers
- Results class
- SolverSettings class
- TestSet class

[unreleased]: https://github.com/qpsolvers/qpbenchmark/compare/v2.5.0...HEAD
[2.5.0]: https://github.com/qpsolvers/qpbenchmark/compare/v2.4.0...v2.5.0
[2.4.0]: https://github.com/qpsolvers/qpbenchmark/compare/v2.3.0...v2.4.0
[2.3.0]: https://github.com/qpsolvers/qpbenchmark/compare/v2.2.3...v2.3.0
[2.2.3]: https://github.com/qpsolvers/qpbenchmark/compare/v2.2.2...v2.2.3
[2.2.2]: https://github.com/qpsolvers/qpbenchmark/compare/v2.2.1...v2.2.2
[2.2.1]: https://github.com/qpsolvers/qpbenchmark/compare/v2.2.0...v2.2.1
[2.2.0]: https://github.com/qpsolvers/qpbenchmark/compare/v2.1.1...v2.2.0
[2.1.1]: https://github.com/qpsolvers/qpbenchmark/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/qpsolvers/qpbenchmark/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/qpsolvers/qpbenchmark/compare/v1.2.0...v2.0.0
[1.2.0]: https://github.com/qpsolvers/qpbenchmark/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/qpsolvers/qpbenchmark/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/qpsolvers/qpbenchmark/compare/v0.1.0-beta...v1.0.0
[0.1.0-beta]: https://github.com/qpsolvers/qpbenchmark/compare/v0.1.0-alpha...v0.1.0-beta
[0.1.0-alpha]: https://github.com/qpsolvers/qpbenchmark/releases/tag/v0.1.0-alpha
