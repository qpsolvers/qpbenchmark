# QP solvers benchmark

[![Build](https://img.shields.io/github/actions/workflow/status/qpsolvers/qpsolvers_benchmark/ci.yml?branch=main)](https://github.com/qpsolvers/qpsolvers_benchmark/actions)
[![PyPI version](https://img.shields.io/pypi/v/qpsolvers_benchmark)](https://pypi.org/project/qpsolvers_benchmark/)
[![Contributing](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/qpsolvers/qpsolvers_benchmark/tree/master/CONTRIBUTING.md)

Benchmark for quadratic programming (QP) solvers available in Python.

* **Results:** [GitHub-FFA](github_ffa/results/github_ffa.md), [Maros-Meszaros](maros_meszaros/results/maros_meszaros.md), [Maros-Meszaros-dense](maros_meszaros/results/maros_meszaros_dense.md)
* **Install:** `pip install qpsolvers_benchmark`
* **Run:** `qpsolvers_benchmark maros_meszaros/maros_meszaros.py run`

The goal of this benchmark is to help users compare and select QP solvers. Its methodology is open to [discussions](https://github.com/qpsolvers/qpsolvers_benchmark/discussions). The benchmark ships standard and community [test sets](#test-sets), as well as a ``qpsolvers_benchmark`` command-line tool to run test sets directly. The main output of the benchmark are standardized reports evaluating all [metrics](#metrics) across all QP solvers available on the test machine. This repository also distributes [results](#results) from running the benchmark on a reference computer.

New test sets are welcome! The benchmark is designed so that each test-set comes in a standalone directory. Feel free to create a new one and [contribute it](CONTRIBUTING.md) here so that we grow the collection over time.

## Solvers

| Solver | Keyword | Algorithm | Matrices | License |
| ------ | ------- | --------- | -------- | ------- |
| [Clarabel](https://github.com/oxfordcontrol/Clarabel.rs) | ``clarabel`` | Interior point | Sparse | Apache-2.0 |
| [CVXOPT](http://cvxopt.org/) | ``cvxopt`` | Interior point | Dense | GPL-3.0 |
| [DAQP](https://github.com/darnstrom/daqp) | ``daqp`` | Active set | Dense | MIT |
| [ECOS](https://web.stanford.edu/~boyd/papers/ecos.html) | ``ecos`` | Interior point | Sparse | GPL-3.0 |
| [Gurobi](https://www.gurobi.com/) | ``gurobi`` | Interior point | Sparse | Commercial |
| [HiGHS](https://highs.dev/) | ``highs`` | Active set | Sparse | MIT |
| [HPIPM](https://github.com/giaf/hpipm) | ``hpipm`` | Interior point | Dense | BSD-2-Clause |
| [MOSEK](https://mosek.com/) | ``mosek`` | Interior point | Sparse | Commercial |
| NPPro | ``nppro`` | Active set | Dense | Commercial |
| [OSQP](https://osqp.org/) | ``osqp`` | Douglas–Rachford | Sparse | Apache-2.0 |
| [ProxQP](https://github.com/Simple-Robotics/proxsuite) | ``proxqp`` | Augmented Lagrangian | Dense & Sparse | BSD-2-Clause |
| [qpOASES](https://github.com/coin-or/qpOASES) | ``qpoases`` | Active set | Dense | LGPL-2.1 |
| [qpSWIFT](https://qpswift.github.io/) | ``qpswift`` | Interior point | Sparse | GPL-3.0 |
| [quadprog](https://pypi.python.org/pypi/quadprog/) | ``quadprog`` | Goldfarb-Idnani | Dense | GPL-2.0 |
| [SCS](https://www.cvxgrp.org/scs/) | ``scs`` | Douglas–Rachford | Sparse | MIT |

## Test sets

The benchmark comes with standard and community test sets to represent different use cases for QP solvers:

| Test set | Keyword | Description |
| -------- | ------- | ----------- |
| **GitHub free-for-all** | ``github_ffa`` | Test set built by the community on GitHub, new problems [are welcome](https://github.com/qpsolvers/qpsolvers_benchmark/issues/new?assignees=&labels=&template=new_problem.md&title=)! |
| **Maros-Meszaros** | ``maros_meszaros`` | Standard set of problems designed to be difficult. |
| **Maros-Meszaros dense** | ``maros_meszaros_dense`` | Subset of the Maros-Meszaros test set restricted to smaller dense problems. |

## Results

The outcome from running a test set is a standardized report. You can check out results from a variety of machines, and share the reports produced by running the benchmark on your own machine, in the [Results category](https://github.com/qpsolvers/qpsolvers_benchmark/discussions/categories/results) of the discussions forum.

Here are the results obtained from running the benchmark with the same computer:

| Test set | Results | CPU info |
| -------- | ------- | -------- |
| **GitHub free-for-all** | [Full report](github_ffa/results/github_ffa.md) | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| **Maros-Meszaros** | [Full report](maros_meszaros/results/maros_meszaros.md) | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| **Maros-Meszaros dense** | [Full report](maros_meszaros/results/maros_meszaros_dense.md) | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |

## Metrics

We evaluate QP solvers based on the following metrics:

- **Success rate:** percentage of problems a solver is able to solve on a given test set.
- **Computation time:** time a solver takes to solve a given problem.
- **Optimality conditions:** we evaluate all three [optimality conditions](https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html):
    - **Primal residual:** maximum error on equality and inequality constraints at the returned solution.
    - **Dual residual:** maximum error on the dual feasibility condition at the returned solution.
    - **Duality gap:** value of the duality gap at the returned solution.
- **Cost error:** difference between the solution cost and the known optimal cost.

### Shifted geometric mean

Each metric (computation time, primal and dual residuals, duality gap) produces a different ranking of solvers for each problem. To aggregate those rankings into a single metric over the whole test set, we use the *shifted geometric mean* (shm), which is a standard to aggregate computation times in [benchmarks for optimization software](#other-benchmarks). This mean has the advantage of being compromised by neither large outliers (as opposed to the arithmetic mean) nor by small outliers (in contrast to the geometric geometric mean). Check out the [references](#references) below for further details.

Here are some intuitive interpretations:

- A solver with a shifted-geometric-mean runtime of $Y$ is $Y$ times slower than the best solver over the test set.
- A solver with a shifted-geometric-mean primal residual $R$ is $R$ times less accurate on equality and inequality constraints than the best solver over the test set.

## Limitations

Here are some known areas of improvement for this benchmark:

- *Cold start only:* we don't evaluate warm-start performance for now.

Check out the [issue tracker](https://github.com/qpsolvers/qpsolvers_benchmark/issues) for ongoing works and future improvements.

## Installation

You can install the benchmark and its dependencies in an isolated environment using ``conda``:

```console
conda create -f environment.yaml
conda activate qpsolvers_benchmark
```

Alternatively, you can install the benchmark on your system using ``pip``:

```console
pip install qpsolvers_benchmark
```

By default, the benchmark will run all supported solvers it finds.

## Running the benchmark

Once the benchmark is installed, you will be able to run the ``qpsolvers_benchmark`` command. Provide it with the script corresponding to the [test set](#test-sets) you want to run, followed by a benchmark command such as "run". For instance, let's run the "dense" subset of the Maros-Meszaros test set:

```console
qpsolvers_benchmark maros_meszaros/maros_meszaros_dense.py run
```

You can also run a specific solver, problem or set of solver settings:

```console
qpsolvers_benchmark maros_meszaros/maros_meszaros_dense.py run --solver proxqp --settings default
```

Check out ``qpsolvers_benchmark --help`` for a list of available commands and arguments.

## Plots

The command line ships a ``plot`` command to compare solver performances over a test set for a specific metric. For instance, run:

```console
qpsolvers_benchmark maros_meszaros/maros_meszaros_dense.py plot runtime high_accuracy
```

To generate the following plot:

![image](https://user-images.githubusercontent.com/1189580/220150365-530cd685-fc90-49b5-90e0-0b243fa602d9.png)

## Contributing

Contributions to improving this benchmark are welcome. You can for instance propose new problems, or share the runtimes you obtain on your machine. Check out the [contribution guidelines](CONTRIBUTING.md) for details.

## See also

### References

- [How not to lie with statistics: the correct way to summarize benchmark results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf): why geometric means should always be used to summarize normalized results.
- [Optimality conditions and numerical tolerances in QP solvers](https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html): note written while figuring out the ``high_accuracy`` settings of this benchmark.

### Other benchmarks

- [Benchmarks for optimization software](http://plato.asu.edu/bench.html) by Hans Mittelmann, which includes reports on the Maros-Meszaros test set.
- [jrl-qp/benchmarks](https://github.com/jrl-umi3218/jrl-qp/tree/master/benchmarks): benchmark of QP solvers available in C++.
- [osqp\_benchmark](https://github.com/osqp/osqp_benchmarks): benchmark examples for the OSQP solver.
- [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark): benchmark examples for the ProxQP solver.
