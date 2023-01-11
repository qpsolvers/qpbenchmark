# Maros-Meszaros dense subset

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-01-11 10:06:46.423970+00:00 |
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
| ecos     | 2.0.11                |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.5.0.dev0            |
| osqp     | 0.6.2.post0           |
| proxqp   | 0.3.1                 |
| qpoases  | 3.2.0                 |
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

| solver   | parameter                        | default   | high_accuracy   | low_accuracy   |
|:---------|:---------------------------------|:----------|:----------------|:---------------|
| cvxopt   | ``feastol``                      | -         | 1e-09           | 0.001          |
| ecos     | ``feastol``                      | -         | 1e-09           | 0.001          |
| gurobi   | ``FeasibilityTol``               | -         | 1e-09           | 0.001          |
| gurobi   | ``OptimalityTol``                | -         | 1e-09           | 0.001          |
| gurobi   | ``TimeLimit``                    | 1000.0    | 1000.0          | 1000.0         |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09           | 0.001          |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09           | 0.001          |
| highs    | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         |
| osqp     | ``eps_abs``                      | -         | 1e-09           | 0.001          |
| osqp     | ``eps_rel``                      | -         | 0.0             | 0.0            |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         |
| proxqp   | ``eps_abs``                      | -         | 1e-09           | 0.001          |
| proxqp   | ``eps_rel``                      | -         | 0.0             | 0.0            |
| qpoases  | ``predefined_options``           | default   | reliable        | fast           |
| qpoases  | ``time_limit``                   | 1000.0    | 1000.0          | 1000.0         |
| scs      | ``eps_abs``                      | -         | 1e-09           | 0.001          |
| scs      | ``eps_rel``                      | -         | 0.0             | 0.0            |
| scs      | ``time_limit_secs``              | 1000.0    | 1000.0          | 1000.0         |

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                25.8 |                                773.5 |                                    436461.0 |                                900605.1 |                                 3.3 |                             570.5 |
| ecos     |                                12.9 |                               1320.0 |                                    505626.4 |                               1070256.9 |                                 3.8 |                             973.8 |
| gurobi   |                                37.1 |                                168.5 |                                    252435.0 |                              15498065.5 |                                95.4 |                             124.3 |
| highs    |                                64.5 |                                 48.5 |                                    129584.0 |                                268127.5 |                                 7.6 |                              35.5 |
| osqp     |                                51.6 |                                 17.8 |                                   2781619.7 |                               4143135.0 |                               464.9 |                             403.3 |
| proxqp   |                                96.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| qpoases  |                                24.2 |                                187.9 |                                   4070518.0 |                              26566357.8 |                                 2.0 |                             507.8 |
| qpswift  |                                25.8 |                                773.3 |                                    436461.0 |                                900602.3 |                                 3.3 |                             570.6 |
| quadprog |                                32.3 |                                567.4 |                                    397270.7 |                                819736.4 |                                 3.0 |                             418.7 |
| scs      |                                71.0 |                                  4.6 |                                   1699303.1 |                                421125.7 |                                63.9 |                             103.6 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                 0.0 |                                751.3 |                                         4.6 |                                  5401.9 |                            201610.2 |                             934.7 |
| ecos     |                                 0.0 |                               1282.1 |                                         4.9 |                              12732498.8 |                           1008113.0 |                            1595.4 |
| gurobi   |                                11.3 |                                163.6 |                                         6.7 |                           29506745597.9 |                       44892532683.0 |                             203.6 |
| highs    |                                 0.0 |                                 47.1 |                                         2.3 |                               1489774.0 |                        3253828307.1 |                              58.2 |
| osqp     |                                41.9 |                                210.7 |                                         3.3 |                                     1.4 |                                 3.7 |                             262.2 |
| proxqp   |                                41.9 |                                  1.0 |                                         1.0 |                                     1.0 |                             26634.4 |                               1.0 |
| qpoases  |                                19.4 |                                186.3 |                               73519160990.9 |                           50991723949.2 |                        8885523867.2 |                            1090.4 |
| qpswift  |                                17.7 |                                751.1 |                                         4.3 |                                     1.9 |                             48079.4 |                             934.7 |
| quadprog |                                25.8 |                                551.1 |                                         7.3 |                                     6.9 |                                11.5 |                             685.9 |
| scs      |                                67.7 |                                 87.3 |                                         2.1 |                                     1.0 |                                 1.0 |                             108.0 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                21.0 |                                810.0 |                                         3.7 |                                    10.8 |                                 2.3 |                              67.7 |
| ecos     |                                11.3 |                               1491.4 |                                         4.3 |                                    14.3 |                                 2.4 |                             124.6 |
| gurobi   |                                37.1 |                                176.4 |                                         2.2 |                                169867.0 |                             55063.1 |                              14.7 |
| highs    |                                54.8 |                                 50.8 |                                         1.1 |                                    11.9 |                              3991.4 |                               4.2 |
| osqp     |                                38.7 |                                135.6 |                                         2.3 |                                     7.7 |                               373.4 |                              11.5 |
| proxqp   |                                29.0 |                                  1.0 |                                         1.0 |                                     1.0 |                             13921.9 |                               1.0 |
| qpoases  |                                19.4 |                                228.1 |                                     19764.2 |                                197762.2 |                                 1.3 |                              54.1 |
| qpswift  |                                24.2 |                                809.8 |                                         3.7 |                                    11.0 |                                 7.2 |                              67.7 |
| quadprog |                                32.3 |                                594.2 |                                         3.4 |                                     9.8 |                                 1.9 |                              49.7 |
| scs      |                                79.0 |                                 45.2 |                                         1.5 |                                     4.2 |                                 1.0 |                               3.7 |

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
| proxqp   |        97 |              42 |             29 |
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
| proxqp   |        97 |              42 |             29 |
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
| cvxopt   |     773.5 |           751.3 |          810.0 |
| ecos     |    1320.0 |          1282.1 |         1491.4 |
| gurobi   |     168.5 |           163.6 |          176.4 |
| highs    |      48.5 |            47.1 |           50.8 |
| osqp     |      17.8 |           210.7 |          135.6 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     187.9 |           186.3 |          228.1 |
| qpswift  |     773.3 |           751.1 |          809.8 |
| quadprog |     567.4 |           551.1 |          594.2 |
| scs      |       4.6 |            87.3 |           45.2 |

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
| cvxopt   |  436461.0 |             4.6 |            3.7 |
| ecos     |  505626.4 |             4.9 |            4.3 |
| gurobi   |  252435.0 |             6.7 |            2.2 |
| highs    |  129584.0 |             2.3 |            1.1 |
| osqp     | 2781619.7 |             3.3 |            2.3 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  | 4070518.0 |   73519160990.9 |        19764.2 |
| qpswift  |  436461.0 |             4.3 |            3.7 |
| quadprog |  397270.7 |             7.3 |            3.4 |
| scs      | 1699303.1 |             2.1 |            1.5 |

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
| cvxopt   |   900605.1 |          5401.9 |           10.8 |
| ecos     |  1070256.9 |      12732498.8 |           14.3 |
| gurobi   | 15498065.5 |   29506745597.9 |       169867.0 |
| highs    |   268127.5 |       1489774.0 |           11.9 |
| osqp     |  4143135.0 |             1.4 |            7.7 |
| proxqp   |        1.0 |             1.0 |            1.0 |
| qpoases  | 26566357.8 |   50991723949.2 |       197762.2 |
| qpswift  |   900602.3 |             1.9 |           11.0 |
| quadprog |   819736.4 |             6.9 |            9.8 |
| scs      |   421125.7 |             1.0 |            4.2 |

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
| proxqp   |       1.0 |         26634.4 |        13921.9 |
| qpoases  |       2.0 |    8885523867.2 |            1.3 |
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
| cvxopt   |     570.5 |           934.7 |           67.7 |
| ecos     |     973.8 |          1595.4 |          124.6 |
| gurobi   |     124.3 |           203.6 |           14.7 |
| highs    |      35.5 |            58.2 |            4.2 |
| osqp     |     403.3 |           262.2 |           11.5 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     507.8 |          1090.4 |           54.1 |
| qpswift  |     570.6 |           934.7 |           67.7 |
| quadprog |     418.7 |           685.9 |           49.7 |
| scs      |     103.6 |           108.0 |            3.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
