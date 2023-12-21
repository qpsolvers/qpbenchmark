# QP solvers benchmark

[![CI](https://github.com/qpsolvers/qpbenchmark/actions/workflows/ci.yml/badge.svg)](https://github.com/qpsolvers/qpbenchmark/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/qpbenchmark)](https://pypi.org/project/qpbenchmark/)
[![Contributing](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/qpsolvers/qpbenchmark/tree/main/CONTRIBUTING.md)

Benchmark for quadratic programming (QP) solvers available in Python.

The objective is to compare and select the best QP solvers for given use cases. The benchmarking methodology is open to [discussions](https://github.com/qpsolvers/qpbenchmark/discussions). Standard and community [test sets](#test-sets) are available: all of them can be processed using the ``qpbenchmark`` command-line tool, resulting in standardized reports evaluating all [metrics](#metrics) across all QP solvers available on the test machine.

## Test sets

The benchmark comes with standard and community test sets to represent different use cases for QP solvers:

- [Free-for-all](https://github.com/qpsolvers/free_for_all_qpbenchmark): community-built test set, new problems [are welcome](https://github.com/qpsolvers/free_for_all_qpbenchmark/issues/new?template=new_problem.md&title=)!
- [Maros-Meszaros](https://github.com/qpsolvers/maros_meszaros_qpbenchmark): a standard test set with problems designed to be difficult.
- [Model predictive control](https://github.com/qpsolvers/mpc_qpbenchmark): model predictive control problems arising *e.g.* in robotics.

New test sets are welcome! The `qpbenchmark` tool is designed to make it easy to wrap up a new test set without re-implementing the benchmark methodology. Check out [creating a new test set](CONTRIBUTING.md).

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
| [PIQP](https://github.com/PREDICT-EPFL/piqp) | ``piqp`` | Proximal Interior Point | Dense & Sparse | BSD-2-Clause |
| [ProxQP](https://github.com/Simple-Robotics/proxsuite) | ``proxqp`` | Augmented Lagrangian | Dense & Sparse | BSD-2-Clause |
| [QPALM](https://github.com/kul-optec/QPALM) | ``qpalm`` | Augmented Lagrangian | Sparse | LGPL-3.0 |
| [qpOASES](https://github.com/coin-or/qpOASES) | ``qpoases`` | Active set | Dense | LGPL-2.1 |
| [qpSWIFT](https://qpswift.github.io/) | ``qpswift`` | Interior point | Sparse | GPL-3.0 |
| [quadprog](https://pypi.python.org/pypi/quadprog/) | ``quadprog`` | Goldfarb-Idnani | Dense | GPL-2.0 |
| [SCS](https://www.cvxgrp.org/scs/) | ``scs`` | Douglas–Rachford | Sparse | MIT |

## Metrics

We evaluate QP solvers based on the following metrics:

- **Success rate:** percentage of problems a solver is able to solve on a given test set.
- **Computation time:** time a solver takes to solve a given problem.
- **Optimality conditions:** we evaluate all three [optimality conditions](https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html):
    - **Primal residual:** maximum error on equality and inequality constraints at the returned solution.
    - **Dual residual:** maximum error on the dual feasibility condition at the returned solution.
    - **Duality gap:** value of the duality gap at the returned solution.

### Shifted geometric mean

Each metric (computation time, primal and dual residuals, duality gap) produces a different ranking of solvers for each problem. To aggregate those rankings into a single metric over the whole test set, we use the *shifted geometric mean* (shm), which is a standard to aggregate computation times in [benchmarks for optimization software](#other-benchmarks). This mean has the advantage of being compromised by neither large outliers (as opposed to the arithmetic mean) nor by small outliers (in contrast to the geometric geometric mean). Check out the [references](#references) below for further details.

Here are some intuitive interpretations:

- A solver with a shifted-geometric-mean runtime of $Y$ is $Y$ times slower than the best solver over the test set.
- A solver with a shifted-geometric-mean primal residual $R$ is $R$ times less accurate on equality and inequality constraints than the best solver over the test set.

## Results

The outcome from running a test set is a standardized report comparing [solvers](#solvers) against the different [metrics](#metrics). Here are the results for the various ``qpbenchmark`` test sets:

- [Free-for-all results](https://github.com/qpsolvers/free_for_all_qpbenchmark/blob/main/results/free_for_all_qpbenchmark_ref.md)
- [Maros-Meszaros results](https://github.com/qpsolvers/maros_meszaros_qpbenchmark/blob/main/results/maros_meszaros_ref.md)
- [Model predictive control results](https://github.com/qpsolvers/mpc_qpbenchmark/blob/main/results/mpc_qpbenchmark_ref.md)

You can check out results from a variety of machines, and share the reports produced by running the benchmark on your own machine, in the Results category of the discussions forum of each test set.

## Limitations

Here are some known areas of improvement for this benchmark:

- [Cold start only:](https://github.com/qpsolvers/qpbenchmark/issues/101) we don't evaluate warm-start performance for now.
- [CPU thermal throttling:](https://github.com/qpsolvers/qpbenchmark/issues/88) the benchmark currently does not check the status of CPU thermal throttling. Adding this feature is a [good way to start contributing](https://github.com/qpsolvers/qpbenchmark/labels/good%20first%20issue) to the benchmark.

Check out the issue tracker for ongoing works and future improvements.

## Installation

The recommended process is to install the benchmark and all solvers in an isolated environment using ``conda``:

```console
conda env create -f environment.yaml
conda activate qpbenchmark
```

Alternatively, you can install the benchmarking tool individually using ``pip``:

```console
pip install qpbenchmark
```

In that case, the benchmark will run all supported solvers it finds. (Quick way to install open source solvers from PyPI: ``pip install qpsolvers[open_source_solvers]``.)

## Usage

The benchmark works by running ``qpbenchmark`` on a Python script describing the test set. For instance:

```console
qpbenchmark my_benchmark.py run
```

The test-set script is followed by a benchmark command, such as "run" here. We can add optional arguments to run a specific solver, problem, or solver settings:

```console
qpbenchmark my_benchmark.py run --solver proxqp --settings default
```

Check out ``qpbenchmark --help`` for a list of available commands and arguments.

### Plots

The command line ships a ``plot`` command to compare solver performances over a test set for a specific metric. For instance, run:

```console
qpbenchmark maros_meszaros_dense.py plot runtime high_accuracy
```

To generate the following plot:

![image](https://user-images.githubusercontent.com/1189580/220150365-530cd685-fc90-49b5-90e0-0b243fa602d9.png)

## Contributing

Contributions to improving this benchmark are welcome. You can for instance propose new problems, or share the runtimes you obtain on your machine. Check out the [contribution guidelines](CONTRIBUTING.md) for details.

## Citation

If you use `qpbenchmark` in your scientific works, please cite it *e.g.* as follows:

```bibtex
@software{qpbenchmark2023,
  author = {Caron, Stéphane and Zaki, Akram and Otta, Pavel and Arnström, Daniel and Carpentier, Justin},
  license = {Apache-2.0},
  month = dec,
  title = {{qpbenchmark: Benchmark for quadratic programming solvers available in Python}},
  url = {https://github.com/qpsolvers/qpbenchmark},
  version = {2.1.0},
  year = {2023}
}
```

You can also click on ``Cite this repository`` at the top-right of the [repository page](https://github.com/qpsolvers/qpbenchmark/).

## See also

### References

- [How not to lie with statistics: the correct way to summarize benchmark results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf): why geometric means should always be used to summarize normalized results.
- [Optimality conditions and numerical tolerances in QP solvers](https://scaron.info/blog/optimality-conditions-and-numerical-tolerances-in-qp-solvers.html): note written while figuring out the ``high_accuracy`` settings of this benchmark.

### Other benchmarks

- [Benchmarks for optimization software](http://plato.asu.edu/bench.html) by Hans Mittelmann, which includes reports on the Maros-Meszaros test set.
- [jrl-qp/benchmarks](https://github.com/jrl-umi3218/jrl-qp/tree/master/benchmarks): benchmark of QP solvers available in C++.
- [osqp\_benchmark](https://github.com/osqp/osqp_benchmarks): benchmark examples for the OSQP solver.
- [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark): benchmark examples for the ProxQP solver.
