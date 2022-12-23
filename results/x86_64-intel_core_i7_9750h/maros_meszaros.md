# Maros-Meszaros test set

- Author: [@stephane-caron](https://github.com/stephane-caron/)
- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- Date: 2022-11-08 21:57:53.629027+00:00

## Solvers

| package   | version     |
|:----------|:------------|
| cvxopt    | 1.3.0       |
| osqp      | 0.6.2.post5 |
| proxqp    | 0.2.5       |
| scs       | 3.2.2       |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v2.5.0.

## Settings

- Cost tolerance: 1000.0
- Primal tolerance: 1.0
- Time limit: 1000.0 seconds

| solver   | parameter           | default   |   high_accuracy |
|:---------|:--------------------|:----------|----------------:|
| cvxopt   | ``feastol``         | -         |           1e-09 |
| osqp     | ``eps_abs``         | -         |           1e-09 |
| osqp     | ``eps_rel``         | -         |           0     |
| osqp     | ``time_limit``      | 1000.0    |        1000     |
| proxqp   | ``eps_abs``         | -         |           1e-09 |
| proxqp   | ``eps_rel``         | -         |           0     |
| scs      | ``eps_abs``         | -         |           1e-09 |
| scs      | ``eps_rel``         | -         |           0     |
| scs      | ``time_limit_secs`` | 1000.0    |        1000     |

## Metrics

We look at the following statistics:

- [Success rate](#success-rate)
- [Computation time](#computation-time)
- [Primal error](#primal-error)
- [Cost error](#cost-error)

They are presented in more detail in [Metrics](README.md#metrics).

## Results

### Success rate

Precentage of problems each solver is able to solve:

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |        16 |              16 |
| highs  |        60 |              60 |
| osqp   |        59 |              36 |
| proxqp |        81 |              76 |
| scs    |        32 |              33 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). Here is a summary of the frequency at which solvers
returned success (1) but the corresponding solution did not pass tolerance
checks:

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |       100 |             100 |
| highs  |        99 |              99 |
| osqp   |        73 |             100 |
| proxqp |        96 |              99 |
| scs    |        78 |              78 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |      53.5 |            20.1 |
| highs  |       6.2 |             2.3 |
| osqp   |       1.0 |             7.0 |
| proxqp |       2.1 |             1.0 |
| scs    |       9.6 |             4.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal errors over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal error of Y is Y times less precise
on constraints than the best solver over the test set. See
[Metrics](README.md#metrics) for details.

Shifted geometric means of solver primal errors (1.0 is the best):

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |       5.7 |             3.9 |
| highs  |       2.6 |             1.8 |
| osqp   |      52.1 |             2.9 |
| proxqp |       1.0 |             1.0 |
| scs    |   12941.6 |          7994.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal tolerance](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |      24.6 |            19.7 |
| highs  |       2.9 |             2.3 |
| osqp   |      26.1 |             7.7 |
| proxqp |       1.0 |             1.0 |
| scs    |  433062.8 |        312789.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
