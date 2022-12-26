# Maros-Meszaros dense subset

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| CPU     | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| Date    | 2022-12-24 10:21:01.015929+00:00 |
| Run by  | [@stephane-caron](https://github.com/stephane-caron/) |

## Contents

* [Solvers](#solvers)
* [Settings](#settings)
* [Results by settings](#results-by-settings)
    * [Default](#default)
    * [Low accuracy](#low-accuracy)
    * [High accuracy](#high-accuracy)
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)
    * [Cost error](#cost-error)

## Solvers

| solver   | version               |
|:---------|:----------------------|
| cvxopt   | 1.3.0                 |
| ecos     | 2.0.10                |
| gurobi   | 10.0.0 (size-limited) |
| highs    | 1.1.2.dev3            |
| osqp     | 0.6.2.post5           |
| proxqp   | 0.2.7                 |
| qpoases  | 3.2.0                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.11                |
| scs      | 3.2.2                 |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers)
v2.7.1.

## Settings

There are 3 settings: *default*, *low_accuracy*
and *high_accuracy*. They validate solutions using the following
tolerances:

| tolerance   |   default |   low_accuracy |   high_accuracy |
|:------------|----------:|---------------:|----------------:|
| ``cost``    |      1000 |       1000     |        1000     |
| ``dual``    |         1 |          0.001 |           1e-09 |
| ``gap``     |         1 |          0.001 |           1e-09 |
| ``primal``  |         1 |          0.001 |           1e-09 |
| ``runtime`` |      1000 |       1000     |        1000     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   | low_accuracy          | high_accuracy          |
|:---------|:---------------------------------|:----------|:----------------------|:-----------------------|
| cvxopt   | ``feastol``                      | -         | 0.001                 | 1e-09                  |
| ecos     | ``feastol``                      | -         | 0.001                 | 1e-09                  |
| gurobi   | ``FeasibilityTol``               | -         | 0.001                 | 1e-09                  |
| gurobi   | ``OptimalityTol``                | -         | 0.001                 | 1e-09                  |
| gurobi   | ``TimeLimit``                    | 1000.0    | 1000.0                | 1000.0                 |
| highs    | ``dual_feasibility_tolerance``   | -         | 0.001                 | 1e-09                  |
| highs    | ``primal_feasibility_tolerance`` | -         | 0.001                 | 1e-09                  |
| highs    | ``time_limit``                   | 1000.0    | 1000.0                | 1000.0                 |
| osqp     | ``eps_abs``                      | -         | 0.001                 | 1e-09                  |
| osqp     | ``eps_rel``                      | -         | 0.0                   | 0.0                    |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0                | 1000.0                 |
| proxqp   | ``eps_abs``                      | -         | 0.001                 | 1e-09                  |
| proxqp   | ``eps_rel``                      | -         | 0.0                   | 0.0                    |
| qpoases  | ``predefined_options``           | default   | fast                  | reliable               |
| qpoases  | ``time_limit``                   | 1000.0    | 1000.0                | 1000.0                 |
| qpswift  | ``RELTOL``                       | -         | 0.0017320508075688772 | 1.7320508075688772e-09 |
| scs      | ``eps_abs``                      | -         | 0.001                 | 1e-09                  |
| scs      | ``eps_rel``                      | -         | 0.0                   | 0.0                    |
| scs      | ``time_limit_secs``              | 1000.0    | 1000.0                | 1000.0                 |

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                25.8 |                                951.2 |                                    465050.2 |                                822425.4 |                                 2.6 |                             584.2 |
| ecos     |                                12.9 |                               1623.3 |                                    538746.1 |                                977350.0 |                                 3.0 |                             997.2 |
| gurobi   |                                37.1 |                                207.2 |                                    268970.1 |                              14152710.0 |                                75.2 |                             127.3 |
| highs    |                                64.5 |                                 59.6 |                                    138072.1 |                                244851.9 |                                 6.0 |                              36.4 |
| osqp     |                                51.6 |                                 21.9 |                                   2963822.1 |                               3783477.9 |                               366.4 |                             413.0 |
| proxqp   |                                93.5 |                                  1.0 |                                         1.0 |                                     1.0 |                                 1.0 |                               1.0 |
| qpoases  |                                24.2 |                                231.1 |                                   4337146.3 |                              24260186.3 |                                 1.5 |                             520.0 |
| qpswift  |                                25.8 |                                951.0 |                                    465050.2 |                                822422.8 |                                 2.6 |                             584.3 |
| quadprog |                                32.3 |                                697.8 |                                    423292.9 |                                748576.7 |                                 2.3 |                             428.7 |
| scs      |                                71.0 |                                  5.6 |                                   1810611.4 |                                384568.7 |                                50.3 |                             106.1 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                21.0 |                                961.0 |                                         4.2 |                                    11.5 |                                 2.3 |                              68.6 |
| ecos     |                                11.3 |                               1769.4 |                                         4.9 |                                    15.2 |                                 2.4 |                             126.4 |
| gurobi   |                                37.1 |                                209.3 |                                         2.5 |                                180384.8 |                             55063.1 |                              15.0 |
| highs    |                                54.8 |                                 60.2 |                                         1.3 |                                    12.6 |                              3991.4 |                               4.3 |
| osqp     |                                38.7 |                                160.9 |                                         2.6 |                                     8.2 |                               373.4 |                              11.7 |
| proxqp   |                                27.4 |                                  1.0 |                                         1.0 |                                     1.0 |                             13621.9 |                               1.0 |
| qpoases  |                                19.4 |                                270.6 |                                     22559.2 |                                210007.1 |                                 1.3 |                              54.9 |
| qpswift  |                                24.2 |                                960.8 |                                         4.2 |                                    11.6 |                                 7.2 |                              68.7 |
| quadprog |                                32.3 |                                705.0 |                                         3.8 |                                    10.5 |                                 1.9 |                              50.4 |
| scs      |                                79.0 |                                 53.6 |                                         1.7 |                                     4.5 |                                 1.0 |                               3.8 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| cvxopt   |                                 0.0 |                                895.1 |                                         4.7 |                                 12899.3 |                            201610.2 |                             934.7 |
| ecos     |                                 0.0 |                               1527.6 |                                         5.0 |                              30404172.7 |                           1008113.0 |                            1595.3 |
| gurobi   |                                11.3 |                                194.9 |                                         6.8 |                           70459711327.3 |                       44892532683.0 |                             203.6 |
| highs    |                                 0.0 |                                 56.0 |                                         2.3 |                               3557459.2 |                        3253828307.1 |                              58.2 |
| osqp     |                                41.9 |                                251.1 |                                         3.3 |                                     3.4 |                                 3.7 |                             262.2 |
| proxqp   |                                45.2 |                                  1.0 |                                         1.0 |                                     1.0 |                              4400.0 |                               1.0 |
| qpoases  |                                19.4 |                                221.9 |                               74419665464.2 |                          121764094167.0 |                        8885523867.2 |                            1090.4 |
| qpswift  |                                17.7 |                                894.9 |                                         4.3 |                                     4.6 |                             48079.4 |                             934.7 |
| quadprog |                                25.8 |                                656.6 |                                         7.4 |                                    16.4 |                                11.5 |                             685.9 |
| scs      |                                67.7 |                                104.0 |                                         2.2 |                                     2.4 |                                 1.0 |                             108.0 |

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
| proxqp   |        94 |              45 |             27 |
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
| proxqp   |        94 |              45 |             27 |
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
| cvxopt   |     951.2 |           895.1 |          961.0 |
| ecos     |    1623.3 |          1527.6 |         1769.4 |
| gurobi   |     207.2 |           194.9 |          209.3 |
| highs    |      59.6 |            56.0 |           60.2 |
| osqp     |      21.9 |           251.1 |          160.9 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     231.1 |           221.9 |          270.6 |
| qpswift  |     951.0 |           894.9 |          960.8 |
| quadprog |     697.8 |           656.6 |          705.0 |
| scs      |       5.6 |           104.0 |           53.6 |

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
| cvxopt   |  465050.2 |             4.7 |            4.2 |
| ecos     |  538746.1 |             5.0 |            4.9 |
| gurobi   |  268970.1 |             6.8 |            2.5 |
| highs    |  138072.1 |             2.3 |            1.3 |
| osqp     | 2963822.1 |             3.3 |            2.6 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  | 4337146.3 |   74419665464.2 |        22559.2 |
| qpswift  |  465050.2 |             4.3 |            4.2 |
| quadprog |  423292.9 |             7.4 |            3.8 |
| scs      | 1810611.4 |             2.2 |            1.7 |

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
| cvxopt   |   822425.4 |         12899.3 |           11.5 |
| ecos     |   977350.0 |      30404172.7 |           15.2 |
| gurobi   | 14152710.0 |   70459711327.3 |       180384.8 |
| highs    |   244851.9 |       3557459.2 |           12.6 |
| osqp     |  3783477.9 |             3.4 |            8.2 |
| proxqp   |        1.0 |             1.0 |            1.0 |
| qpoases  | 24260186.3 |  121764094167.0 |       210007.1 |
| qpswift  |   822422.8 |             4.6 |           11.6 |
| quadprog |   748576.7 |            16.4 |           10.5 |
| scs      |   384568.7 |             2.4 |            4.5 |

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
| cvxopt   |       2.6 |        201610.2 |            2.3 |
| ecos     |       3.0 |       1008113.0 |            2.4 |
| gurobi   |      75.2 |   44892532683.0 |        55063.1 |
| highs    |       6.0 |    3253828307.1 |         3991.4 |
| osqp     |     366.4 |             3.7 |          373.4 |
| proxqp   |       1.0 |          4400.0 |        13621.9 |
| qpoases  |       1.5 |    8885523867.2 |            1.3 |
| qpswift  |       2.6 |         48079.4 |            7.2 |
| quadprog |       2.3 |            11.5 |            1.9 |
| scs      |      50.3 |             1.0 |            1.0 |

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
| cvxopt   |     584.2 |           934.7 |           68.6 |
| ecos     |     997.2 |          1595.3 |          126.4 |
| gurobi   |     127.3 |           203.6 |           15.0 |
| highs    |      36.4 |            58.2 |            4.3 |
| osqp     |     413.0 |           262.2 |           11.7 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     520.0 |          1090.4 |           54.9 |
| qpswift  |     584.3 |           934.7 |           68.7 |
| quadprog |     428.7 |           685.9 |           50.4 |
| scs      |     106.1 |           108.0 |            3.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
