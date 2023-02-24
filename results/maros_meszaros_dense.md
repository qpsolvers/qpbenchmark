# Maros-Meszaros dense subset

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-01-26 14:37:47.901309+00:00 |
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

Subset of the Maros-Meszaros test setrestricted to smaller dense problems.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| cvxopt   | 1.3.0                 |
| ecos     | 2.0.10                |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.1.2.dev3            |
| osqp     | 0.6.2.post5           |
| proxqp   | 0.3.2                 |
| qpoases  | 3.2.1                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.11                |
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

| solver   | parameter                        | default   | high_accuracy          | low_accuracy          |
|:---------|:---------------------------------|:----------|:-----------------------|:----------------------|
| cvxopt   | ``feastol``                      | -         | 1e-09                  | 0.001                 |
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

## Know limitations

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
| cvxopt   |                                25.8 |                                761.3 |                                    436461.0 |                                900605.1 |                                 3.3 |                             570.5 |
| ecos     |                                12.9 |                               1299.2 |                                    505626.4 |                               1070256.9 |                                 3.8 |                             973.8 |
| gurobi   |                                37.1 |                                165.8 |                                    252435.0 |                              15498065.5 |                                95.4 |                             124.3 |
| highs    |                                64.5 |                                 47.7 |                                    129584.0 |                                268127.5 |                                 7.6 |                              35.5 |
| osqp     |                                51.6 |                                 17.6 |                                   2781619.7 |                               4143135.0 |                               464.9 |                             403.3 |
| proxqp   |                                96.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| qpoases  |                                24.2 |                                185.2 |                                   4070518.0 |                              26566357.8 |                                 2.0 |                             507.8 |
| qpswift  |                                25.8 |                                761.1 |                                    436461.0 |                                900602.3 |                                 3.3 |                             570.6 |
| quadprog |                                32.3 |                                558.5 |                                    397270.7 |                                819736.4 |                                 3.0 |                             418.7 |
| scs      |                                71.0 |                                  4.5 |                                   1699303.1 |                                421125.7 |                                63.9 |                             103.6 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                 0.0 |                                 96.8 |                                         5.4 |                                 10732.9 |                            201610.2 |                             103.9 |
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
| cvxopt   |                                21.0 |                                751.0 |                                        16.3 |                                    73.9 |                                 2.3 |                             934.5 |
| ecos     |                                11.3 |                               1382.6 |                                        19.1 |                                    98.0 |                                 2.4 |                            1720.7 |
| gurobi   |                                37.1 |                                163.5 |                                         9.6 |                               1161012.7 |                             55063.1 |                             203.6 |
| highs    |                                54.8 |                                 47.1 |                                         5.0 |                                    81.0 |                              3991.4 |                              58.2 |
| osqp     |                                38.7 |                                125.7 |                                        10.3 |                                    52.9 |                               373.4 |                             159.1 |
| proxqp   |                                95.2 |                                  1.0 |                                         1.0 |                                     1.0 |                                25.2 |                               1.0 |
| qpoases  |                                19.4 |                                211.5 |                                     87750.6 |                               1351671.4 |                                 1.3 |                             746.9 |
| qpswift  |                                24.2 |                                750.8 |                                        16.3 |                                    75.0 |                                 7.2 |                             934.7 |
| quadprog |                                32.3 |                                550.9 |                                        14.9 |                                    67.3 |                                 1.9 |                             685.7 |
| scs      |                                79.0 |                                 41.9 |                                         6.8 |                                    29.0 |                                 1.0 |                              51.6 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |        26 |               0 |             21 |
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
| cvxopt   |       100 |              74 |             95 |
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
| cvxopt   |     761.3 |            96.8 |          751.0 |
| ecos     |    1299.2 |           165.2 |         1382.6 |
| gurobi   |     165.8 |            21.1 |          163.5 |
| highs    |      47.7 |             6.1 |           47.1 |
| osqp     |      17.6 |            27.1 |          125.7 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     185.2 |            26.4 |          211.5 |
| qpswift  |     761.1 |            96.8 |          750.8 |
| quadprog |     558.5 |            71.0 |          550.9 |
| scs      |       4.5 |            11.2 |           41.9 |

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
| cvxopt   |  436461.0 |             5.4 |           16.3 |
| ecos     |  505626.4 |             5.7 |           19.1 |
| gurobi   |  252435.0 |             7.8 |            9.6 |
| highs    |  129584.0 |             2.6 |            5.0 |
| osqp     | 2781619.7 |             3.8 |           10.3 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  | 4070518.0 |   40961623773.0 |        87750.6 |
| qpswift  |  436461.0 |             5.0 |           16.3 |
| quadprog |  397270.7 |             8.5 |           14.9 |
| scs      | 1699303.1 |             2.5 |            6.8 |

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
| cvxopt   |   900605.1 |         10732.9 |           73.9 |
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
| cvxopt   |       3.3 |        201610.2 |            2.3 |
| ecos     |       3.8 |       1008113.0 |            2.4 |
| gurobi   |      95.4 |   44892532683.0 |        55063.1 |
| highs    |       7.6 |    3253828307.1 |         3991.4 |
| osqp     |     464.9 |             3.7 |          373.4 |
| proxqp   |       1.0 |             2.2 |           25.2 |
| qpoases  |       2.0 |             1.7 |            1.3 |
| qpswift  |       3.3 |         48079.4 |            7.2 |
| quadprog |       3.0 |            11.5 |            1.9 |
| scs      |      63.9 |             1.0 |            1.0 |

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
| cvxopt   |     570.5 |           103.9 |          934.5 |
| ecos     |     973.8 |           177.3 |         1720.7 |
| gurobi   |     124.3 |            22.6 |          203.6 |
| highs    |      35.5 |             6.5 |           58.2 |
| osqp     |     403.3 |            29.1 |          159.1 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     507.8 |            92.4 |          746.9 |
| qpswift  |     570.6 |           103.9 |          934.7 |
| quadprog |     418.7 |            76.2 |          685.7 |
| scs      |     103.6 |            12.0 |           51.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
