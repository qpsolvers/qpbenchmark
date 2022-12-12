# GitHub "free-for-all" test set

- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-12-12 16:44:39.896803+00:00
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

- [GHFFA01](https://github.com/stephane-caron/qpsolvers_benchmark/issues/25) Project the origin on a 2D line that becomes vertical.
- [GHFFA02](https://github.com/stephane-caron/qpsolvers_benchmark/issues/27) Linear system with two variables and a large condition number

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
| cvxopt   |        60 |              55 |             60 |
| ecos     |        50 |              50 |             50 |
| highs    |        60 |              60 |             60 |
| osqp     |        55 |              55 |             55 |
| proxqp   |        60 |              60 |             55 |
| qpoases  |        70 |              70 |             70 |
| qpswift  |         0 |               0 |              0 |
| quadprog |         0 |               0 |              0 |
| scs      |        60 |              55 |             60 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |        80 |              75 |             80 |
| ecos     |       100 |             100 |            100 |
| highs    |        80 |              80 |             80 |
| osqp     |        95 |              95 |             95 |
| proxqp   |        90 |              90 |             85 |
| qpoases  |        70 |              70 |             70 |
| qpswift  |       100 |             100 |            100 |
| quadprog |       100 |             100 |            100 |
| scs      |        90 |              95 |             90 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |   35643.4 |         46806.2 |        46671.0 |
| ecos     |  134166.1 |        176204.1 |       175696.0 |
| highs    |   35647.1 |         46811.4 |        46676.3 |
| osqp     |   93207.9 |        122414.7 |       122061.0 |
| proxqp   |   60988.5 |         80098.2 |        79866.6 |
| qpoases  |       1.0 |             1.0 |            1.0 |
| qpswift  |  579093.4 |        760555.3 |       758357.9 |
| quadprog |  579093.4 |        760555.3 |       758357.9 |
| scs      |   60990.8 |        122417.4 |        79869.8 |

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

|          |            default |   high_accuracy |    low_accuracy |
|:---------|-------------------:|----------------:|----------------:|
| cvxopt   | -108344124091417.0 |   -5004647703.0 | -117590122552.0 |
| ecos     | -274769388039508.0 |       -281626.0 | -281467940334.0 |
| highs    | -108339023244642.0 |       -112591.0 | -112585487354.0 |
| osqp     | -218829401905928.0 |       -225179.0 | -289076873422.0 |
| proxqp   | -163288323377648.0 |       -466216.0 | -527415114875.0 |
| qpoases  |                1.0 |             1.0 |             1.0 |
| qpswift  | -562949953421316.0 |       -562951.0 | -562949953418.0 |
| quadprog | -562949953421316.0 |       -562951.0 | -562949953418.0 |
| scs      | -163288049868560.0 |       -225184.0 | -168882945522.0 |

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
| cvxopt   |       7.3 |             7.3 |            7.3 |
| ecos     |       1.2 |             1.2 |            1.2 |
| highs    |      18.0 |            18.0 |           18.0 |
| osqp     |       1.0 |             1.0 |            1.0 |
| proxqp   |       1.7 |             1.4 |            2.4 |
| qpoases  |      87.2 |            87.2 |           87.2 |
| qpswift  |      13.1 |            13.1 |           13.1 |
| quadprog |      13.1 |            13.1 |           13.1 |
| scs      |       1.4 |             1.0 |            1.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
