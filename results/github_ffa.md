# GitHub "free-for-all" test set

- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-12-13 12:05:41.771365+00:00
- Run by: [@stephane-caron](https://github.com/stephane-caron/)

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [Results](#results)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Primal error](#primal-error)
    * [Cost error](#cost-error)

## Description

Problems in this test set:

- [GHFFA01](https://github.com/stephane-caron/qpsolvers_benchmark/issues/25): Project the origin on a 2D line that becomes vertical.
- [GHFFA02](https://github.com/stephane-caron/qpsolvers_benchmark/issues/27): Linear system with two variables and a large condition number.
- [GHFFA03](https://github.com/stephane-caron/qpsolvers_benchmark/issues/29): Large unconstrained least squares.

## Solvers

| solver   | version     |
|:---------|:------------|
| cvxopt   | 1.3.0       |
| ecos     | 2.0.10      |
| highs    | 1.1.2.dev3  |
| osqp     | 0.6.2.post5 |
| proxqp   | 0.2.7       |
| qpoases  | 3.2.0       |
| qpswift  | 1.0.0       |
| quadprog | 0.1.11      |
| scs      | 3.2.2       |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v2.6.0.

## Settings

There are 3 settings: *default*, *low_accuracy* and
*high_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   low_accuracy |   high_accuracy |
|:------------|----------:|---------------:|----------------:|
| ``cost``    |      1000 |       1000     |        1000     |
| ``primal``  |         1 |          0.001 |           1e-09 |
| ``runtime`` |       100 |        100     |         100     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   |   low_accuracy |   high_accuracy |
|:---------|:---------------------------------|:----------|---------------:|----------------:|
| cvxopt   | ``feastol``                      | -         |     0.001      |     1e-09       |
| ecos     | ``feastol``                      | -         |     0.001      |     1e-09       |
| highs    | ``dual_feasibility_tolerance``   | -         |     0.001      |     1e-09       |
| highs    | ``primal_feasibility_tolerance`` | -         |     0.001      |     1e-09       |
| highs    | ``time_limit``                   | 100.0     |   100          |   100           |
| osqp     | ``eps_abs``                      | -         |     0.001      |     1e-09       |
| osqp     | ``eps_rel``                      | -         |     0          |     0           |
| osqp     | ``time_limit``                   | 100.0     |   100          |   100           |
| proxqp   | ``eps_abs``                      | -         |     0.001      |     1e-09       |
| proxqp   | ``eps_rel``                      | -         |     0          |     0           |
| qpoases  | ``time_limit``                   | 100.0     |   100          |   100           |
| qpswift  | ``RELTOL``                       | -         |     0.00173205 |     1.73205e-09 |
| scs      | ``eps_abs``                      | -         |     0.001      |     1e-09       |
| scs      | ``eps_rel``                      | -         |     0          |     0           |
| scs      | ``time_limit_secs``              | 100.0     |   100          |   100           |

## Results

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |        64 |              55 |             64 |
| ecos     |        45 |              45 |             45 |
| highs    |        82 |              82 |             82 |
| osqp     |        64 |              55 |             64 |
| proxqp   |        64 |              64 |             55 |
| qpoases  |        91 |              91 |             91 |
| qpswift  |         0 |               0 |              0 |
| quadprog |         0 |               0 |              0 |
| scs      |        64 |              55 |             64 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |        91 |              82 |             91 |
| ecos     |       100 |             100 |            100 |
| highs    |       100 |             100 |            100 |
| osqp     |       100 |             100 |            100 |
| proxqp   |       100 |             100 |             91 |
| qpoases  |        91 |              91 |             91 |
| qpswift  |       100 |             100 |            100 |
| quadprog |       100 |             100 |            100 |
| scs      |       100 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |      30.9 |            29.7 |           30.2 |
| ecos     |      90.2 |            86.7 |           88.3 |
| highs    |      18.6 |            17.8 |           18.2 |
| osqp     |      46.8 |            63.4 |           48.4 |
| proxqp   |      46.5 |            44.7 |           45.5 |
| qpoases  |       1.0 |             1.0 |            1.0 |
| qpswift  |     334.4 |           321.2 |          327.0 |
| quadprog |     334.4 |           321.2 |          327.0 |
| scs      |      46.5 |            63.4 |           45.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time
limit](#settings) when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal errors over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal error of Y is Y times less precise
on constraints than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver primal errors (1.0 is the best):

|          |           default |   high_accuracy |   low_accuracy |
|:---------|------------------:|----------------:|---------------:|
| cvxopt   |  37063635566269.2 |    1137432680.5 |  39518981023.0 |
| ecos     |  75100956805741.8 |         76800.2 |  76764158178.2 |
| highs    |  24601115559046.5 |         25589.0 |  25587587503.0 |
| osqp     |  49647297291915.2 |         63971.5 |  65699136068.8 |
| proxqp   |  49632356874694.8 |        118752.2 | 132661386369.2 |
| qpoases  |               1.0 |             1.0 |            1.0 |
| qpswift  | 140737488355329.0 |        140737.2 | 140737488355.8 |
| quadprog | 140737488355329.0 |        140737.2 | 140737488355.8 |
| scs      |  49632294335373.5 |         63972.2 |  51176519797.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal tolerance](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |      13.7 |            13.7 |           13.7 |
| ecos     |      11.0 |            11.0 |           11.0 |
| highs    |       1.3 |             1.3 |            1.3 |
| osqp     |       6.4 |             6.9 |            6.4 |
| proxqp   |       6.2 |             4.2 |           11.9 |
| qpoases  |       1.0 |             1.0 |            1.0 |
| qpswift  |      96.6 |            96.6 |           96.6 |
| quadprog |      96.6 |            96.6 |           96.6 |
| scs      |       4.2 |             6.9 |            4.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
