# GitHub free-for-all test set

| Version | 1.1.0rc0 |
|:--------|:--------------------|
| Date    | 2023-08-17 15:22:44.257029+00:00 |
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
| clarabel | 0.5.1                 |
| cvxopt   | 1.3.2                 |
| daqp     | 0.5.1                 |
| ecos     | 2.0.11                |
| gurobi   | 10.0.2 (size-limited) |
| highs    | 1.5.3                 |
| osqp     | 0.6.3                 |
| proxqp   | 0.4.1                 |
| qpoases  | 3.2.1                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.11                |
| scs      | 3.2.3                 |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers)
v3.5.0.

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
| daqp     | ``dual_tol``                     | -         | 1e-09                  | 0.001                 |
| daqp     | ``primal_tol``                   | -         | 1e-09                  | 0.001                 |
| ecos     | ``feastol``                      | -         | 1e-09                  | 0.001                 |
| gurobi   | ``FeasibilityTol``               | -         | 1e-09                  | 0.001                 |
| gurobi   | ``OptimalityTol``                | -         | 1e-09                  | 0.001                 |
| gurobi   | ``TimeLimit``                    | 100.0     | 100.0                  | 100.0                 |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09                  | 0.001                 |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09                  | 0.001                 |
| highs    | ``time_limit``                   | 100.0     | 100.0                  | 100.0                 |
| hpipm    | ``tol_comp``                     | -         | 1e-09                  | 0.001                 |
| hpipm    | ``tol_eq``                       | -         | 1e-09                  | 0.001                 |
| hpipm    | ``tol_ineq``                     | -         | 1e-09                  | 0.001                 |
| hpipm    | ``tol_stat``                     | -         | 1e-09                  | 0.001                 |
| osqp     | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| osqp     | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| osqp     | ``time_limit``                   | 100.0     | 100.0                  | 100.0                 |
| proxqp   | ``check_duality_gap``            | -         | True                   | True                  |
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
mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean)
(shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                63.6 |                               2701.0 |                                         2.2 |                                     2.2 |                                 2.3 |                               3.7 |
| cvxopt   |                                58.3 |                               2375.7 |                                         2.0 |                                     2.0 |                               183.3 |                              14.3 |
| daqp     |                                63.6 |                               2700.9 |                                         2.2 |                                     2.2 |                                 2.4 |                               3.7 |
| ecos     |                                41.7 |                               5920.5 |                                         3.6 |                                     3.6 |                                 3.6 |                              11.7 |
| gurobi   |                                75.0 |                                955.7 |                                         1.0 |                                     1.0 |                                 1.0 |                               2.4 |
| highs    |                                41.7 |                                981.7 |                                         1.0 |                                  1234.3 |                               612.5 |                               1.0 |
| hpipm    |                                63.6 |                                  1.0 |                                         1.1 |                                    15.0 |                               206.6 |                            5692.1 |
| osqp     |                                50.0 |                               2396.7 |                                         2.0 |                                    85.0 |                                 2.0 |                               6.6 |
| proxqp   |                                50.0 |                               3330.4 |                                         2.5 |                                     2.5 |                                25.3 |                               7.0 |
| qpoases  |                                66.7 |                                953.6 |                                         1.0 |                                     2.0 |                                 1.0 |                               2.4 |
| qpswift  |                                 0.0 |                              19408.6 |                                         6.2 |                                     6.2 |                                 6.2 |                              85.1 |
| quadprog |                                75.0 |                               1604.7 |                                         1.5 |                                     1.5 |                                 1.5 |                               2.8 |
| scs      |                                58.3 |                               3330.4 |                                         2.5 |                                     2.5 |                                 2.7 |                               5.0 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean)
(shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                54.5 |                               1856.6 |                                         2.2 |                                     2.2 |                                10.3 |                               3.7 |
| cvxopt   |                                41.7 |                               1633.0 |                                     44450.7 |                                     2.0 |                      168327208682.3 |                              14.3 |
| daqp     |                                45.5 |                               1856.6 |                                         4.3 |                                     2.2 |                         209710895.6 |                               3.7 |
| ecos     |                                 0.0 |                               4069.6 |                                         3.5 |                                157713.2 |                            157713.2 |                              11.7 |
| gurobi   |                                75.0 |                                656.2 |                                         1.0 |                                     1.0 |                                 1.0 |                               2.4 |
| highs    |                                 0.0 |                                673.7 |                                         1.0 |                         1163315301303.3 |                      576790866538.3 |                               1.0 |
| hpipm    |                                45.5 |                                  1.0 |                                1048846709.2 |                           14407044547.8 |                      197992946197.5 |                            5692.1 |
| osqp     |                                50.0 |                               3090.7 |                                         3.0 |                                     3.0 |                                 3.0 |                               7.7 |
| proxqp   |                                58.3 |                               2289.2 |                                         5.0 |                                     2.5 |                                 5.0 |                               5.0 |
| qpoases  |                                58.3 |                                655.5 |                                         1.0 |                             916283906.9 |                            121766.3 |                               2.4 |
| qpswift  |                                 0.0 |                              13341.1 |                                         6.0 |                                     6.0 |                                 6.0 |                              85.1 |
| quadprog |                                50.0 |                               1103.1 |                                         1.5 |                                144070.8 |                            121774.3 |                               2.8 |
| scs      |                                50.0 |                               3090.7 |                                         3.0 |                                     3.0 |                                 3.3 |                               7.7 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean)
(shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                63.6 |                               1884.4 |                                         4.4 |                                     2.2 |                                 2.6 |                               3.7 |
| cvxopt   |                                50.0 |                               1657.4 |                                         4.1 |                                     2.0 |                            168761.7 |                              14.3 |
| daqp     |                                54.5 |                               1884.4 |                                         4.4 |                                     2.2 |                               212.4 |                               3.7 |
| ecos     |                                41.7 |                               4130.6 |                                         7.0 |                                     3.7 |                                 3.7 |                              11.7 |
| gurobi   |                                75.0 |                                665.8 |                                         2.0 |                                     1.0 |                                 1.0 |                               2.4 |
| highs    |                                25.0 |                                684.3 |                                         2.0 |                               1166285.7 |                            578264.2 |                               1.0 |
| hpipm    |                                54.5 |                                  1.0 |                                      2097.8 |                                 14443.6 |                            198495.0 |                            5692.1 |
| osqp     |                                58.3 |                               1765.6 |                                         5.1 |                                     4.3 |                                 3.8 |                               6.6 |
| proxqp   |                                58.3 |                               2323.5 |                                        10.0 |                                     2.5 |                                 5.5 |                               5.0 |
| qpoases  |                                66.7 |                                302.6 |                                         1.0 |                                 70347.3 |                             70823.2 |                               2.1 |
| qpswift  |                                 0.0 |                              13540.9 |                                        12.0 |                                     6.0 |                                 6.0 |                              85.1 |
| quadprog |                                75.0 |                               1119.6 |                                         3.0 |                                     1.6 |                                 1.6 |                               2.8 |
| scs      |                                58.3 |                               2323.6 |                                         5.0 |                                     2.5 |                                 2.5 |                               5.0 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        64 |              55 |             64 |
| cvxopt   |        58 |              42 |             50 |
| daqp     |        64 |              45 |             55 |
| ecos     |        42 |               0 |             42 |
| gurobi   |        75 |              75 |             75 |
| highs    |        42 |               0 |             25 |
| hpipm    |        64 |              45 |             55 |
| osqp     |        50 |              50 |             58 |
| proxqp   |        50 |              58 |             58 |
| qpoases  |        67 |              58 |             67 |
| qpswift  |         0 |               0 |              0 |
| quadprog |        75 |              50 |             75 |
| scs      |        58 |              50 |             58 |

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
| cvxopt   |        92 |              75 |             83 |
| daqp     |       100 |              82 |             91 |
| ecos     |       100 |              58 |            100 |
| gurobi   |        92 |              92 |             92 |
| highs    |        58 |              17 |             42 |
| hpipm    |        64 |              45 |             55 |
| osqp     |        83 |             100 |             92 |
| proxqp   |        92 |             100 |            100 |
| qpoases  |        83 |              75 |             75 |
| qpswift  |       100 |             100 |            100 |
| quadprog |       100 |              75 |            100 |
| scs      |       100 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for
details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |    2701.0 |          1856.6 |         1884.4 |
| cvxopt   |    2375.7 |          1633.0 |         1657.4 |
| daqp     |    2700.9 |          1856.6 |         1884.4 |
| ecos     |    5920.5 |          4069.6 |         4130.6 |
| gurobi   |     955.7 |           656.2 |          665.8 |
| highs    |     981.7 |           673.7 |          684.3 |
| hpipm    |       1.0 |             1.0 |            1.0 |
| osqp     |    2396.7 |          3090.7 |         1765.6 |
| proxqp   |    3330.4 |          2289.2 |         2323.5 |
| qpoases  |     953.6 |           655.5 |          302.6 |
| qpswift  |   19408.6 |         13341.1 |        13540.9 |
| quadprog |    1604.7 |          1103.1 |         1119.6 |
| scs      |    3330.4 |          3090.7 |         2323.6 |

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
[Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for
details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       2.2 |             2.2 |            4.4 |
| cvxopt   |       2.0 |         44450.7 |            4.1 |
| daqp     |       2.2 |             4.3 |            4.4 |
| ecos     |       3.6 |             3.5 |            7.0 |
| gurobi   |       1.0 |             1.0 |            2.0 |
| highs    |       1.0 |             1.0 |            2.0 |
| hpipm    |       1.1 |    1048846709.2 |         2097.8 |
| osqp     |       2.0 |             3.0 |            5.1 |
| proxqp   |       2.5 |             5.0 |           10.0 |
| qpoases  |       1.0 |             1.0 |            1.0 |
| qpswift  |       6.2 |             6.0 |           12.0 |
| quadprog |       1.5 |             1.5 |            3.0 |
| scs      |       2.5 |             3.0 |            5.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal residual equal to the
full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility
condition in the solution returned by a solver. We use the shifted geometric
mean to compare solver dual residuals over the whole test set. Intuitively, a
solver with a shifted-geometric-mean dual residual of Y is Y times less precise
on the dual feasibility condition than the best solver over the test set. See
[Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for
details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       2.2 |             2.2 |            2.2 |
| cvxopt   |       2.0 |             2.0 |            2.0 |
| daqp     |       2.2 |             2.2 |            2.2 |
| ecos     |       3.6 |        157713.2 |            3.7 |
| gurobi   |       1.0 |             1.0 |            1.0 |
| highs    |    1234.3 | 1163315301303.3 |      1166285.7 |
| hpipm    |      15.0 |   14407044547.8 |        14443.6 |
| osqp     |      85.0 |             3.0 |            4.3 |
| proxqp   |       2.5 |             2.5 |            2.5 |
| qpoases  |       2.0 |     916283906.9 |        70347.3 |
| qpswift  |       6.2 |             6.0 |            6.0 |
| quadprog |       1.5 |        144070.8 |            1.6 |
| scs      |       2.5 |             3.0 |            2.5 |

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
over the test set. See
[Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for
details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       2.3 |            10.3 |            2.6 |
| cvxopt   |     183.3 |  168327208682.3 |       168761.7 |
| daqp     |       2.4 |     209710895.6 |          212.4 |
| ecos     |       3.6 |        157713.2 |            3.7 |
| gurobi   |       1.0 |             1.0 |            1.0 |
| highs    |     612.5 |  576790866538.3 |       578264.2 |
| hpipm    |     206.6 |  197992946197.5 |       198495.0 |
| osqp     |       2.0 |             3.0 |            3.8 |
| proxqp   |      25.3 |             5.0 |            5.5 |
| qpoases  |       1.0 |        121766.3 |        70823.2 |
| qpswift  |       6.2 |             6.0 |            6.0 |
| quadprog |       1.5 |        121774.3 |            1.6 |
| scs      |       2.7 |             3.3 |            2.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a duality gap equal to the full
[gap tolerance](#settings).

### Cost error

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for
details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       3.7 |             3.7 |            3.7 |
| cvxopt   |      14.3 |            14.3 |           14.3 |
| daqp     |       3.7 |             3.7 |            3.7 |
| ecos     |      11.7 |            11.7 |           11.7 |
| gurobi   |       2.4 |             2.4 |            2.4 |
| highs    |       1.0 |             1.0 |            1.0 |
| hpipm    |    5692.1 |          5692.1 |         5692.1 |
| osqp     |       6.6 |             7.7 |            6.6 |
| proxqp   |       7.0 |             5.0 |            5.0 |
| qpoases  |       2.4 |             2.4 |            2.1 |
| qpswift  |      85.1 |            85.1 |           85.1 |
| quadprog |       2.8 |             2.8 |            2.8 |
| scs      |       5.0 |             7.7 |            5.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
