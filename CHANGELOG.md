# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2023/07/25

### Added

* Allow non-lowercase solver names in the command line (thanks to @ottapav)
* Command-line tool and standalone test sets (thanks to @ZAKIAkram)

### Changed

* Plot: trim solutions that don't fulfill tolerance requirements
* Rename ``hist`` command to ``plot``
* Update to qpsolvers v3.4.0

### Fixed

* Plot whiskers on solutions beyond tolerance requirements (thanks to @ottapav)

## [0.1.0-beta] - 2022/01/26

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
* ProxQP: re-run benchmark with ProxQP 0.3.2
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
