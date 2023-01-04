# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added

* Check dual residual
* Check duality gap
* Document all benchmark functions
* Main script: new ``hist_metric`` plot command
* ProblemNotFound exception
* Results by settings in reports
* Write benchmark version in reports

### Changed

* Benchmark script takes test set as first argument
* Maros-Meszaros: empty equality constraints are now set to ``None``
* Refactor Report class and run function
* Report encoding is now UTF-8
* Switch to qpsolvers v2.7
* Test set descriptions are now mandatory

### Fixed

* Conform to linter standards
* Sparse matrix conversion

## [0.1.0-alpha] - 2022/12/21

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
