# Maros-Meszaros test set

- Author: [@stephane-caron](https://github.com/stephane-caron/)
- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-11-07 11:34:58.075526+00:00

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

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |        16 |              16 |
| highs  |        61 |              61 |
| osqp   |        64 |              36 |
| proxqp |        72 |              72 |
| scs    |        54 |              53 |

Rows are solvers and columns are solver settings.

### Computation time

We compare solver computation times over the whole test set using the [shifted
geometric mean](#shifted-geometric-mean). Intuitively, a solver with a
shifted-geometric-mean runtime of Y is Y times slower than the best solver over
the test set.

Shifted geometric mean of solver computation times (1.0 is the best):

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |      16.8 |            16.6 |
| highs  |       1.9 |             1.9 |
| osqp   |       1.3 |             5.6 |
| proxqp |       1.0 |             1.0 |
| scs    |       3.2 |             4.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. Here are the shifted geometric
means of solver primal errors (1.0 is the best):

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |       3.1 |             3.1 |
| highs  |       1.4 |             1.4 |
| osqp   |       4.5 |             2.4 |
| proxqp |       1.0 |             1.0 |
| scs    |    6680.3 |          6501.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal error limit](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. Here are the shifted
geometric means of solver cost errors (1.0 is the best):

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |      15.9 |            16.1 |
| highs  |       1.9 |             1.9 |
| osqp   |       3.9 |             6.3 |
| proxqp |       1.0 |             1.0 |
| scs    |  241057.5 |        261034.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
error limit](#settings).

## Package versions

Versions of all relevant packages used when running this test set:

| package   | version     |
|:----------|:------------|
| cvxopt    | 1.3.0       |
| highs     | 1.1.2.dev3  |
| osqp      | 0.6.2.post0 |
| proxqp    | 0.2.4       |
| qpsolvers | 2.5.1rc0    |
| scs       | 3.2.0       |

## See also

- [How not to lie with statistics: the correct way to summarize benchmark
  results](https://www.cse.unsw.edu.au/~cs9242/18/papers/Fleming_Wallace_86.pdf):
  why geometric means should always be used to summarize normalized results.
