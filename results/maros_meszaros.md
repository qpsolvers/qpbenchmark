# Maros-Meszaros test set

- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-11-09 21:45:47.569562+00:00
- Run by: [@stephane-caron](https://github.com/stephane-caron/)

## Solvers

| solver   | version     |
|:---------|:------------|
| cvxopt   | 1.3.0       |
| highs    | 1.1.2.dev3  |
| osqp     | 0.6.2.post5 |
| proxqp   | 0.2.5       |
| scs      | 3.2.2       |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v2.6.0rc2.

## Settings

There are 2 settings: **default** and
**high_accuracy**. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |
|:------------|----------:|----------------:|
| ``cost``    |      1000 |        1000     |
| ``primal``  |         1 |           1e-09 |
| ``runtime`` |      1000 |        1000     |

Solvers for each group of settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |
|:---------|:---------------------------------|:----------|----------------:|
| cvxopt   | ``feastol``                      | -         |           1e-09 |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |
| highs    | ``time_limit``                   | 1000.0    |        1000     |
| osqp     | ``eps_abs``                      | -         |           1e-09 |
| osqp     | ``eps_rel``                      | -         |           0     |
| osqp     | ``time_limit``                   | 1000.0    |        1000     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |
| proxqp   | ``eps_rel``                      | -         |           0     |
| scs      | ``eps_abs``                      | -         |           1e-09 |
| scs      | ``eps_rel``                      | -         |           0     |
| scs      | ``time_limit_secs``              | 1000.0    |        1000     |

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

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |        16 |              12 |
| highs  |        60 |              56 |
| osqp   |        59 |              36 |
| proxqp |        81 |              75 |
| scs    |        33 |              21 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). Here is a summary of the frequency at which solvers
returned success (1) but the corresponding solution did not pass tolerance
checks:

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |       100 |              96 |
| highs  |        99 |              95 |
| osqp   |        73 |             100 |
| proxqp |        96 |              98 |
| scs    |        99 |              96 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |      54.0 |            19.5 |
| highs  |       6.1 |             2.2 |
| osqp   |       1.0 |             6.6 |
| proxqp |       2.4 |             1.0 |
| scs    |      23.2 |            14.0 |

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

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |       5.7 |             6.5 |
| highs  |       2.6 |          3510.9 |
| osqp   |      52.1 |             1.8 |
| proxqp |       1.0 |             1.0 |
| scs    |      11.8 |     160597376.4 |

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

|        |   default |   high_accuracy |
|:-------|----------:|----------------:|
| cvxopt |      24.5 |            19.7 |
| highs  |       2.9 |             2.3 |
| osqp   |      26.0 |             7.7 |
| proxqp |       1.0 |             1.0 |
| scs    |      12.5 |            14.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
