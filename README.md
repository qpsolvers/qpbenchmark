# qpsolvers benchmark

[![Contributing](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/stephane-caron/qpsolvers_benchmark/tree/master/CONTRIBUTING.md)

Benchmark for quadratic programming solvers available in Python. It contains the following test sets:

- [Maros-Meszaros](#maros-meszaros): Problems designed to be difficult, some of them with non-strictly p.s.d. Hessians.

New test sets [are welcome](CONTRIBUTING.md). Feel free to add one that better represents the family of problems you are working on.

## Results

Check out the full reports for each test set in the [results](results) directory.

### Maros-Meszaros

The Maros-Meszaros test set contains difficult problems, some of them large, sparse, ill-conditioned or with non-strictly p.s.d. Hessian matrices. For sparse solvers only.

| Solver | Success rate (%) | Slower than best (×) |
|:-------|-----------------:|---------------------:|
| cvxopt | 15.9 | 16.4 |
| osqp   | 64.4 | 1.3 |
| proxqp | 72.4 | 1.0 |
| scs    | 54.3 | 3.1 |

Check out the [full report](results/maros_meszaros.md) for definitions and details.

## Running the benchmark

To run the benchmark on your machine, you will first need to install [qpsolvers](https://github.com/stephane-caron/qpsolvers) along with the QP solvers you want to test. For instance, to install open source solvers:

```console
$ pip install qpsolvers[open_source_solvers]
```

Then, run the benchmark by:

```console
$ python run_benchmark.py
```

## Limitations

Here are some known areas of improvement for this benchmark:

- Cold start only: we don't evaluate warm-start performance for now.
- Dual feasibility: we don't check the dual multipliers that solvers compute internally, as the API for them is not yet unified.

## See also

This repository borrows from [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark), which follows the methodology laid out by the [OSQP benchmark](https://arxiv.org/pdf/1711.08013.pdf).

- [jrl-qp/benchmarks](https://github.com/jrl-umi3218/jrl-qp/tree/master/benchmarks)
- [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark)
