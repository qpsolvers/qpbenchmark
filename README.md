# QP solvers benchmark

[![Contributing](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/stephane-caron/qpsolvers_benchmark/tree/master/CONTRIBUTING.md)

Benchmark for quadratic programming (QP) solvers available in Python. It contains the following test sets:

- [Maros-Meszaros](#maros-meszaros): problems designed to be difficult, some of them with non-strictly p.s.d. Hessians.
- [Maros-Meszaros dense](#maros-meszaros-dense): subset of the 59 smallest Maros-Meszaros problems, still difficult but accessible to dense solvers.

This benchmark aims to help us compare and select QP solvers. Its methodology is open to [discussions](https://github.com/stephane-caron/qpsolvers_benchmark/discussions). New test sets are [also welcome](CONTRIBUTING.md). Feel free to add one that better represents the family of problems you are working on.

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

- **Success rate:** percentage of problems a solver is able to solve on a given test set.
- **Primal error:** ...
- **Cost error:** ...

### Shifted geometric mean

For each metric (computation time, primal error, cost error, ...), every
problem in the test set produces a different ranking of solvers. To aggregate
those rankings into a single metric over the whole test set, we use the
**shifted geometric mean**, which is a standard to aggregate computation times
in [benchmarks for optimization software](http://plato.asu.edu/bench.html).

The shifted geometric mean is a slowdown/loss factor compared to the best
solver over the whole test set. This mean has the advantage of being
compromised by neither large outliers (as opposed to the arithmetic mean) nor
by small outliers (in contrast to the geometric geometric mean). Check out the
[references](#see-also) below for further details.

## Results

Check out the full reports for each test set in the [results](results) directory.

### Maros-Meszaros

The Maros-Meszaros test set contains difficult problems, some of them large, sparse, ill-conditioned or not strictly convex. For sparse solvers only.

| Solver | Success rate (%) | Runtime (× slower than best) | Primal error |
|:-------|-----------------:|-----------------------------:|-------------:|
| cvxopt | 16 | 16.4 |  18.5 |
| highs  | 61 |  1.8 |   2.0 |
| osqp   | 64 |  1.3 |   1.8 |
| proxqp | 72 |  1.0 |   1.0 |
| scs    | 54 |  3.1 | 548.2 |

Check out the [full report](results/maros_meszaros.md) for definitions and details.

### Maros-Meszaros dense

Probems in the Maros-Meszaros test set with less than a 1,000 optimization variables and 1,000 constraints. Note that this subset is not representative of the full Maros-Meszaros test set.

Check out the [full report](results/maros_meszaros_dense.md) for definitions and details.

## Limitations

Here are some known areas of improvement for this benchmark:

- Cold start only: we don't evaluate warm-start performance for now.
- Dual feasibility: we don't check the dual multipliers that solvers compute internally, as the API for them is not yet unified.
- TODO: any measure of the mean value of data is misleading when there is large variance. We should provide some low and high estimates (min and max, or 5% and 95% percentiles) along with geometric means.

## Installation

Install all required dependencies by:

```console
pip install qpsolvers_benchmark
```

By default, the benchmark will run with any supported solver installed on your system. You can install all supported open-source solvers at once by:

```console
pip install qpsolvers_benchmark[open_source_solvers]
```

## Running the benchmark

Let's run for instance the Maros-Meszaros test set:

```console
python benchmark.py run maros_meszaros
```

Replace ``maros_meszaros`` with the name of the test set you want to run. You can also run a specific solver, problem or set of solver settings:

```console
python benchmark.py run maros_meszaros_dense --solver proxqp --settings default
```

Check out ``python benchmark.py --help`` for details.

## See also

- [How not to lie with statistics: the correct way to summarize benchmark results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf): why geometric means should always be used to summarize normalized results.
- [Optimality conditions and numerical tolerances in QP solvers](https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html): note written while figuring out the ``high_accuracy`` settings of this benchmark.
- [jrl-qp/benchmarks](https://github.com/jrl-umi3218/jrl-qp/tree/master/benchmarks): benchmark of QP solvers available in C++.
- [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark): benchmark examples for the ProxQP solver.
