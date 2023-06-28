# Maros-Meszaros dense positive definite subset

| Version | 0.1.0rc4 |
|:--------|:--------------------|
| Date    | 2023-04-18 14:26:17.359951+00:00 |
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

Subset of the Maros-Meszaros test set restricted to smaller dense problems with positive definite Hessian matrix.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| cvxopt   | 1.3.0                 |
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
| clarabel |                               100.0 |                                  1.1 |                                        19.7 |                                  5116.4 |                                 1.0 |                               1.7 |
| cvxopt   |                                84.2 |                               1200.0 |                                4007270686.2 |                             180793919.3 |                              1047.8 |                            3959.5 |
| daqp     |                               100.0 |                                  1.3 |                                     10594.6 |                                     1.0 |                                13.7 |                               1.0 |
| ecos     |                                36.8 |                              15058.7 |                               14992890085.1 |                             759675905.3 |                              3944.1 |                           49723.2 |
| gurobi   |                                57.9 |                                703.2 |                                2664807625.9 |                           12895492545.7 |                            149702.7 |                            2311.1 |
| highs    |                               100.0 |                                  3.7 |                                         1.0 |                                 10715.2 |                               282.5 |                               1.7 |
| osqp     |                                78.9 |                                  1.0 |                               27630593448.6 |                            3620003925.9 |                            213166.8 |                           14618.3 |
| proxqp   |                                94.7 |                                  3.7 |                                     52843.6 |                                  1197.3 |                               889.2 |                              47.9 |
| qpoases  |                                57.9 |                               2649.1 |                               11234458286.5 |                           23021254924.4 |                              1746.3 |                           15505.1 |
| qpswift  |                                42.1 |                              15052.2 |                               14992890095.0 |                             676425667.9 |                              3918.9 |                           49736.6 |
| quadprog |                                84.2 |                               1198.6 |                                4007270686.2 |                             180793743.1 |                              1042.5 |                            3959.3 |
| scs      |                                89.5 |                                 32.9 |                               27777409922.4 |                              80699992.5 |                             50938.7 |                            6996.1 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                84.2 |                                178.2 |                                         2.8 |                                    18.3 |                                 3.4 |                            1333.5 |
| cvxopt   |                                 5.3 |                                305.8 |                                         4.2 |                                   282.3 |                           3221384.9 |                            2284.6 |
| daqp     |                                78.9 |                                 78.5 |                                      2770.9 |                                     1.1 |                           8430010.9 |                             586.3 |
| ecos     |                                 0.0 |                               3834.2 |                                        15.3 |                             171874315.7 |                           6231552.4 |                           28689.7 |
| gurobi   |                                 5.3 |                                178.5 |                                         2.8 |                          110692667522.2 |                       90789765573.8 |                            1333.5 |
| highs    |                                 0.0 |                                  1.0 |                                         1.0 |                                 93778.8 |                         173856845.8 |                               1.0 |
| osqp     |                                63.2 |                                467.6 |                                         8.3 |                                     3.2 |                                 2.6 |                            3498.3 |
| proxqp   |                                84.2 |                                 80.5 |                                         5.5 |                                     1.0 |                                 2.0 |                             586.8 |
| qpoases  |                                52.6 |                                675.1 |                                4409966163.4 |                          193905970022.2 |                                 1.1 |                            8946.3 |
| qpswift  |                                26.3 |                               3832.3 |                                        15.6 |                                     6.3 |                            297175.8 |                           28689.9 |
| quadprog |                                78.9 |                                305.2 |                                         4.2 |                                     5.6 |                                 1.0 |                            2284.5 |
| scs      |                                84.2 |                                306.6 |                                         5.9 |                                     2.5 |                                 1.4 |                            2284.5 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric
mean](../README.md#shifted-geometric-mean) (shm). Lower is better.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         6.6 |                                  5586.1 |                                 1.0 |                               1.7 |
| cvxopt   |                                73.7 |                                778.5 |                                   2781805.5 |                                147386.7 |                                 5.7 |                            2246.3 |
| daqp     |                                84.2 |                                  1.6 |                                  12661580.2 |                                     1.0 |                                12.9 |                               1.0 |
| ecos     |                                31.6 |                              21444.3 |                                  16691272.3 |                               1203006.2 |                                 4.4 |                           62628.9 |
| gurobi   |                                57.9 |                                770.2 |                                   2781805.5 |                           12648745729.9 |                            139252.1 |                            2247.2 |
| highs    |                                78.9 |                                  4.3 |                                         1.0 |                                 10715.8 |                               266.7 |                               1.7 |
| osqp     |                                57.9 |                                770.1 |                                   5471523.7 |                                444811.1 |                              2859.0 |                            2498.9 |
| proxqp   |                                89.5 |                                  3.9 |                                   3046973.5 |                                 38720.7 |                               190.7 |                               1.8 |
| qpoases  |                                52.6 |                               2910.3 |                                4417036903.5 |                           22258301788.9 |                                 1.7 |                           15076.6 |
| qpswift  |                                36.8 |                              16545.8 |                                  15300315.6 |                                730375.0 |                                44.0 |                           48380.9 |
| quadprog |                                84.2 |                               1317.5 |                                   4172719.2 |                                188269.8 |                                 1.0 |                            3849.9 |
| scs      |                                89.5 |                                801.4 |                                   5455494.8 |                                180274.7 |                                 1.8 |                            2246.2 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              84 |            100 |
| cvxopt   |        84 |               5 |             74 |
| daqp     |       100 |              79 |             84 |
| ecos     |        37 |               0 |             32 |
| gurobi   |        58 |               5 |             58 |
| highs    |       100 |               0 |             79 |
| osqp     |        79 |              63 |             58 |
| proxqp   |        95 |              84 |             89 |
| qpoases  |        58 |              53 |             53 |
| qpswift  |        42 |              26 |             37 |
| quadprog |        84 |              79 |             84 |
| scs      |        89 |              84 |             89 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution satisfies optimality conditions within
[tolerance](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              95 |            100 |
| cvxopt   |       100 |              21 |             84 |
| daqp     |       100 |              84 |             84 |
| ecos     |        95 |              58 |             95 |
| gurobi   |        68 |              16 |             68 |
| highs    |       100 |               0 |             79 |
| osqp     |        79 |              84 |             68 |
| proxqp   |        95 |              89 |             89 |
| qpoases  |        84 |              79 |             79 |
| qpswift  |       100 |              84 |             95 |
| quadprog |       100 |              95 |            100 |
| scs      |        89 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.1 |           178.2 |            1.0 |
| cvxopt   |    1200.0 |           305.8 |          778.5 |
| daqp     |       1.3 |            78.5 |            1.6 |
| ecos     |   15058.7 |          3834.2 |        21444.3 |
| gurobi   |     703.2 |           178.5 |          770.2 |
| highs    |       3.7 |             1.0 |            4.3 |
| osqp     |       1.0 |           467.6 |          770.1 |
| proxqp   |       3.7 |            80.5 |            3.9 |
| qpoases  |    2649.1 |           675.1 |         2910.3 |
| qpswift  |   15052.2 |          3832.3 |        16545.8 |
| quadprog |    1198.6 |           305.2 |         1317.5 |
| scs      |      32.9 |           306.6 |          801.4 |

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

|          |       default |   high_accuracy |   low_accuracy |
|:---------|--------------:|----------------:|---------------:|
| clarabel |          19.7 |             2.8 |            6.6 |
| cvxopt   |  4007270686.2 |             4.2 |      2781805.5 |
| daqp     |       10594.6 |          2770.9 |     12661580.2 |
| ecos     | 14992890085.1 |            15.3 |     16691272.3 |
| gurobi   |  2664807625.9 |             2.8 |      2781805.5 |
| highs    |           1.0 |             1.0 |            1.0 |
| osqp     | 27630593448.6 |             8.3 |      5471523.7 |
| proxqp   |       52843.6 |             5.5 |      3046973.5 |
| qpoases  | 11234458286.5 |    4409966163.4 |   4417036903.5 |
| qpswift  | 14992890095.0 |            15.6 |     15300315.6 |
| quadprog |  4007270686.2 |             4.2 |      4172719.2 |
| scs      | 27777409922.4 |             5.9 |      5455494.8 |

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

|          |       default |   high_accuracy |   low_accuracy |
|:---------|--------------:|----------------:|---------------:|
| clarabel |        5116.4 |            18.3 |         5586.1 |
| cvxopt   |   180793919.3 |           282.3 |       147386.7 |
| daqp     |           1.0 |             1.1 |            1.0 |
| ecos     |   759675905.3 |     171874315.7 |      1203006.2 |
| gurobi   | 12895492545.7 |  110692667522.2 |  12648745729.9 |
| highs    |       10715.2 |         93778.8 |        10715.8 |
| osqp     |  3620003925.9 |             3.2 |       444811.1 |
| proxqp   |        1197.3 |             1.0 |        38720.7 |
| qpoases  | 23021254924.4 |  193905970022.2 |  22258301788.9 |
| qpswift  |   676425667.9 |             6.3 |       730375.0 |
| quadprog |   180793743.1 |             5.6 |       188269.8 |
| scs      |    80699992.5 |             2.5 |       180274.7 |

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
| clarabel |       1.0 |             3.4 |            1.0 |
| cvxopt   |    1047.8 |       3221384.9 |            5.7 |
| daqp     |      13.7 |       8430010.9 |           12.9 |
| ecos     |    3944.1 |       6231552.4 |            4.4 |
| gurobi   |  149702.7 |   90789765573.8 |       139252.1 |
| highs    |     282.5 |     173856845.8 |          266.7 |
| osqp     |  213166.8 |             2.6 |         2859.0 |
| proxqp   |     889.2 |             2.0 |          190.7 |
| qpoases  |    1746.3 |             1.1 |            1.7 |
| qpswift  |    3918.9 |        297175.8 |           44.0 |
| quadprog |    1042.5 |             1.0 |            1.0 |
| scs      |   50938.7 |             1.4 |            1.8 |

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
| clarabel |       1.7 |          1333.5 |            1.7 |
| cvxopt   |    3959.5 |          2284.6 |         2246.3 |
| daqp     |       1.0 |           586.3 |            1.0 |
| ecos     |   49723.2 |         28689.7 |        62628.9 |
| gurobi   |    2311.1 |          1333.5 |         2247.2 |
| highs    |       1.7 |             1.0 |            1.7 |
| osqp     |   14618.3 |          3498.3 |         2498.9 |
| proxqp   |      47.9 |           586.8 |            1.8 |
| qpoases  |   15505.1 |          8946.3 |        15076.6 |
| qpswift  |   49736.6 |         28689.9 |        48380.9 |
| quadprog |    3959.3 |          2284.5 |         3849.9 |
| scs      |    6996.1 |          2284.5 |         2246.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
