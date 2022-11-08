# Maros-Meszaros dense subset

- CPU: i386
- Date: 2022-11-04 19:34:07.386694+00:00
- Maintainer: [@stephane-caron](https://github.com/stephane-caron/)
- Time limit: 1000.0 seconds
- qpsolvers version: 2.5.0

Solvers:

| solver   | version     |
|:---------|:------------|
| cvxopt   | 1.3.0       |
| ecos     | 2.0.10      |
| osqp     | 0.6.2.post5 |
| proxqp   | 0.2.4       |
| scs      | 3.2.2       |

## Metrics

### Shifted geometric mean

For each metric (computation time, solution accuracy, ...), every problem in
the test set produces a different ranking of solvers. To aggregate those
rankings into a single metric over the whole test set, we use the shifted
geometric mean, which is a standard to aggregate computation times in
[benchmarks for optimization software](http://plato.asu.edu/bench.html).

The shifted geometric mean is a slowdown/loss factor compared to the best
solver over the whole test set. It has the advantage of being compromised by
neither large outliers (as opposed to the arithmetic mean) nor by small
outliers (in contrast to the geometric geometric mean). The best solvers have a
shifted geometric mean close to one.

## Results

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |        15 |              15 |
| ecos     |         8 |               8 |
| osqp     |        93 |              53 |
| proxqp   |       100 |             100 |
| qpswift  |        15 |              15 |
| quadprog |        34 |              34 |
| scs      |        56 |              56 |

Rows are solvers and columns are solver settings.

### Computation time

We compare solver computation times over the whole test set using the [shifted
geometric mean](#shifted-geometric-mean). Intuitively, a solver with a
shifted-geometric-mean runtime of Y is Y times slower than the best solver over
the test set.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |     967.0 |           985.0 |
| ecos     |    1329.5 |          1354.2 |
| osqp     |       7.3 |           159.8 |
| proxqp   |       1.0 |             1.0 |
| qpswift  |     966.9 |           985.0 |
| quadprog |     397.6 |           405.0 |
| scs      |     141.1 |           144.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. As with runtimes, we use the
[shifted geometric mean](#shifted-geometric-mean) to aggregate primal errors
over the whole test set.

Shifted geometric mean of solver primal errors (1.0 is the best):

|          |         default |   high_accuracy |
|:---------|----------------:|----------------:|
| cvxopt   |     533692864.2 |     533692864.2 |
| ecos     |     578279684.7 |     578279684.7 |
| osqp     |    9167423668.4 |     293549344.6 |
| proxqp   |             1.0 |             1.0 |
| qpswift  |     533692864.1 |     533692864.1 |
| quadprog |     412554313.6 |     412554313.6 |
| scs      | 4925361579784.5 | 4924776578454.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error of
1.0.

### Cost errors

...
