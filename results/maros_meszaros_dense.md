# Maros-Meszaros dense subset

- Author: [@stephane-caron](https://github.com/stephane-caron/)
- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-11-07 10:49:21.842658+00:00

## Settings

- Cost error limit: 1000.0
- Primal error limit: 1.0
- Time limit: 1000.0 seconds

| solver   | parameter                        | default   |   high_accuracy |
|:---------|:---------------------------------|:----------|----------------:|
| cvxopt   | ``feastol``                      | -         |     1e-09       |
| ecos     | ``feastol``                      | -         |     1e-09       |
| gurobi   | ``time_limit``                   | 1000.0    |  1000           |
| highs    | ``dual_feasibility_tolerance``   | -         |     1e-09       |
| highs    | ``primal_feasibility_tolerance`` | -         |     1e-09       |
| highs    | ``time_limit``                   | 1000.0    |  1000           |
| osqp     | ``eps_abs``                      | -         |     1e-09       |
| osqp     | ``eps_rel``                      | -         |     0           |
| osqp     | ``time_limit``                   | 1000.0    |  1000           |
| proxqp   | ``eps_abs``                      | -         |     1e-09       |
| proxqp   | ``eps_rel``                      | -         |     0           |
| qpoases  | ``time_limit``                   | 1000.0    |  1000           |
| qpswift  | ``RELTOL``                       | -         |     1.73205e-09 |
| scs      | ``eps_abs``                      | -         |     1e-09       |
| scs      | ``eps_rel``                      | -         |     0           |
| scs      | ``time_limit_secs``              | 1000.0    |  1000           |

## Metrics

For each metric (computation time, primal error, cost error, ...), every
problem in the test set produces a different ranking of solvers. To aggregate
those rankings into a single metric over the whole test set, we use the
**shifted geometric mean**, which is a standard to aggregate computation times
in [benchmarks for optimization software](http://plato.asu.edu/bench.html).

The shifted geometric mean is a slowdown/loss factor compared to the best
solver over the whole test set. Hence, the best solvers for a given metric have
a shifted geometric mean close to one. This mean has the advantage of being
compromised by neither large outliers (as opposed to the arithmetic mean) nor
by small outliers (in contrast to the geometric geometric mean). Check out the
[references](#see-also) below for more information.

## Results

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |        15 |              15 |
| ecos     |         8 |               8 |
| highs    |        76 |              76 |
| osqp     |        66 |              53 |
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
| cvxopt   |    1126.6 |          1080.5 |
| ecos     |    1549.0 |          1485.6 |
| highs    |      47.5 |            45.6 |
| osqp     |      87.1 |           175.3 |
| proxqp   |       1.0 |             1.0 |
| qpswift  |    1126.4 |          1080.4 |
| quadprog |     463.2 |           444.2 |
| scs      |     168.0 |           162.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. Here are the shifted geometric
means of solver primal errors (1.0 is the best):

|          |       default |    high_accuracy |
|:---------|--------------:|-----------------:|
| cvxopt   |     1265879.8 |     4364662336.9 |
| ecos     |     1371636.4 |     4729303555.6 |
| highs    |      344202.0 |     1186783808.0 |
| osqp     |      798784.5 |     2400713695.4 |
| proxqp   |           1.0 |              1.0 |
| qpswift  |     1265879.8 |     4364662336.8 |
| quadprog |      978548.1 |     3373963557.3 |
| scs      | 11712300201.7 | 40383163869509.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal error limit](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. Here are the shifted
geometric means of solver cost errors (1.0 is the best):

|          |     default |   high_accuracy |
|:---------|------------:|----------------:|
| cvxopt   |      1037.8 |          1591.7 |
| ecos     |      1426.8 |          2188.4 |
| highs    |        42.5 |            65.1 |
| osqp     |       123.9 |           258.1 |
| proxqp   |         1.0 |             1.0 |
| qpswift  |      1037.8 |          1591.7 |
| quadprog |       426.7 |           654.5 |
| scs      | 410691408.3 |     629922619.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
error limit](#settings).

## Package versions

Versions of all relevant packages used when running this test set:

| package   | version     |
|:----------|:------------|
| cvxopt    | 1.3.0       |
| ecos      | 2.0.10      |
| highs     | 1.1.2.dev3  |
| osqp      | 0.6.2.post0 |
| proxqp    | 0.2.4       |
| qpsolvers | 2.5.0       |
| qpswift   | 1.0.0       |
| quadprog  | 0.1.11      |
| scs       | 3.2.0       |

## See also

- [How not to lie with statistics: the correct way to summarize benchmark
  results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf):
  why geometric means should always be used to summarize normalized results.
