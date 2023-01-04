# Maros-Meszaros dense subset

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-01-04 17:49:17.657768+00:00 |
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

Subset of the Maros-Meszaros test setrestricted to smaller dense problems.

## Solvers

| solver   | version     |
|:---------|:------------|
| cvxopt   | 1.3.0       |
| ecos     | 2.0.11      |
| osqp     | 0.6.2.post0 |
| proxqp   | 0.3.0       |
| qpoases  | 3.2.0       |
| quadprog | 0.1.11      |
| scs      | 3.2.0       |

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

| solver   | parameter              | default   | high_accuracy   | low_accuracy   |
|:---------|:-----------------------|:----------|:----------------|:---------------|
| cvxopt   | ``feastol``            | -         | 1e-09           | 0.001          |
| ecos     | ``feastol``            | -         | 1e-09           | 0.001          |
| osqp     | ``eps_abs``            | -         | 1e-09           | 0.001          |
| osqp     | ``eps_rel``            | -         | 0.0             | 0.0            |
| osqp     | ``time_limit``         | 1000.0    | 1000.0          | 1000.0         |
| proxqp   | ``eps_abs``            | -         | 1e-09           | 0.001          |
| proxqp   | ``eps_rel``            | -         | 0.0             | 0.0            |
| qpoases  | ``predefined_options`` | default   | reliable        | fast           |
| qpoases  | ``time_limit``         | 1000.0    | 1000.0          | 1000.0         |
| scs      | ``eps_abs``            | -         | 1e-09           | 0.001          |
| scs      | ``eps_rel``            | -         | 0.0             | 0.0            |
| scs      | ``time_limit_secs``    | 1000.0    | 1000.0          | 1000.0         |

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                25.8 |                                169.1 |                                        23.8 |                                    23.8 |                                 6.8 |                             150.2 |
| ecos     |                                12.9 |                                288.6 |                                        27.6 |                                    28.3 |                                 7.9 |                             256.3 |
| gurobi   |                                37.1 |                                 36.8 |                                        13.8 |                                   409.5 |                               198.1 |                              32.7 |
| highs    |                                64.5 |                                 10.6 |                                         7.1 |                                     7.1 |                                15.8 |                               9.3 |
| osqp     |                                51.6 |                                  3.9 |                                       151.6 |                                   109.5 |                               965.4 |                             106.2 |
| proxqp   |                                95.2 |                                  1.2 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| qpoases  |                                24.2 |                                 41.1 |                                       221.9 |                                   701.9 |                                 4.1 |                             133.7 |
| qpswift  |                                25.8 |                                169.1 |                                        23.8 |                                    23.8 |                                 6.8 |                             150.2 |
| quadprog |                                32.3 |                                124.0 |                                        21.7 |                                    21.7 |                                 6.2 |                             110.2 |
| scs      |                                71.0 |                                  1.0 |                                        92.6 |                                    11.1 |                               132.6 |                              27.3 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                 0.0 |                                145.9 |                                         4.1 |                                  5336.1 |                            201610.2 |                             150.4 |
| ecos     |                                 0.0 |                                249.0 |                                         4.3 |                              12577419.7 |                           1008113.0 |                             256.8 |
| gurobi   |                                11.3 |                                 31.8 |                                         5.9 |                           29147359855.8 |                       44892532683.0 |                              32.8 |
| highs    |                                 0.0 |                                  9.1 |                                         2.0 |                               1471628.8 |                        3253828307.1 |                               9.4 |
| osqp     |                                41.9 |                                 40.9 |                                         2.9 |                                     1.4 |                                 3.7 |                              42.2 |
| proxqp   |                                48.4 |                                  1.0 |                                         1.0 |                                     1.1 |                             30720.0 |                               1.0 |
| qpoases  |                                19.4 |                                 36.2 |                               65018918805.4 |                           50370655844.9 |                        8885523867.2 |                             175.5 |
| qpswift  |                                17.7 |                                145.9 |                                         3.8 |                                     1.9 |                             48079.4 |                             150.4 |
| quadprog |                                25.8 |                                107.0 |                                         6.5 |                                     6.8 |                                11.5 |                             110.4 |
| scs      |                                67.7 |                                 16.9 |                                         1.9 |                                     1.0 |                                 1.0 |                              17.4 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                21.0 |                                143.3 |                                         3.8 |                                     8.8 |                                 2.3 |                              66.7 |
| ecos     |                                11.3 |                                263.9 |                                         4.4 |                                    11.6 |                                 2.4 |                             122.8 |
| gurobi   |                                37.1 |                                 31.2 |                                         2.2 |                                137836.7 |                             55063.1 |                              14.5 |
| highs    |                                54.8 |                                  9.0 |                                         1.1 |                                     9.6 |                              3991.4 |                               4.2 |
| osqp     |                                38.7 |                                 24.0 |                                         2.4 |                                     6.3 |                               373.4 |                              11.4 |
| proxqp   |                                37.1 |                                  1.0 |                                         1.0 |                                     1.0 |                              7870.3 |                               1.0 |
| qpoases  |                                19.4 |                                 40.4 |                                     20284.2 |                                160471.9 |                                 1.3 |                              53.3 |
| qpswift  |                                24.2 |                                143.3 |                                         3.8 |                                     8.9 |                                 7.2 |                              66.7 |
| quadprog |                                32.3 |                                105.1 |                                         3.4 |                                     8.0 |                                 1.9 |                              48.9 |
| scs      |                                79.0 |                                  8.0 |                                         1.6 |                                     3.4 |                                 1.0 |                               3.7 |

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
| proxqp   |        95 |              48 |             37 |
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
| proxqp   |        98 |              52 |             40 |
| qpoases  |        69 |              63 |             68 |
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
| cvxopt   |     169.1 |           145.9 |          143.3 |
| ecos     |     288.6 |           249.0 |          263.9 |
| gurobi   |      36.8 |            31.8 |           31.2 |
| highs    |      10.6 |             9.1 |            9.0 |
| osqp     |       3.9 |            40.9 |           24.0 |
| proxqp   |       1.2 |             1.0 |            1.0 |
| qpoases  |      41.1 |            36.2 |           40.4 |
| qpswift  |     169.1 |           145.9 |          143.3 |
| quadprog |     124.0 |           107.0 |          105.1 |
| scs      |       1.0 |            16.9 |            8.0 |

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
| cvxopt   |      23.8 |             4.1 |            3.8 |
| ecos     |      27.6 |             4.3 |            4.4 |
| gurobi   |      13.8 |             5.9 |            2.2 |
| highs    |       7.1 |             2.0 |            1.1 |
| osqp     |     151.6 |             2.9 |            2.4 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     221.9 |   65018918805.4 |        20284.2 |
| qpswift  |      23.8 |             3.8 |            3.8 |
| quadprog |      21.7 |             6.5 |            3.4 |
| scs      |      92.6 |             1.9 |            1.6 |

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
| cvxopt   |      23.8 |          5336.1 |            8.8 |
| ecos     |      28.3 |      12577419.7 |           11.6 |
| gurobi   |     409.5 |   29147359855.8 |       137836.7 |
| highs    |       7.1 |       1471628.8 |            9.6 |
| osqp     |     109.5 |             1.4 |            6.3 |
| proxqp   |       1.0 |             1.1 |            1.0 |
| qpoases  |     701.9 |   50370655844.9 |       160471.9 |
| qpswift  |      23.8 |             1.9 |            8.9 |
| quadprog |      21.7 |             6.8 |            8.0 |
| scs      |      11.1 |             1.0 |            3.4 |

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
| cvxopt   |       6.8 |        201610.2 |            2.3 |
| ecos     |       7.9 |       1008113.0 |            2.4 |
| gurobi   |     198.1 |   44892532683.0 |        55063.1 |
| highs    |      15.8 |    3253828307.1 |         3991.4 |
| osqp     |     965.4 |             3.7 |          373.4 |
| proxqp   |       1.0 |         30720.0 |         7870.3 |
| qpoases  |       4.1 |    8885523867.2 |            1.3 |
| qpswift  |       6.8 |         48079.4 |            7.2 |
| quadprog |       6.2 |            11.5 |            1.9 |
| scs      |     132.6 |             1.0 |            1.0 |

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
| cvxopt   |     150.2 |           150.4 |           66.7 |
| ecos     |     256.3 |           256.8 |          122.8 |
| gurobi   |      32.7 |            32.8 |           14.5 |
| highs    |       9.3 |             9.4 |            4.2 |
| osqp     |     106.2 |            42.2 |           11.4 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     133.7 |           175.5 |           53.3 |
| qpswift  |     150.2 |           150.4 |           66.7 |
| quadprog |     110.2 |           110.4 |           48.9 |
| scs      |      27.3 |            17.4 |            3.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
