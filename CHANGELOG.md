# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [2.0.0] - 2023-12-11

### Added

* New solver: QPALM

### Changed

* **Breaking:** Rename the project "qpbenchmark"
* Don't install solvers by default from PyPI
* Move solver issue and timeout listings to test-set themselves

### Removed

* Module-wide skip solver issue/timeout functions

## [1.2.0] - 2023-11-27

### Added

* Citation file to refer to the benchmark in scientific works
* Medium accuracy settings
* Note in the readme on CPU throttling

## [1.1.0] - 2023-09-08

### Added

* Check consistency after loading results
* More CPU information in reports
* New solver: HPIPM
* New solver: PIQP

### Changed

* Don't hard-wrap report lines, as it doesn't render well in Discussions
* Improve reporting of shifted geometric mean errors
* Make `cpuinfo` a proper dependency
* Refactor results class to allow finer `check_results` sessions
* Update to qpsolvers v4.0.0

### Fixed

* Correct `None` values to `False` in found column
* Make sure found column has only boolean values

## [1.0.0] - 2023-07-25

### Added

* Allow non-lowercase solver names in the command line (thanks to @ottapav)
* Command-line tool and standalone test sets (thanks to @ZAKIAkram)

### Changed

* Plot: trim solutions that don't fulfill tolerance requirements
* Rename ``hist`` command to ``plot``
* Update to qpsolvers v3.4.0

### Fixed

* Plot whiskers on solutions beyond tolerance requirements (thanks to @ottapav)

## [0.1.0-beta] - 2022-01-26

### Added

* Check dual residual
* Check duality gap
* Document all benchmark functions
* Main script: new ``hist`` plot command
* ProblemNotFound exception
* Results by settings in reports
* Write benchmark version in reports

### Changed

* Benchmark script takes test set as first argument
* Maros-Meszaros: empty equality constraints are now set to ``None``
* Re-run benchmark with ProxQP 0.3.2
* Refactor Report class and run function
* Report encoding is now UTF-8
* Switch to qpsolvers v2.7
* Test set descriptions are now mandatory

### Fixed

* Conform to linter standards
* Sparse matrix conversion

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

[unreleased]: https://github.com/qpsolvers/qpbenchmark/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/qpsolvers/qpbenchmark/compare/v1.2.0...v2.0.0
[1.2.0]: https://github.com/qpsolvers/qpbenchmark/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/qpsolvers/qpbenchmark/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/qpsolvers/qpbenchmark/compare/v0.1.0-beta...v1.0.0
[0.1.0-beta]: https://github.com/qpsolvers/qpbenchmark/compare/v0.1.0-alpha...v0.1.0-beta
[0.1.0-alpha]: https://github.com/qpsolvers/qpbenchmark/releases/tag/v0.1.0-alpha
