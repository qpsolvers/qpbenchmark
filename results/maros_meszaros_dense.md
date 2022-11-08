# Maros-Meszaros dense subset

- Author: [@stephane-caron](https://github.com/stephane-caron/)
- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-11-08 18:33:13.323571+00:00

## Solvers

| solver   | version     |
|:---------|:------------|
| cvxopt   | 1.3.0       |
| ecos     | 2.0.10      |
| highs    | 1.1.2.dev3  |
| osqp     | 0.6.2.post0 |
| proxqp   | 0.2.5       |
| qpoases  | 3.2.0       |
| qpswift  | 1.0.0       |
| quadprog | 0.1.11      |
| scs      | 3.2.0       |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v2.6.0rc1.

## Settings

- Cost tolerance: 1000.0
- Primal tolerance: 1.0
- Time limit: 1000.0 seconds

| solver   | parameter                        | default   |   high_accuracy |
|:---------|:---------------------------------|:----------|----------------:|
| cvxopt   | ``feastol``                      | -         |     1e-09       |
| ecos     | ``feastol``                      | -         |     1e-09       |
| highs    | ``dual_feasibility_tolerance``   | -         |     1e-09       |
| highs    | ``primal_feasibility_tolerance`` | -         |     1e-09       |
| highs    | ``time_limit``                   | 1000.0    |  1000           |
| osqp     | ``eps_abs``                      | -         |     1e-09       |
| osqp     | ``eps_rel``                      | -         |     0           |
| osqp     | ``time_limit``                   | 1000.0    |  1000           |
| proxqp   | ``eps_abs``                      | -         |     1e-09       |
| proxqp   | ``eps_rel``                      | -         |     0           |
| qpoases  | ``termination_tolerance``        | -         |     1e-07       |
| qpoases  | ``time_limit``                   | 1000.0    |  1000           |
| qpswift  | ``RELTOL``                       | -         |     1.73205e-09 |
| scs      | ``eps_abs``                      | -         |     1e-09       |
| scs      | ``eps_rel``                      | -         |     0           |
| scs      | ``time_limit_secs``              | 1000.0    |  1000           |

## Metrics

We look at the following statistics:

- [Success rate](#success-rate)
- [Computation time](#computation-time)
- [Primal error](#primal-error)
- [Cost error](#cost-error)

They are presented in more detail in [Metrics](../README.md#metrics).

## Results

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |        15 |              15 |
| ecos     |         8 |               8 |
| highs    |        76 |              76 |
| osqp     |        68 |              53 |
| proxqp   |       100 |             100 |
| qpoases  |        76 |              76 |
| qpswift  |        15 |              15 |
| quadprog |        34 |              34 |
| scs      |        29 |              27 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). Here is a summary of the frequency at which solvers
returned success (1) but the corresponding solution did not pass tolerance
checks:

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |       100 |             100 |
| ecos     |       100 |             100 |
| highs    |       100 |             100 |
| osqp     |        75 |             100 |
| proxqp   |       100 |             100 |
| qpoases  |        78 |              78 |
| qpswift  |       100 |             100 |
| quadprog |       100 |             100 |
| scs      |       100 |             100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |    1581.5 |          1466.4 |
| ecos     |    2174.0 |          2015.9 |
| highs    |      66.8 |            61.9 |
| osqp     |      12.0 |           237.9 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |       9.0 |             8.4 |
| qpswift  |    1581.1 |          1466.1 |
| quadprog |     650.1 |           602.8 |
| scs      |     830.9 |           835.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal errors over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal error of Y is Y times less precise
on constraints than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver primal errors (1.0 is the best):

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |  527043.5 |    4394430787.5 |
| ecos     |  571074.8 |    4761558980.4 |
| highs    |  143307.0 |    1194878068.7 |
| osqp     | 9053101.1 |    2417087362.5 |
| proxqp   |       1.0 |             1.0 |
| qpoases  | 8920845.0 |   74381031642.9 |
| qpswift  |  527043.5 |    4394430787.2 |
| quadprog |  407414.2 |    3396975112.1 |
| scs      |  440625.3 |    3757637166.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal tolerance](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |    1037.8 |          1591.7 |
| ecos     |    1426.8 |          2188.4 |
| highs    |      42.5 |            65.1 |
| osqp     |     123.9 |           258.1 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |     255.7 |           392.2 |
| qpswift  |    1037.8 |          1591.7 |
| quadprog |     426.7 |           654.5 |
| scs      |     547.5 |           906.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
