# Maros-Meszaros dense subset

| Version | 1.0.0 |
|:--------|:--------------------|
| Date    | 2023-07-19 11:38:03.832653+00:00 |
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
| clarabel | 0.4.1                 |
| cvxopt   | 1.3.0                 |
| daqp     | 0.5.1                 |
| ecos     | 2.0.10                |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.1.2.dev3            |
| osqp     | 0.6.2.post5           |
| proxqp   | 0.4.0                 |
| qpoases  | 3.2.1                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.11                |
| scs      | 3.2.2                 |

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
| clarabel | ``tol_feas``                     | -         | 1e-09                  | 0.001                 |
| clarabel | ``tol_gap_abs``                  | -         | 1e-09                  | 0.001                 |
| clarabel | ``tol_gap_rel``                  | -         | 0.0                    | 0.0                   |
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
| proxqp   | ``check_duality_gap``            | -         | 1.0                    | 1.0                   |
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
| clarabel |                               100.0 |                                  1.0 |                                         1.0 |                                    78.4 |                                 1.0 |                               1.0 |
| cvxopt   |                                66.1 |                               1267.4 |                                 292269757.0 |                                268292.6 |                               269.1 |                              72.5 |
| daqp     |                                50.0 |                               4163.4 |                                1056090169.5 |                                491187.7 |                               351.8 |                             280.0 |
| ecos     |                                12.9 |                              27499.0 |                                 996322577.2 |                                938191.8 |                               197.6 |                            1493.3 |
| gurobi   |                                37.1 |                               3511.4 |                                 497416073.4 |                              13585671.6 |                              4964.0 |                             190.6 |
| highs    |                                64.5 |                               1008.4 |                                 255341695.6 |                                235041.8 |                               396.2 |                              54.5 |
| osqp     |                                51.6 |                                371.7 |                                5481100037.5 |                               3631889.3 |                             24185.1 |                             618.4 |
| proxqp   |                                91.9 |                                 14.1 |                                      1184.3 |                                     1.0 |                                71.8 |                               7.2 |
| qpoases  |                                24.2 |                               3916.0 |                                8020840724.2 |                              23288184.8 |                               102.2 |                             778.7 |
| qpswift  |                                25.8 |                              16109.1 |                                 860033995.1 |                                789471.9 |                               170.4 |                             875.0 |
| quadprog |                                62.9 |                               1430.6 |                                 315885538.2 |                               4734021.7 |                              2200.0 |                             192.3 |
| scs      |                                72.6 |                                 95.6 |                                2817718628.1 |                                369300.9 |                              3303.2 |                             152.5 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                77.4 |                                  1.0 |                                         1.0 |                                     4.1 |                                67.0 |                               1.0 |
| cvxopt   |                                 4.8 |                                  5.1 |                                         3.8 |                                   722.1 |                         789312687.2 |                               4.8 |
| daqp     |                                27.4 |                                 14.3 |                                     40700.2 |                                     2.4 |                           1503115.8 |                              13.4 |
| ecos     |                                 0.0 |                                 73.9 |                                         5.6 |                              22337783.9 |                            947663.3 |                              69.3 |
| gurobi   |                                11.3 |                                  9.4 |                                         7.7 |                           51766375081.0 |                       42200631866.2 |                               8.8 |
| highs    |                                 0.0 |                                  2.7 |                                         2.6 |                               2613646.3 |                        3058718284.2 |                               2.5 |
| osqp     |                                41.9 |                                 12.1 |                                         3.7 |                                     2.5 |                                 3.5 |                              11.4 |
| proxqp   |                                77.4 |                                  1.5 |                                         1.6 |                                     1.0 |                                 5.8 |                               1.4 |
| qpoases  |                                19.4 |                                 11.7 |                               40078358108.0 |                           89032104811.7 |                                 1.6 |                              36.1 |
| qpswift  |                                17.7 |                                 43.3 |                                         4.9 |                                     3.4 |                             45196.4 |                              40.6 |
| quadprog |                                33.9 |                                  3.8 |                                  27750671.2 |                           17812606993.5 |                       18834891992.5 |                               8.9 |
| scs      |                                62.9 |                                  6.6 |                                         2.8 |                                     2.1 |                                 1.0 |                               6.2 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                96.8 |                                  1.0 |                                         1.0 |                                     1.8 |                                 1.0 |                               1.0 |
| cvxopt   |                                53.2 |                               1324.8 |                                     11427.3 |                                     5.9 |                              7150.6 |                              64.5 |
| daqp     |                                33.9 |                               1971.2 |                                 485249571.5 |                                     7.1 |                             23487.1 |                             540.9 |
| ecos     |                                11.3 |                              34452.1 |                                     41139.1 |                                    23.0 |                                 7.1 |                            1593.5 |
| gurobi   |                                37.1 |                               4073.6 |                                     20569.1 |                                272080.2 |                            161860.5 |                             188.5 |
| highs    |                                54.8 |                               1171.7 |                                     10665.4 |                                    19.0 |                             11733.0 |                              53.9 |
| osqp     |                                38.7 |                               3131.9 |                                     22068.0 |                                    12.4 |                              1097.8 |                             147.3 |
| proxqp   |                                90.3 |                                128.3 |                                      3963.4 |                                     1.0 |                                78.8 |                               6.4 |
| qpoases  |                                19.4 |                               5268.7 |                                 188710021.3 |                                316760.5 |                                 3.9 |                             691.7 |
| qpswift  |                                24.2 |                              18708.0 |                                     35044.2 |                                    17.6 |                                21.3 |                             865.6 |
| quadprog |                                54.8 |                               1661.7 |                                    213259.9 |                                 93623.1 |                             72240.7 |                             190.3 |
| scs      |                                80.6 |                                929.0 |                                     14557.9 |                                     6.5 |                                 3.0 |                              43.7 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              77 |             97 |
| cvxopt   |        66 |               5 |             53 |
| daqp     |        50 |              27 |             34 |
| ecos     |        13 |               0 |             11 |
| gurobi   |        37 |              11 |             37 |
| highs    |        65 |               0 |             55 |
| osqp     |        52 |              42 |             39 |
| proxqp   |        92 |              77 |             90 |
| qpoases  |        24 |              19 |             19 |
| qpswift  |        26 |              18 |             24 |
| quadprog |        63 |              34 |             55 |
| scs      |        73 |              63 |             81 |

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
| cvxopt   |        87 |              32 |             73 |
| daqp     |        97 |              79 |             65 |
| ecos     |        35 |              23 |             35 |
| gurobi   |        37 |              11 |             37 |
| highs    |        87 |              23 |             77 |
| osqp     |        63 |              90 |             77 |
| proxqp   |        92 |              92 |             94 |
| qpoases  |        69 |              65 |             68 |
| qpswift  |       100 |              92 |             98 |
| quadprog |        81 |              52 |             73 |
| scs      |        76 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |
| cvxopt   |    1267.4 |             5.1 |         1324.8 |
| daqp     |    4163.4 |            14.3 |         1971.2 |
| ecos     |   27499.0 |            73.9 |        34452.1 |
| gurobi   |    3511.4 |             9.4 |         4073.6 |
| highs    |    1008.4 |             2.7 |         1171.7 |
| osqp     |     371.7 |            12.1 |         3131.9 |
| proxqp   |      14.1 |             1.5 |          128.3 |
| qpoases  |    3916.0 |            11.7 |         5268.7 |
| qpswift  |   16109.1 |            43.3 |        18708.0 |
| quadprog |    1430.6 |             3.8 |         1661.7 |
| scs      |      95.6 |             6.6 |          929.0 |

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
| cvxopt   |  292269757.0 |             3.8 |        11427.3 |
| daqp     | 1056090169.5 |         40700.2 |    485249571.5 |
| ecos     |  996322577.2 |             5.6 |        41139.1 |
| gurobi   |  497416073.4 |             7.7 |        20569.1 |
| highs    |  255341695.6 |             2.6 |        10665.4 |
| osqp     | 5481100037.5 |             3.7 |        22068.0 |
| proxqp   |       1184.3 |             1.6 |         3963.4 |
| qpoases  | 8020840724.2 |   40078358108.0 |    188710021.3 |
| qpswift  |  860033995.1 |             4.9 |        35044.2 |
| quadprog |  315885538.2 |      27750671.2 |       213259.9 |
| scs      | 2817718628.1 |             2.8 |        14557.9 |

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
| clarabel |       78.4 |             4.1 |            1.8 |
| cvxopt   |   268292.6 |           722.1 |            5.9 |
| daqp     |   491187.7 |             2.4 |            7.1 |
| ecos     |   938191.8 |      22337783.9 |           23.0 |
| gurobi   | 13585671.6 |   51766375081.0 |       272080.2 |
| highs    |   235041.8 |       2613646.3 |           19.0 |
| osqp     |  3631889.3 |             2.5 |           12.4 |
| proxqp   |        1.0 |             1.0 |            1.0 |
| qpoases  | 23288184.8 |   89032104811.7 |       316760.5 |
| qpswift  |   789471.9 |             3.4 |           17.6 |
| quadprog |  4734021.7 |   17812606993.5 |        93623.1 |
| scs      |   369300.9 |             2.1 |            6.5 |

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
| clarabel |       1.0 |            67.0 |            1.0 |
| cvxopt   |     269.1 |     789312687.2 |         7150.6 |
| daqp     |     351.8 |       1503115.8 |        23487.1 |
| ecos     |     197.6 |        947663.3 |            7.1 |
| gurobi   |    4964.0 |   42200631866.2 |       161860.5 |
| highs    |     396.2 |    3058718284.2 |        11733.0 |
| osqp     |   24185.1 |             3.5 |         1097.8 |
| proxqp   |      71.8 |             5.8 |           78.8 |
| qpoases  |     102.2 |             1.6 |            3.9 |
| qpswift  |     170.4 |         45196.4 |           21.3 |
| quadprog |    2200.0 |   18834891992.5 |        72240.7 |
| scs      |    3303.2 |             1.0 |            3.0 |

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
| cvxopt   |      72.5 |             4.8 |           64.5 |
| daqp     |     280.0 |            13.4 |          540.9 |
| ecos     |    1493.3 |            69.3 |         1593.5 |
| gurobi   |     190.6 |             8.8 |          188.5 |
| highs    |      54.5 |             2.5 |           53.9 |
| osqp     |     618.4 |            11.4 |          147.3 |
| proxqp   |       7.2 |             1.4 |            6.4 |
| qpoases  |     778.7 |            36.1 |          691.7 |
| qpswift  |     875.0 |            40.6 |          865.6 |
| quadprog |     192.3 |             8.9 |          190.3 |
| scs      |     152.5 |             6.2 |           43.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
