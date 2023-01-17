# Maros-Meszaros dense subset

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-01-17 16:35:09.950590+00:00 |
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

| solver   | version               |
|:---------|:----------------------|
| cvxopt   | 1.3.0                 |
| ecos     | 2.0.10                |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.1.2.dev3            |
| osqp     | 0.6.2.post5           |
| proxqp   | 0.3.1                 |
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

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                25.8 |                                638.2 |                                    482749.9 |                                794862.9 |                                 2.5 |                             568.0 |
| ecos     |                                12.9 |                               1089.2 |                                    559250.8 |                                944595.4 |                                 2.8 |                             969.5 |
| gurobi   |                                37.1 |                                139.0 |                                    279207.1 |                              13678400.5 |                                71.5 |                             123.8 |
| highs    |                                64.5 |                                 40.0 |                                    143327.1 |                                236646.0 |                                 5.7 |                              35.4 |
| osqp     |                                51.6 |                                 14.7 |                                   3076625.0 |                               3656679.6 |                               348.3 |                             401.5 |
| proxqp   |                                95.2 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| qpoases  |                                24.2 |                                155.3 |                                   4502217.8 |                              23447138.1 |                                 1.5 |                             505.6 |
| qpswift  |                                25.8 |                                638.1 |                                    482749.9 |                                794860.4 |                                 2.5 |                             568.0 |
| quadprog |                                32.3 |                                468.2 |                                    439403.4 |                                723489.2 |                                 2.2 |                             416.8 |
| scs      |                                71.0 |                                  3.8 |                                   1879523.1 |                                371680.3 |                                47.8 |                             103.1 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                 0.0 |                                 93.9 |                                         4.7 |                                 10694.8 |                            201610.2 |                             103.9 |
| ecos     |                                 0.0 |                                160.3 |                                         5.0 |                              25207983.1 |                           1008113.0 |                             177.3 |
| gurobi   |                                11.3 |                                 20.4 |                                         6.9 |                           58417876841.3 |                       44892532683.0 |                              22.6 |
| highs    |                                 0.0 |                                  5.9 |                                         2.3 |                               2949475.8 |                        3253828307.1 |                               6.5 |
| osqp     |                                41.9 |                                 26.3 |                                         3.3 |                                     2.8 |                                 3.7 |                              29.1 |
| proxqp   |                                85.5 |                                  1.0 |                                         1.0 |                                     1.0 |                                71.9 |                               1.0 |
| qpoases  |                                19.4 |                                 25.6 |                               35961583271.8 |                          100471909143.0 |                                 1.7 |                              92.4 |
| qpswift  |                                17.7 |                                 93.9 |                                         4.4 |                                     3.8 |                             48079.4 |                             103.9 |
| quadprog |                                25.8 |                                 68.9 |                                         7.5 |                                    13.6 |                                11.5 |                              76.2 |
| scs      |                                67.7 |                                 10.9 |                                         2.2 |                                     2.0 |                                 1.0 |                              12.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                21.0 |                                627.2 |                                        13.3 |                                    73.9 |                                 2.3 |                             934.4 |
| ecos     |                                11.3 |                               1154.7 |                                        15.6 |                                    97.9 |                                 2.4 |                            1720.6 |
| gurobi   |                                37.1 |                                136.6 |                                         7.8 |                               1160403.6 |                             55063.1 |                             203.6 |
| highs    |                                54.8 |                                 39.3 |                                         4.1 |                                    81.0 |                              3991.4 |                              58.2 |
| osqp     |                                38.7 |                                105.0 |                                         8.4 |                                    52.9 |                               373.4 |                             159.1 |
| proxqp   |                                95.2 |                                  1.0 |                                         1.0 |                                     1.0 |                                26.5 |                               1.0 |
| qpoases  |                                19.4 |                                176.6 |                                     71742.6 |                               1350962.2 |                                 1.3 |                             746.9 |
| qpswift  |                                24.2 |                                627.0 |                                        13.3 |                                    74.9 |                                 7.2 |                             934.6 |
| quadprog |                                32.3 |                                460.1 |                                        12.2 |                                    67.2 |                                 1.9 |                             685.7 |
| scs      |                                79.0 |                                 35.0 |                                         5.6 |                                    29.0 |                                 1.0 |                              51.6 |

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
| proxqp   |        95 |              85 |             95 |
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
| proxqp   |        95 |              90 |             95 |
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
| cvxopt   |     638.2 |            93.9 |          627.2 |
| ecos     |    1089.2 |           160.3 |         1154.7 |
| gurobi   |     139.0 |            20.4 |          136.6 |
| highs    |      40.0 |             5.9 |           39.3 |
| osqp     |      14.7 |            26.3 |          105.0 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     155.3 |            25.6 |          176.6 |
| qpswift  |     638.1 |            93.9 |          627.0 |
| quadprog |     468.2 |            68.9 |          460.1 |
| scs      |       3.8 |            10.9 |           35.0 |

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
| cvxopt   |  482749.9 |             4.7 |           13.3 |
| ecos     |  559250.8 |             5.0 |           15.6 |
| gurobi   |  279207.1 |             6.9 |            7.8 |
| highs    |  143327.1 |             2.3 |            4.1 |
| osqp     | 3076625.0 |             3.3 |            8.4 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  | 4502217.8 |   35961583271.8 |        71742.6 |
| qpswift  |  482749.9 |             4.4 |           13.3 |
| quadprog |  439403.4 |             7.5 |           12.2 |
| scs      | 1879523.1 |             2.2 |            5.6 |

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
| cvxopt   |   794862.9 |         10694.8 |           73.9 |
| ecos     |   944595.4 |      25207983.1 |           97.9 |
| gurobi   | 13678400.5 |   58417876841.3 |      1160403.6 |
| highs    |   236646.0 |       2949475.8 |           81.0 |
| osqp     |  3656679.6 |             2.8 |           52.9 |
| proxqp   |        1.0 |             1.0 |            1.0 |
| qpoases  | 23447138.1 |  100471909143.0 |      1350962.2 |
| qpswift  |   794860.4 |             3.8 |           74.9 |
| quadprog |   723489.2 |            13.6 |           67.2 |
| scs      |   371680.3 |             2.0 |           29.0 |

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
| cvxopt   |       2.5 |        201610.2 |            2.3 |
| ecos     |       2.8 |       1008113.0 |            2.4 |
| gurobi   |      71.5 |   44892532683.0 |        55063.1 |
| highs    |       5.7 |    3253828307.1 |         3991.4 |
| osqp     |     348.3 |             3.7 |          373.4 |
| proxqp   |       1.0 |            71.9 |           26.5 |
| qpoases  |       1.5 |             1.7 |            1.3 |
| qpswift  |       2.5 |         48079.4 |            7.2 |
| quadprog |       2.2 |            11.5 |            1.9 |
| scs      |      47.8 |             1.0 |            1.0 |

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
| cvxopt   |     568.0 |           103.9 |          934.4 |
| ecos     |     969.5 |           177.3 |         1720.6 |
| gurobi   |     123.8 |            22.6 |          203.6 |
| highs    |      35.4 |             6.5 |           58.2 |
| osqp     |     401.5 |            29.1 |          159.1 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     505.6 |            92.4 |          746.9 |
| qpswift  |     568.0 |           103.9 |          934.6 |
| quadprog |     416.8 |            76.2 |          685.7 |
| scs      |     103.1 |            12.0 |           51.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
