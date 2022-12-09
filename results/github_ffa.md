# GitHub "free-for-all" test set

- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-12-09 15:48:29.785982+00:00
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

- [Geometric and numerical aspects of redundancy](https://github.com/stephane-caron/qpsolvers_benchmark/issues/25)

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
| cvxopt   |       100 |             100 |            100 |
| ecos     |       100 |             100 |            100 |
| highs    |        80 |              80 |             80 |
| osqp     |       100 |             100 |            100 |
| proxqp   |       100 |             100 |            100 |
| qpoases  |       100 |             100 |            100 |
| qpswift  |         0 |               0 |              0 |
| quadprog |         0 |               0 |              0 |
| scs      |       100 |             100 |            100 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |       100 |             100 |            100 |
| ecos     |       100 |             100 |            100 |
| highs    |       100 |             100 |            100 |
| osqp     |       100 |             100 |            100 |
| proxqp   |       100 |             100 |            100 |
| qpoases  |       100 |             100 |            100 |
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
| cvxopt   |       4.8 |             2.2 |            3.2 |
| ecos     |      10.4 |            11.3 |           11.8 |
| highs    |   58807.7 |         64216.8 |        76840.7 |
| osqp     |       2.5 |             2.7 |            3.1 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |       1.6 |             1.1 |            1.4 |
| qpswift  |  955415.4 |       1043347.0 |      1248411.5 |
| quadprog |  955415.4 |       1043347.0 |      1248411.5 |
| scs      |       2.7 |             3.4 |            3.7 |

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
| cvxopt   |               1.0 |             1.0 |            1.0 |
| ecos     |             301.0 |           301.0 |          301.0 |
| highs    | 108339023244645.0 |        112591.0 | 112585487356.0 |
| osqp     |    127802862917.0 |             1.0 | 127802862917.0 |
| proxqp   |       561242599.0 |        560111.0 | 562376891151.0 |
| qpoases  |               1.0 |             1.0 |            1.0 |
| qpswift  | 562949953421313.0 |        562951.0 | 562949953420.0 |
| quadprog | 562949953421313.0 |        562951.0 | 562949953420.0 |
| scs      |         7740031.0 |             1.0 |      7740031.0 |

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

|          |              default |        high_accuracy |         low_accuracy |
|:---------|---------------------:|---------------------:|---------------------:|
| cvxopt   |                  1.0 |                  1.0 |                  1.0 |
| ecos     |                301.0 |                301.0 |                301.0 |
| highs    |   8539332837687120.0 |   8539332837687120.0 |   8539332837687120.0 |
| osqp     |       127785799965.0 |                  1.0 |       127785799965.0 |
| proxqp   |          561231094.0 |             560101.0 |       562084747927.0 |
| qpoases  |                  1.0 |                  1.0 |                  1.0 |
| qpswift  | 562949953421311744.0 | 562949953421311744.0 | 562949953421311744.0 |
| quadprog | 562949953421311744.0 | 562949953421311744.0 | 562949953421311744.0 |
| scs      |            7739874.0 |                  1.0 |            7739874.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
