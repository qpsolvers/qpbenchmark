# Maros-Meszaros dense subset

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-04-18 14:46:02.417227+00:00 |
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

Subset of the Maros-Meszaros test set restricted to smaller dense problems.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| cvxopt   | 1.3.0                 |
| daqp     | 0.5.1                 |
| ecos     | 2.0.11                |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.5.0.dev0            |
| osqp     | 0.6.2.post0           |
| proxqp   | 0.3.6                 |
| qpoases  | 3.2.1                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.11                |
| scs      | 3.2.3                 |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers)
v3.3.1.

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

| solver   | parameter                        | default   | high_accuracy          | low_accuracy          |
|:---------|:---------------------------------|:----------|:-----------------------|:----------------------|
| cvxopt   | ``feastol``                      | -         | 1e-09                  | 0.001                 |
| daqp     | ``dual_tol``                     | -         | 1e-09                  | 0.001                 |
| daqp     | ``primal_tol``                   | -         | 1e-09                  | 0.001                 |
| ecos     | ``feastol``                      | -         | 1e-09                  | 0.001                 |
| gurobi   | ``FeasibilityTol``               | -         | 1e-09                  | 0.001                 |
| gurobi   | ``OptimalityTol``                | -         | 1e-09                  | 0.001                 |
| gurobi   | ``TimeLimit``                    | 1000.0    | 1000.0                 | 1000.0                |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09                  | 0.001                 |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09                  | 0.001                 |
| highs    | ``time_limit``                   | 1000.0    | 1000.0                 | 1000.0                |
| osqp     | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| osqp     | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0                 | 1000.0                |
| proxqp   | ``check_duality_gap``            | -         | True                   | True                  |
| proxqp   | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| proxqp   | ``eps_duality_gap_abs``          | -         | 1e-09                  | 0.001                 |
| proxqp   | ``eps_duality_gap_rel``          | -         | 0.0                    | 0.0                   |
| proxqp   | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| qpoases  | ``predefined_options``           | default   | reliable               | fast                  |
| qpoases  | ``time_limit``                   | 1000.0    | 1000.0                 | 1000.0                |
| qpswift  | ``RELTOL``                       | -         | 1.7320508075688772e-09 | 0.0017320508075688772 |
| scs      | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| scs      | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| scs      | ``time_limit_secs``              | 1000.0    | 1000.0                 | 1000.0                |

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
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                    89.4 |                                 1.0 |                               1.0 |
| cvxopt   |                                25.8 |                              21078.1 |                                 860033995.0 |                                900605.1 |                               170.2 |                             874.9 |
| daqp     |                                30.6 |                              16717.7 |                                 802072216.3 |                                839906.3 |                               158.9 |                             693.9 |
| ecos     |                                12.9 |                              35971.5 |                                 996322577.2 |                               1070256.9 |                               197.6 |                            1493.3 |
| gurobi   |                                37.1 |                               4591.7 |                                 497416073.4 |                              15498065.5 |                              4964.0 |                             190.6 |
| highs    |                                64.5 |                               1320.4 |                                 255341695.6 |                                268127.5 |                               396.2 |                              54.5 |
| osqp     |                                51.6 |                                486.4 |                                5481102900.3 |                               4143135.0 |                             24185.1 |                             618.4 |
| proxqp   |                                96.8 |                                 27.7 |                                      1970.5 |                                     1.0 |                                52.0 |                               1.5 |
| qpoases  |                                24.2 |                               5127.5 |                                8020840724.2 |                              26566357.8 |                               102.2 |                             778.7 |
| qpswift  |                                25.8 |                              21072.9 |                                 860033995.1 |                                900602.3 |                               170.4 |                             875.0 |
| quadprog |                                32.3 |                              15462.6 |                                 782810744.5 |                                819736.4 |                               154.9 |                             642.0 |
| scs      |                                71.0 |                                124.6 |                                3348428752.8 |                                421125.7 |                              3322.4 |                             158.9 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                77.4 |                                  2.2 |                                         1.0 |                                     4.6 |                                71.3 |                               2.6 |
| cvxopt   |                                 0.0 |                                 96.8 |                                         5.4 |                                 10732.9 |                            201610.2 |                             103.9 |
| daqp     |                                24.2 |                                 82.9 |                                       219.5 |                                     3.6 |                           1363730.7 |                              89.0 |
| ecos     |                                 0.0 |                                165.2 |                                         5.7 |                              25297807.9 |                           1008113.0 |                             177.3 |
| gurobi   |                                11.3 |                                 21.1 |                                         7.8 |                           58626040031.3 |                       44892532683.0 |                              22.6 |
| highs    |                                 0.0 |                                  6.1 |                                         2.6 |                               2959985.8 |                        3253828307.1 |                               6.5 |
| osqp     |                                41.9 |                                 27.1 |                                         3.8 |                                     2.8 |                                 3.7 |                              29.1 |
| proxqp   |                                82.3 |                                  1.0 |                                         1.0 |                                     1.0 |                                 2.2 |                               1.0 |
| qpoases  |                                19.4 |                                 26.4 |                               40961623773.0 |                          100829925460.1 |                                 1.7 |                              92.4 |
| qpswift  |                                17.7 |                                 96.8 |                                         5.0 |                                     3.8 |                             48079.4 |                             103.9 |
| quadprog |                                25.8 |                                 71.0 |                                         8.5 |                                    13.7 |                                11.5 |                              76.2 |
| scs      |                                67.7 |                                 11.2 |                                         2.5 |                                     2.0 |                                 1.0 |                              12.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                96.8 |                                  1.0 |                                         1.0 |                                     7.9 |                                 1.0 |                               1.1 |
| cvxopt   |                                21.0 |                              18384.2 |                                     35044.2 |                                    73.9 |                                 6.7 |                             934.5 |
| daqp     |                                25.8 |                              14582.2 |                                     39693.8 |                                    68.9 |                                10.5 |                             741.2 |
| ecos     |                                11.3 |                              33847.6 |                                     41139.1 |                                    98.0 |                                 7.1 |                            1720.7 |
| gurobi   |                                37.1 |                               4003.6 |                                     20569.1 |                               1161012.7 |                            161860.5 |                             203.6 |
| highs    |                                54.8 |                               1152.4 |                                     10665.4 |                                    81.0 |                             11733.0 |                              58.2 |
| osqp     |                                38.7 |                               3077.4 |                                     22068.0 |                                    52.9 |                              1097.8 |                             159.1 |
| proxqp   |                                95.2 |                                 24.5 |                                      2150.5 |                                     1.0 |                                74.0 |                               1.0 |
| qpoases  |                                19.4 |                               5176.6 |                                 188710021.3 |                               1351671.4 |                                 3.9 |                             746.9 |
| qpswift  |                                24.2 |                              18379.6 |                                     35044.2 |                                    75.0 |                                21.3 |                             934.7 |
| quadprog |                                32.3 |                              13486.9 |                                     31996.8 |                                    67.3 |                                 5.5 |                             685.7 |
| scs      |                                79.0 |                               1025.6 |                                     14602.3 |                                    29.0 |                                 2.9 |                              51.6 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              77 |             97 |
| cvxopt   |        26 |               0 |             21 |
| daqp     |        31 |              24 |             26 |
| ecos     |        13 |               0 |             11 |
| gurobi   |        37 |              11 |             37 |
| highs    |        65 |               0 |             55 |
| osqp     |        52 |              42 |             39 |
| proxqp   |        97 |              82 |             95 |
| qpoases  |        24 |              19 |             19 |
| qpswift  |        26 |              18 |             24 |
| quadprog |        32 |              26 |             32 |
| scs      |        71 |              68 |             79 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution satisfies optimality conditions within
[tolerance](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              89 |             97 |
| cvxopt   |       100 |              74 |             95 |
| daqp     |       100 |              95 |             95 |
| ecos     |        98 |              85 |             98 |
| gurobi   |        81 |              55 |             81 |
| highs    |        87 |              23 |             77 |
| osqp     |        63 |              90 |             77 |
| proxqp   |        97 |              87 |             95 |
| qpoases  |        69 |              65 |             68 |
| qpswift  |       100 |              92 |             98 |
| quadprog |       100 |              94 |            100 |
| scs      |        74 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             2.2 |            1.0 |
| cvxopt   |   21078.1 |            96.8 |        18384.2 |
| daqp     |   16717.7 |            82.9 |        14582.2 |
| ecos     |   35971.5 |           165.2 |        33847.6 |
| gurobi   |    4591.7 |            21.1 |         4003.6 |
| highs    |    1320.4 |             6.1 |         1152.4 |
| osqp     |     486.4 |            27.1 |         3077.4 |
| proxqp   |      27.7 |             1.0 |           24.5 |
| qpoases  |    5127.5 |            26.4 |         5176.6 |
| qpswift  |   21072.9 |            96.8 |        18379.6 |
| quadprog |   15462.6 |            71.0 |        13486.9 |
| scs      |     124.6 |            11.2 |         1025.6 |

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

|          |      default |   high_accuracy |   low_accuracy |
|:---------|-------------:|----------------:|---------------:|
| clarabel |          1.0 |             1.0 |            1.0 |
| cvxopt   |  860033995.0 |             5.4 |        35044.2 |
| daqp     |  802072216.3 |           219.5 |        39693.8 |
| ecos     |  996322577.2 |             5.7 |        41139.1 |
| gurobi   |  497416073.4 |             7.8 |        20569.1 |
| highs    |  255341695.6 |             2.6 |        10665.4 |
| osqp     | 5481102900.3 |             3.8 |        22068.0 |
| proxqp   |       1970.5 |             1.0 |         2150.5 |
| qpoases  | 8020840724.2 |   40961623773.0 |    188710021.3 |
| qpswift  |  860033995.1 |             5.0 |        35044.2 |
| quadprog |  782810744.5 |             8.5 |        31996.8 |
| scs      | 3348428752.8 |             2.5 |        14602.3 |

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

|          |    default |   high_accuracy |   low_accuracy |
|:---------|-----------:|----------------:|---------------:|
| clarabel |       89.4 |             4.6 |            7.9 |
| cvxopt   |   900605.1 |         10732.9 |           73.9 |
| daqp     |   839906.3 |             3.6 |           68.9 |
| ecos     |  1070256.9 |      25297807.9 |           98.0 |
| gurobi   | 15498065.5 |   58626040031.3 |      1161012.7 |
| highs    |   268127.5 |       2959985.8 |           81.0 |
| osqp     |  4143135.0 |             2.8 |           52.9 |
| proxqp   |        1.0 |             1.0 |            1.0 |
| qpoases  | 26566357.8 |  100829925460.1 |      1351671.4 |
| qpswift  |   900602.3 |             3.8 |           75.0 |
| quadprog |   819736.4 |            13.7 |           67.3 |
| scs      |   421125.7 |             2.0 |           29.0 |

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
| clarabel |       1.0 |            71.3 |            1.0 |
| cvxopt   |     170.2 |        201610.2 |            6.7 |
| daqp     |     158.9 |       1363730.7 |           10.5 |
| ecos     |     197.6 |       1008113.0 |            7.1 |
| gurobi   |    4964.0 |   44892532683.0 |       161860.5 |
| highs    |     396.2 |    3253828307.1 |        11733.0 |
| osqp     |   24185.1 |             3.7 |         1097.8 |
| proxqp   |      52.0 |             2.2 |           74.0 |
| qpoases  |     102.2 |             1.7 |            3.9 |
| qpswift  |     170.4 |         48079.4 |           21.3 |
| quadprog |     154.9 |            11.5 |            5.5 |
| scs      |    3322.4 |             1.0 |            2.9 |

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
| clarabel |       1.0 |             2.6 |            1.1 |
| cvxopt   |     874.9 |           103.9 |          934.5 |
| daqp     |     693.9 |            89.0 |          741.2 |
| ecos     |    1493.3 |           177.3 |         1720.7 |
| gurobi   |     190.6 |            22.6 |          203.6 |
| highs    |      54.5 |             6.5 |           58.2 |
| osqp     |     618.4 |            29.1 |          159.1 |
| proxqp   |       1.5 |             1.0 |            1.0 |
| qpoases  |     778.7 |            92.4 |          746.9 |
| qpswift  |     875.0 |           103.9 |          934.7 |
| quadprog |     642.0 |            76.2 |          685.7 |
| scs      |     158.9 |            12.0 |           51.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
