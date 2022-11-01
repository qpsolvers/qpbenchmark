# Maros-Meszaros test set

- Maintainer: [@stephane-caron](https://github.com/stephane-caron/)
- Date: 2022-11-01 10:28:23.687963+00:00
- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Solver versions:

| solver   | version   |
|:---------|:----------|
| cvxopt   | 1.3.0     |
| highs    | 1.2.2     |
| osqp     | 0.6.2     |
| proxqp   | 0.2.2     |
| scs      | 3.2.0     |

## Success rate

Precentage of problems each solver is able to solve:

|        |   default |
|:-------|----------:|
| cvxopt |        16 |
| highs  |        59 |
| osqp   |        64 |
| proxqp |        72 |
| scs    |        54 |

Rows are solvers and columns are solver settings.

## Computation time

We compare solver computation times using the **shifted geometric mean**. A
solver with a shifted geometric mean of Y is Y times slower than the best
solver over the test set.

### Details

There is a different ranking of solver runtimes for each problem in the test
set. To aggregate those rankings into a single metric over the whole test set,
we use the shifted geometric mean, which is a standard in [benchmarks for
optimization software](http://plato.asu.edu/bench.html).

The shifted geometric mean is a slowdown factor compared to the best solver
over the whole test set. It has the advantage of being compromised by neither
large outliers (as opposed to the arithmetic mean) nor by small outliers (in
contrast to the geometric geometric mean). The best solvers have a shifted
geometric mean close to one.

As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the
time limit when it fails to solve a problem.

### Results

Shifted geometric mean of solver computation times for each setting:

|        |   default |
|:-------|----------:|
| cvxopt |      16.4 |
| highs  |       2.1 |
| osqp   |       1.3 |
| proxqp |       1.0 |
| scs    |       3.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$.

## Accuracy

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. As with runtimes, we use the
shifted geometric mean of primal errors to aggregate the metric over the whole
test set.

Shifted geometric mean of solver primal errors for each setting:

|        |   default |
|:-------|----------:|
| cvxopt |      18.5 |
| highs  |       2.2 |
| osqp   |       1.8 |
| proxqp |       1.0 |
| scs    |     548.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error of 1.

### Cost errors

...
