# Maros-Meszaros test set

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-01-26 14:30:51.623545+00:00 |
| CPU     | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| Run by  | [@stephane-caron](https://github.com/stephane-caron/) |

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [Known limitations](#known-limitations)
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
| proxqp   | 0.3.2                 |
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
| proxqp   | ``check_duality_gap``            | -         |           1     |          1     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| proxqp   | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |
| proxqp   | ``eps_duality_gap_rel``          | -         |           0     |          0     |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``time_limit_secs``              | 1000.0    |        1000     |       1000     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpsolvers_benchmark/issues)
have been identified as impacting the fairness of this benchmark. Keep them in
mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpsolvers_benchmark/issues/60):
  Conversion to SOCP limits performance of ECOS

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|        |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:-------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt |                                19.6 |                                 50.1 |                                         5.6 |                                     5.6 |                                 1.9 |                              20.2 |
| gurobi |                                16.7 |                                 33.8 |                                         5.2 |                                    37.5 |                                16.7 |                              15.9 |
| highs  |                                53.6 |                                  6.6 |                                         2.6 |                                     2.6 |                                 3.8 |                               2.8 |
| osqp   |                                41.3 |                                  1.0 |                                        30.4 |                                    22.9 |                               384.5 |                              20.9 |
| proxqp |                                76.8 |                                  2.7 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| scs    |                                60.1 |                                  1.2 |                                        18.7 |                                     3.4 |                                23.7 |                               3.8 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|        |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:-------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt |                                 0.0 |                                 11.6 |                                         6.8 |                                  1667.7 |                         105162189.5 |                              11.4 |
| gurobi |                                 5.1 |                                  7.8 |                                         3.0 |                            7247695596.0 |                        9769259351.6 |                               8.9 |
| highs  |                                 0.0 |                                  1.5 |                                      3766.3 |                                894822.1 |                        1987500500.6 |                               1.6 |
| osqp   |                                25.4 |                                  4.7 |                                         2.0 |                                     1.2 |                              3235.7 |                               5.3 |
| proxqp |                                57.2 |                                  1.0 |                                         1.0 |                                     1.0 |                              9664.6 |                               1.0 |
| scs    |                                42.8 |                                  3.2 |                                         1.8 |                                     1.1 |                                 1.0 |                               3.4 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|        |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:-------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt |                                13.8 |                                 19.8 |                                         3.9 |                                     4.5 |                               188.2 |                              20.3 |
| gurobi |                                16.7 |                                 13.4 |                                         3.6 |                                 23832.8 |                             17288.7 |                              15.9 |
| highs  |                                37.7 |                                  2.6 |                                         1.9 |                                     5.1 |                              3517.8 |                               2.8 |
| osqp   |                                21.0 |                                  2.5 |                                         2.9 |                                     3.3 |                              3206.0 |                               4.0 |
| proxqp |                                78.3 |                                  1.0 |                                         1.0 |                                     1.0 |                                12.6 |                               1.0 |
| scs    |                                71.0 |                                  1.2 |                                        31.7 |                                     2.2 |                                 1.0 |                               1.5 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |        20 |               0 |             14 |
| gurobi |        17 |               5 |             17 |
| highs  |        54 |               0 |             38 |
| osqp   |        41 |              25 |             21 |
| proxqp |        77 |              57 |             78 |
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
| proxqp |        91 |              86 |             95 |
| scs    |        72 |              97 |             95 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|        |   default |   high_accuracy |   low_accuracy |
|:-------|----------:|----------------:|---------------:|
| cvxopt |      50.1 |            11.6 |           19.8 |
| gurobi |      33.8 |             7.8 |           13.4 |
| highs  |       6.6 |             1.5 |            2.6 |
| osqp   |       1.0 |             4.7 |            2.5 |
| proxqp |       2.7 |             1.0 |            1.0 |
| scs    |       1.2 |             3.2 |            1.2 |

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
| cvxopt |       5.6 |             6.8 |            3.9 |
| gurobi |       5.2 |             3.0 |            3.6 |
| highs  |       2.6 |          3766.3 |            1.9 |
| osqp   |      30.4 |             2.0 |            2.9 |
| proxqp |       1.0 |             1.0 |            1.0 |
| scs    |      18.7 |             1.8 |           31.7 |

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
| cvxopt |       5.6 |          1667.7 |            4.5 |
| gurobi |      37.5 |    7247695596.0 |        23832.8 |
| highs  |       2.6 |        894822.1 |            5.1 |
| osqp   |      22.9 |             1.2 |            3.3 |
| proxqp |       1.0 |             1.0 |            1.0 |
| scs    |       3.4 |             1.1 |            2.2 |

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
| cvxopt |       1.9 |     105162189.5 |          188.2 |
| gurobi |      16.7 |    9769259351.6 |        17288.7 |
| highs  |       3.8 |    1987500500.6 |         3517.8 |
| osqp   |     384.5 |          3235.7 |         3206.0 |
| proxqp |       1.0 |          9664.6 |           12.6 |
| scs    |      23.7 |             1.0 |            1.0 |

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
| cvxopt |      20.2 |            11.4 |           20.3 |
| gurobi |      15.9 |             8.9 |           15.9 |
| highs  |       2.8 |             1.6 |            2.8 |
| osqp   |      20.9 |             5.3 |            4.0 |
| proxqp |       1.0 |             1.0 |            1.0 |
| scs    |       3.8 |             3.4 |            1.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
