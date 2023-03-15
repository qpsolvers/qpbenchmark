# Maros-Meszaros test set

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-03-15 16:04:45.650801+00:00 |
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
| clarabel | 0.4.1                 |
| cvxopt   | 1.3.0                 |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.1.2.dev3            |
| osqp     | 0.6.2.post5           |
| proxqp   | 0.3.2                 |
| scs      | 3.2.2                 |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers)
v3.0.0.

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
| clarabel | ``tol_feas``                     | -         |           1e-09 |          0.001 |
| clarabel | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |
| clarabel | ``tol_gap_rel``                  | -         |           0     |          0     |
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

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                89.9 |                                  1.0 |                                         1.0 |                                     1.9 |                                 1.0 |                               1.0 |
| cvxopt   |                                19.6 |                                 85.7 |                                        11.2 |                                     5.6 |                                10.6 |                              44.4 |
| gurobi   |                                16.7 |                                 57.8 |                                        10.5 |                                    37.5 |                                94.0 |                              34.9 |
| highs    |                                53.6 |                                 11.3 |                                         5.3 |                                     2.6 |                                21.2 |                               6.1 |
| osqp     |                                41.3 |                                  1.7 |                                        60.7 |                                    22.9 |                              2160.0 |                              45.9 |
| proxqp   |                                76.8 |                                  4.6 |                                         2.0 |                                     1.0 |                                 5.6 |                               2.2 |
| scs      |                                60.1 |                                  2.1 |                                        37.5 |                                     3.4 |                               133.1 |                               8.4 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                61.6 |                                  1.0 |                                         1.0 |                                751257.0 |                                44.9 |                               1.0 |
| cvxopt   |                                 0.0 |                                 28.4 |                                         9.8 |                                  1667.7 |                         105162189.5 |                              25.2 |
| gurobi   |                                 5.1 |                                 19.2 |                                         4.3 |                            7247695596.0 |                        9769259351.6 |                              19.8 |
| highs    |                                 0.0 |                                  3.7 |                                      5416.6 |                                894822.1 |                        1987500500.6 |                               3.5 |
| osqp     |                                25.4 |                                 11.5 |                                         2.8 |                                     1.2 |                              3235.7 |                              11.7 |
| proxqp   |                                57.2 |                                  2.5 |                                         1.4 |                                     1.0 |                              9664.6 |                               2.2 |
| scs      |                                42.8 |                                  8.0 |                                         2.5 |                                     1.1 |                                 1.0 |                               7.6 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                91.3 |                                  1.0 |                                         1.8 |                                  1094.5 |                                 1.0 |                               1.0 |
| cvxopt   |                                13.8 |                                157.8 |                                         3.9 |                                     4.5 |                               292.6 |                              58.0 |
| gurobi   |                                16.7 |                                106.4 |                                         3.6 |                                 23832.8 |                             26882.1 |                              45.5 |
| highs    |                                37.7 |                                 20.8 |                                         1.9 |                                     5.1 |                              5469.8 |                               8.0 |
| osqp     |                                21.0 |                                 19.7 |                                         2.9 |                                     3.3 |                              4985.0 |                              11.6 |
| proxqp   |                                78.3 |                                  8.0 |                                         1.0 |                                     1.0 |                                19.6 |                               2.9 |
| scs      |                                71.0 |                                  9.3 |                                        31.7 |                                     2.2 |                                 1.6 |                               4.2 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        90 |              62 |             91 |
| cvxopt   |        20 |               0 |             14 |
| gurobi   |        17 |               5 |             17 |
| highs    |        54 |               0 |             38 |
| osqp     |        41 |              25 |             21 |
| proxqp   |        77 |              57 |             78 |
| scs      |        60 |              43 |             71 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution satisfies optimality conditions within
[tolerance](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        97 |              80 |             95 |
| cvxopt   |        99 |              79 |             93 |
| gurobi   |        91 |              79 |             91 |
| highs    |        91 |              38 |             75 |
| osqp     |        54 |              88 |             61 |
| proxqp   |        91 |              86 |             95 |
| scs      |        72 |              97 |             95 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |
| cvxopt   |      85.7 |            28.4 |          157.8 |
| gurobi   |      57.8 |            19.2 |          106.4 |
| highs    |      11.3 |             3.7 |           20.8 |
| osqp     |       1.7 |            11.5 |           19.7 |
| proxqp   |       4.6 |             2.5 |            8.0 |
| scs      |       2.1 |             8.0 |            9.3 |

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

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.8 |
| cvxopt   |      11.2 |             9.8 |            3.9 |
| gurobi   |      10.5 |             4.3 |            3.6 |
| highs    |       5.3 |          5416.6 |            1.9 |
| osqp     |      60.7 |             2.8 |            2.9 |
| proxqp   |       2.0 |             1.4 |            1.0 |
| scs      |      37.5 |             2.5 |           31.7 |

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

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.9 |        751257.0 |         1094.5 |
| cvxopt   |       5.6 |          1667.7 |            4.5 |
| gurobi   |      37.5 |    7247695596.0 |        23832.8 |
| highs    |       2.6 |        894822.1 |            5.1 |
| osqp     |      22.9 |             1.2 |            3.3 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| scs      |       3.4 |             1.1 |            2.2 |

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

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |            44.9 |            1.0 |
| cvxopt   |      10.6 |     105162189.5 |          292.6 |
| gurobi   |      94.0 |    9769259351.6 |        26882.1 |
| highs    |      21.2 |    1987500500.6 |         5469.8 |
| osqp     |    2160.0 |          3235.7 |         4985.0 |
| proxqp   |       5.6 |          9664.6 |           19.6 |
| scs      |     133.1 |             1.0 |            1.6 |

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

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |
| cvxopt   |      44.4 |            25.2 |           58.0 |
| gurobi   |      34.9 |            19.8 |           45.5 |
| highs    |       6.1 |             3.5 |            8.0 |
| osqp     |      45.9 |            11.7 |           11.6 |
| proxqp   |       2.2 |             2.2 |            2.9 |
| scs      |       8.4 |             7.6 |            4.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
