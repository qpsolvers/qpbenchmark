# QP solvers benchmark

[![Contributing](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/stephane-caron/qpsolvers_benchmark/tree/master/CONTRIBUTING.md)

Benchmark for quadratic programming (QP) solvers available in Python.

The goal of this benchmark is to help us compare and select QP solvers. Its methodology is open to [discussions](https://github.com/stephane-caron/qpsolvers_benchmark/discussions). New test sets are [also welcome](CONTRIBUTING.md). Feel free to add one that better represents the kind of problems you are working on.

## Test sets

- [Maros-Meszaros](#maros-meszaros) (``maros_meszaros``): Standard set of problems designed to be difficult, some of them large, sparse, ill-conditioned or not strictly convex.
- [Maros-Meszaros dense](#maros-meszaros-dense) (``maros_meszaros_dense``): Subset of the Maros-Meszaros test set restricted to problems with less than 1,000 optimization variables and 1,000 constraints.

## Solvers

| Solver | Keyword | Algorithm | Matrices | License |
| ------ | ------- | --------- | -------- | ------- |
| [CVXOPT](http://cvxopt.org/) | ``cvxopt`` | Interior point | Dense | GPL-3.0 |
| [ECOS](https://web.stanford.edu/~boyd/papers/ecos.html) | ``ecos`` | Interior point | Sparse | GPL-3.0 |
| [Gurobi](https://www.gurobi.com/) | ``gurobi`` | Interior point | Sparse | Commercial |
| [HiGHS](https://highs.dev/) | ``highs`` | Active set | Sparse | MIT |
| [MOSEK](https://mosek.com/) | ``mosek`` | Interior point | Sparse | Commercial |
| [OSQP](https://osqp.org/) | ``osqp`` | Augmented Lagrangian | Sparse | Apache-2.0 |
| [ProxQP](https://github.com/Simple-Robotics/proxsuite) | ``proxqp`` | Augmented Lagrangian | Dense & Sparse | BSD-2-Clause |
| [qpOASES](https://github.com/coin-or/qpOASES) | ``qpoases`` | Active set | Dense | LGPL-2.1 |
| [qpSWIFT](https://qpswift.github.io/) | ``qpswift`` | Interior point | Sparse | GPL-3.0 |
| [quadprog](https://pypi.python.org/pypi/quadprog/) | ``quadprog`` | Active set | Dense | GPL-2.0 |
| [SCS](https://www.cvxgrp.org/scs/) | ``scs`` | Augmented Lagrangian | Sparse | MIT |

## Metrics

We evaluate QP solvers based on the following metrics:

- **Success rate:** percentage of problems a solver is able to solve on a given test set.
- **Computation time:** time a solver takes to solve a given problem.
- **Primal error:** maximum error on equality and inequality constraints at the returned solution.
- **Cost error:** difference between the solution cost and the known optimal cost.

### Shifted geometric mean

Problem-specific metrics (computation time, primal error, cost error) produce a different ranking of solvers for each problem. To aggregate those rankings into a single metric over the whole test set, we use the *shifted geometric mean* (SGM), which is a standard to aggregate computation times in [benchmarks for optimization software](#other-benchmarks). This mean has the advantage of being compromised by neither large outliers (as opposed to the arithmetic mean) nor by small outliers (in contrast to the geometric geometric mean). Check out the [references](#references) below for further details.

Here are some intuitive interpretations:

- A solver with a shifted-geometric-mean runtime of $Y$ is $Y$ times slower than the best solver over the test set.
- A solver with a shifted-geometric-mean primal error $P$ is $P$ times less accurate on equality and inequality constraints than the best solver over the test set.

## Results

Check out the full reports for each test set in the [results](results) directory.

### Maros-Meszaros

Summary of solver performances with their default settings:

| Solver | Success rate (%) | Runtime (SGM) | Primal error (SGM) | Cost error (SGM) |
|:-------|-----------------:|--------------:|-------------------:|-----------------:|
| cvxopt |     16 |    54.0 |     5.7 |    24.5 |
| highs  |     60 |     6.1 | **2.6** | **2.9** |
| osqp   |     59 | **1.0** |    52.1 |    26.0 |
| proxqp | **81** | **2.4** | **1.0** | **1.0** |
| scs    |     33 |    23.2 |    11.8 |    12.5 |

Check out the [full report](results/maros_meszaros.md) for details.

### Maros-Meszaros dense subset

Summary of solver performances with their default settings:

| Solver | Success rate (%) | Runtime (SGM) | Primal error (SGM) | Cost error (SGM) |
|:-------|-----------------:|--------------:|-------------------:|-----------------:|
| cvxopt   |      15 |  1600 |  530000 |   950 |
| ecos     |       8 |  2000 |  570000 |  1300 |
| highs    |      76 |    67 |  140000 |    39 |
| osqp     |      68 |    12 | 5900000 |   480 |
| proxqp   | **100** | **1** |   **1** | **1** |
| qpoases  |      63 |   130 |  750000 |   110 |
| qpswift  |      15 |  1600 |  530000 |   950 |
| quadprog |      34 |   660 |  410000 |   390 |
| scs      |      29 |   840 |  440000 |   500 |

Check out the [full report](results/maros_meszaros_dense.md) for details. Note that this subset is not representative of the full Maros-Meszaros test set.

## Limitations

Here are some known areas of improvement for this benchmark:

- *Cold start only:* we don't evaluate warm-start performance for now.
- *Dual feasibility:* we don't check the dual multipliers that solvers compute internally, as the API for them is not yet unified.

Check out the [issue tracker](https://github.com/stephane-caron/qpsolvers_benchmark/issues) for ongoing works and future improvements.

## Installation

Install all required dependencies by:

```console
pip install qpsolvers_benchmark
```

By default, the benchmark will run with any supported solver installed on your system. You can install all supported open-source solvers at once by installing ``qpsolvers_benchmark[open_source_solvers]``, *i.e.* appending the ``open_source_solvers`` dependency.

## Running the benchmark

Pick up the keyword corresponding to the desired [test set](#test-sets), for instance ``maros_meszaros``, and pass it to the ``run`` command:

```console
python benchmark.py run maros_meszaros
```

You can also run a specific solver, problem or set of solver settings:

```console
python benchmark.py run maros_meszaros_dense --solver proxqp --settings default
```

Check out ``python benchmark.py --help`` for all available commands and arguments.

## See also

### References

- [How not to lie with statistics: the correct way to summarize benchmark results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf): why geometric means should always be used to summarize normalized results.
- [Optimality conditions and numerical tolerances in QP solvers](https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html): note written while figuring out the ``high_accuracy`` settings of this benchmark.

### Other benchmarks

- [Benchmarks for optimization software](http://plato.asu.edu/bench.html) by Hans Mittelmann, which includes reports on the Maros-Meszaros test set.
- [jrl-qp/benchmarks](https://github.com/jrl-umi3218/jrl-qp/tree/master/benchmarks): benchmark of QP solvers available in C++.
- [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark): benchmark examples for the ProxQP solver.
