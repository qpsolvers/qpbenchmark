# Maros-Meszaros test set

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-01-04 13:04:08.861409+00:00 |
| CPU     | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| Run by  | [@stephane-caron](https://github.com/stephane-caron/) |

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [Results by settings](#results-by-settings)
    * [Default](#default)
    * [High accuracy](#high-accuracy)
    * [Low accuracy](#low-accuracy)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)
    * [Cost error](#cost-error)

## Description

Standard set of problems designed to be difficult.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| cvxopt   | 1.3.0                 |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.1.2.dev3            |
| osqp     | 0.6.2.post5           |
| proxqp   | 0.2.7                 |
| scs      | 3.2.2                 |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers)
v2.7.2.

## Settings

There are 3 settings: *default*, *high_accuracy*
and *low_accuracy*. They validate solutions using the following
tolerances:

| tolerance   |   default |   low_accuracy |   high_accuracy |
|:------------|----------:|---------------:|----------------:|
| ``cost``    |      1000 |       1000     |        1000     |
| ``dual``    |         1 |          0.001 |           1e-09 |
| ``gap``     |         1 |          0.001 |           1e-09 |
| ``primal``  |         1 |          0.001 |           1e-09 |
| ``runtime`` |      1000 |       1000     |        1000     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |   low_accuracy |
|:---------|:---------------------------------|:----------|----------------:|---------------:|
| cvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |
| gurobi   | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |
| gurobi   | ``OptimalityTol``                | -         |           1e-09 |          0.001 |
| gurobi   | ``TimeLimit``                    | 1000.0    |        1000     |       1000     |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |
| highs    | ``time_limit``                   | 1000.0    |        1000     |       1000     |
| osqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| osqp     | ``eps_rel``                      | -         |           0     |          0     |
| osqp     | ``time_limit``                   | 1000.0    |        1000     |       1000     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``time_limit_secs``              | 1000.0    |        1000     |       1000     |

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|        |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:-------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt |                                19.6 |                                 50.1 |                                         5.6 |                                     5.6 |                                 2.1 |                              20.3 |
| gurobi |                                16.7 |                                 33.8 |                                         5.2 |                                    37.5 |                                18.7 |                              15.9 |
| highs  |                                53.6 |                                  6.6 |                                         2.6 |                                     2.6 |                                 4.2 |                               2.8 |
| osqp   |                                41.3 |                                  1.0 |                                        30.4 |                                    22.9 |                               430.1 |                              21.0 |
| proxqp |                                77.5 |                                  2.7 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| scs    |                                60.1 |                                  1.2 |                                        18.7 |                                     3.4 |                                26.5 |                               3.9 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|        |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:-------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt |                                 0.0 |                                 15.3 |                                         6.6 |                                  1599.3 |                         105162189.5 |                              16.2 |
| gurobi |                                 5.1 |                                 10.3 |                                         2.9 |                            6950494908.1 |                        9769259351.6 |                              12.7 |
| highs  |                                 0.0 |                                  2.0 |                                      3668.0 |                                858128.8 |                        1987500500.6 |                               2.2 |
| osqp   |                                25.4 |                                  6.2 |                                         1.9 |                                     1.2 |                              3235.7 |                               7.5 |
| proxqp |                                23.9 |                                  1.0 |                                         1.0 |                                     1.0 |                            119378.4 |                               1.0 |
| scs    |                                42.8 |                                  4.3 |                                         1.7 |                                     1.0 |                                 1.0 |                               4.9 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|        |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:-------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt |                                13.8 |                                 25.4 |                                         2.1 |                                     4.2 |                               188.2 |                              13.8 |
| gurobi |                                16.7 |                                 17.1 |                                         2.0 |                                 22303.0 |                             17288.7 |                              10.8 |
| highs  |                                37.7 |                                  3.3 |                                         1.0 |                                     4.8 |                              3517.8 |                               1.9 |
| osqp   |                                21.0 |                                  3.2 |                                         1.6 |                                     3.0 |                              3206.0 |                               2.7 |
| proxqp |                                16.7 |                                  1.0 |                                         1.0 |                                     1.0 |                             14292.6 |                               1.0 |
| scs    |                                71.0 |                                  1.5 |                                        17.3 |                                     2.0 |                                 1.0 |                               1.0 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |        20 |               0 |             14 |
| gurobi |        17 |               5 |             17 |
| highs  |        54 |               0 |             38 |
| osqp   |        41 |              25 |             21 |
| proxqp |        78 |              24 |             17 |
| scs    |        60 |              43 |             71 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution satisfies optimality conditions within
[tolerance](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |        99 |              79 |             93 |
| gurobi |        91 |              79 |             91 |
| highs  |        91 |              38 |             75 |
| osqp   |        54 |              88 |             61 |
| proxqp |        92 |              46 |             31 |
| scs    |        72 |              97 |             95 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |      50.1 |            15.3 |           25.4 |
| gurobi |      33.8 |            10.3 |           17.1 |
| highs  |       6.6 |             2.0 |            3.3 |
| osqp   |       1.0 |             6.2 |            3.2 |
| proxqp |       2.7 |             1.0 |            1.0 |
| scs    |       1.2 |             4.3 |            1.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time
limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal residuals over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal residual of Y is Y times less
precise on constraints than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |       5.6 |             6.6 |            2.1 |
| gurobi |       5.2 |             2.9 |            2.0 |
| highs  |       2.6 |          3668.0 |            1.0 |
| osqp   |      30.4 |             1.9 |            1.6 |
| proxqp |       1.0 |             1.0 |            1.0 |
| scs    |      18.7 |             1.7 |           17.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal residual equal to the
full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility
condition in the solution returned by a solver. We use the shifted geometric
mean to compare solver dual residuals over the whole test set. Intuitively, a
solver with a shifted-geometric-mean dual residual of Y is Y times less precise
on the dual feasibility condition than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |       5.6 |          1599.3 |            4.2 |
| gurobi |      37.5 |    6950494908.1 |        22303.0 |
| highs  |       2.6 |        858128.8 |            4.8 |
| osqp   |      22.9 |             1.2 |            3.0 |
| proxqp |       1.0 |             1.0 |            1.0 |
| scs    |       3.4 |             1.0 |            2.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a dual residual equal to the full
[dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions
returned by a solver. A duality gap close to zero ensures that the
complementarity slackness optimality condition is satisfied. We use the shifted
geometric mean to compare solver duality gaps over the whole test set.
Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times
less precise on the complementarity slackness condition than the best solver
over the test set. See [Metrics](../README.md#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |       2.1 |     105162189.5 |          188.2 |
| gurobi |      18.7 |    9769259351.6 |        17288.7 |
| highs  |       4.2 |    1987500500.6 |         3517.8 |
| osqp   |     430.1 |          3235.7 |         3206.0 |
| proxqp |       1.0 |        119378.4 |        14292.6 |
| scs    |      26.5 |             1.0 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a duality gap equal to the full
[gap tolerance](#settings).

### Cost error

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |      20.3 |            16.2 |           13.8 |
| gurobi |      15.9 |            12.7 |           10.8 |
| highs  |       2.8 |             2.2 |            1.9 |
| osqp   |      21.0 |             7.5 |            2.7 |
| proxqp |       1.0 |             1.0 |            1.0 |
| scs    |       3.9 |             4.9 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
