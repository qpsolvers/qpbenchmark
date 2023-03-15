# GitHub free-for-all test set

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-03-15 16:52:46.067045+00:00 |
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

Problems in this test set:

- [GHFFA01](https://github.com/stephane-caron/qpsolvers_benchmark/issues/25): Project the origin on a 2D line that becomes vertical.
- [GHFFA02](https://github.com/stephane-caron/qpsolvers_benchmark/issues/27): Linear system with two variables and a large condition number.
- [GHFFA03](https://github.com/stephane-caron/qpsolvers_benchmark/issues/29): Ill-conditioned unconstrained least squares.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.4.1                 |
| cvxopt   | 1.3.0                 |
| ecos     | 2.0.10                |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.1.2.dev3            |
| osqp     | 0.6.2.post5           |
| proxqp   | 0.3.6                 |
| qpoases  | 3.2.1                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.11                |
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
| ``runtime`` |       100 |        100     |         100     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   | high_accuracy          | low_accuracy          |
|:---------|:---------------------------------|:----------|:-----------------------|:----------------------|
| clarabel | ``tol_feas``                     | -         | 1e-09                  | 0.001                 |
| clarabel | ``tol_gap_abs``                  | -         | 1e-09                  | 0.001                 |
| clarabel | ``tol_gap_rel``                  | -         | 0.0                    | 0.0                   |
| cvxopt   | ``feastol``                      | -         | 1e-09                  | 0.001                 |
| ecos     | ``feastol``                      | -         | 1e-09                  | 0.001                 |
| gurobi   | ``FeasibilityTol``               | -         | 1e-09                  | 0.001                 |
| gurobi   | ``OptimalityTol``                | -         | 1e-09                  | 0.001                 |
| gurobi   | ``TimeLimit``                    | 100.0     | 100.0                  | 100.0                 |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09                  | 0.001                 |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09                  | 0.001                 |
| highs    | ``time_limit``                   | 100.0     | 100.0                  | 100.0                 |
| osqp     | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| osqp     | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| osqp     | ``time_limit``                   | 100.0     | 100.0                  | 100.0                 |
| proxqp   | ``check_duality_gap``            | -         | 1.0                    | 1.0                   |
| proxqp   | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09                  | 0.001                 |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0                    | 0.0                   |
| proxqp   | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| qpoases  | ``predefined_options``           | default   | reliable               | fast                  |
| qpoases  | ``time_limit``                   | 100.0     | 100.0                  | 100.0                 |
| qpswift  | ``RELTOL``                       | -         | 1.7320508075688772e-09 | 0.0017320508075688772 |
| scs      | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| scs      | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| scs      | ``time_limit_secs``              | 100.0     | 100.0                  | 100.0                 |

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
| clarabel |                                63.6 |                                  5.7 |                                         4.1 |                                     4.1 |                                 4.1 |                               3.3 |
| cvxopt   |                                63.6 |                                  3.8 |                                         3.0 |                                     3.0 |                               392.9 |                              10.6 |
| ecos     |                                45.5 |                                 11.1 |                                         6.1 |                                     6.1 |                                 6.1 |                               8.5 |
| gurobi   |                                81.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.4 |
| highs    |                                45.5 |                                  2.3 |                                         2.0 |                                   512.4 |                              1427.0 |                               1.0 |
| osqp     |                                54.5 |                                  5.7 |                                         4.1 |                                    71.9 |                                 4.1 |                               5.0 |
| proxqp   |                                50.0 |                                  7.0 |                                         4.7 |                                     4.7 |                                46.5 |                               6.2 |
| qpoases  |                                72.7 |                                  1.0 |                                         1.0 |                                     2.9 |                                 1.0 |                               1.4 |
| qpswift  |                                 0.0 |                                 41.1 |                                        11.5 |                                    11.5 |                                11.5 |                              74.9 |
| quadprog |                                72.7 |                                  3.8 |                                         3.0 |                                     3.0 |                                 3.0 |                               1.9 |
| scs      |                                63.6 |                                  5.7 |                                         4.1 |                                     4.1 |                                 4.5 |                               3.3 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                54.5 |                                  5.7 |                                         4.0 |                                     4.0 |                                18.8 |                               3.3 |
| cvxopt   |                                45.5 |                                  3.8 |                                     88898.4 |                                     3.0 |                      361808922792.9 |                              10.6 |
| ecos     |                                 0.0 |                                 11.1 |                                         6.0 |                                314633.8 |                            314633.8 |                               8.5 |
| gurobi   |                                81.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.4 |
| highs    |                                 0.0 |                                  2.3 |                                         2.0 |                          477792868971.8 |                     1333969483708.8 |                               1.0 |
| osqp     |                                54.5 |                                  8.1 |                                         5.0 |                                     5.0 |                                 5.0 |                               5.4 |
| proxqp   |                                58.3 |                                  7.0 |                                         9.1 |                                     4.6 |                                 9.1 |                               4.4 |
| qpoases  |                                63.6 |                                  1.0 |                                         1.0 |                            1829234566.4 |                            242920.3 |                               1.4 |
| qpswift  |                                 0.0 |                                 41.1 |                                        11.0 |                                    10.9 |                                10.9 |                              74.9 |
| quadprog |                                54.5 |                                  3.8 |                                         3.0 |                                121478.1 |                            242937.1 |                               1.9 |
| scs      |                                54.5 |                                  8.1 |                                         5.0 |                                     5.0 |                                 5.6 |                               5.4 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                63.6 |                                  5.7 |                                         4.0 |                                     4.0 |                                 4.8 |                               3.3 |
| cvxopt   |                                54.5 |                                  3.8 |                                         3.1 |                                     3.0 |                            363653.4 |                              10.6 |
| ecos     |                                45.5 |                                 11.1 |                                         6.0 |                                     6.3 |                                 6.3 |                               8.5 |
| gurobi   |                                81.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.4 |
| highs    |                                27.3 |                                  2.3 |                                         2.0 |                                480222.3 |                           1340748.7 |                               1.0 |
| osqp     |                                54.5 |                                  6.1 |                                         5.1 |                                     8.4 |                                 7.5 |                               5.0 |
| proxqp   |                                58.3 |                                  7.0 |                                         9.2 |                                     4.6 |                                10.1 |                               4.4 |
| qpoases  |                                72.7 |                                  1.0 |                                         1.0 |                                  1839.5 |                                 1.2 |                               1.4 |
| qpswift  |                                 0.0 |                                 41.1 |                                        11.0 |                                    11.0 |                                11.0 |                              74.9 |
| quadprog |                                72.7 |                                  3.8 |                                         3.0 |                                     3.1 |                                 3.2 |                               1.9 |
| scs      |                                63.6 |                                  5.7 |                                         4.0 |                                     4.0 |                                 4.0 |                               3.3 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        64 |              55 |             64 |
| cvxopt   |        64 |              45 |             55 |
| ecos     |        45 |               0 |             45 |
| gurobi   |        82 |              82 |             82 |
| highs    |        45 |               0 |             27 |
| osqp     |        55 |              55 |             55 |
| proxqp   |        50 |              58 |             58 |
| qpoases  |        73 |              64 |             73 |
| qpswift  |         0 |               0 |              0 |
| quadprog |        73 |              55 |             73 |
| scs      |        64 |              55 |             64 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution satisfies optimality conditions within
[tolerance](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              91 |            100 |
| cvxopt   |        91 |              73 |             82 |
| ecos     |       100 |              55 |            100 |
| gurobi   |        91 |              91 |             91 |
| highs    |        64 |              18 |             45 |
| osqp     |        91 |             100 |             91 |
| proxqp   |        92 |             100 |            100 |
| qpoases  |        82 |              73 |             82 |
| qpswift  |       100 |             100 |            100 |
| quadprog |       100 |              82 |            100 |
| scs      |       100 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       5.7 |             5.7 |            5.7 |
| cvxopt   |       3.8 |             3.8 |            3.8 |
| ecos     |      11.1 |            11.1 |           11.1 |
| gurobi   |       1.0 |             1.0 |            1.0 |
| highs    |       2.3 |             2.3 |            2.3 |
| osqp     |       5.7 |             8.1 |            6.1 |
| proxqp   |       7.0 |             7.0 |            7.0 |
| qpoases  |       1.0 |             1.0 |            1.0 |
| qpswift  |      41.1 |            41.1 |           41.1 |
| quadprog |       3.8 |             3.8 |            3.8 |
| scs      |       5.7 |             8.1 |            5.7 |

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
| clarabel |       4.1 |             4.0 |            4.0 |
| cvxopt   |       3.0 |         88898.4 |            3.1 |
| ecos     |       6.1 |             6.0 |            6.0 |
| gurobi   |       1.0 |             1.0 |            1.0 |
| highs    |       2.0 |             2.0 |            2.0 |
| osqp     |       4.1 |             5.0 |            5.1 |
| proxqp   |       4.7 |             9.1 |            9.2 |
| qpoases  |       1.0 |             1.0 |            1.0 |
| qpswift  |      11.5 |            11.0 |           11.0 |
| quadprog |       3.0 |             3.0 |            3.0 |
| scs      |       4.1 |             5.0 |            4.0 |

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
| clarabel |       4.1 |             4.0 |            4.0 |
| cvxopt   |       3.0 |             3.0 |            3.0 |
| ecos     |       6.1 |        314633.8 |            6.3 |
| gurobi   |       1.0 |             1.0 |            1.0 |
| highs    |     512.4 |  477792868971.8 |       480222.3 |
| osqp     |      71.9 |             5.0 |            8.4 |
| proxqp   |       4.7 |             4.6 |            4.6 |
| qpoases  |       2.9 |    1829234566.4 |         1839.5 |
| qpswift  |      11.5 |            10.9 |           11.0 |
| quadprog |       3.0 |        121478.1 |            3.1 |
| scs      |       4.1 |             5.0 |            4.0 |

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
| clarabel |       4.1 |            18.8 |            4.8 |
| cvxopt   |     392.9 |  361808922792.9 |       363653.4 |
| ecos     |       6.1 |        314633.8 |            6.3 |
| gurobi   |       1.0 |             1.0 |            1.0 |
| highs    |    1427.0 | 1333969483708.8 |      1340748.7 |
| osqp     |       4.1 |             5.0 |            7.5 |
| proxqp   |      46.5 |             9.1 |           10.1 |
| qpoases  |       1.0 |        242920.3 |            1.2 |
| qpswift  |      11.5 |            10.9 |           11.0 |
| quadprog |       3.0 |        242937.1 |            3.2 |
| scs      |       4.5 |             5.6 |            4.0 |

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
| clarabel |       3.3 |             3.3 |            3.3 |
| cvxopt   |      10.6 |            10.6 |           10.6 |
| ecos     |       8.5 |             8.5 |            8.5 |
| gurobi   |       1.4 |             1.4 |            1.4 |
| highs    |       1.0 |             1.0 |            1.0 |
| osqp     |       5.0 |             5.4 |            5.0 |
| proxqp   |       6.2 |             4.4 |            4.4 |
| qpoases  |       1.4 |             1.4 |            1.4 |
| qpswift  |      74.9 |            74.9 |           74.9 |
| quadprog |       1.9 |             1.9 |            1.9 |
| scs      |       3.3 |             5.4 |            3.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
