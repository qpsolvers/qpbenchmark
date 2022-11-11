# Maros-Meszaros dense subset

- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-11-11 18:33:07.313923+00:00
- Run by: [@stephane-caron](https://github.com/stephane-caron/)

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
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v2.6.0rc5.

## Settings

There are 3 settings: **default**, **low_accuracy** and
**high_accuracy**. They validate solutions using the following tolerances:

| tolerance   |   default |   low_accuracy |   high_accuracy |
|:------------|----------:|---------------:|----------------:|
| ``cost``    |      1000 |       1000     |        1000     |
| ``primal``  |         1 |          0.001 |           1e-09 |
| ``runtime`` |      1000 |       1000     |        1000     |

Solvers for each group of settings are configured as follows:

| solver   | parameter                        | default   | low_accuracy          | high_accuracy          |
|:---------|:---------------------------------|:----------|:----------------------|:-----------------------|
| cvxopt   | ``feastol``                      | -         | 0.001                 | 1e-09                  |
| ecos     | ``feastol``                      | -         | 0.001                 | 1e-09                  |
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

## Metrics

We look at the following statistics:

- [Success rate](#success-rate)
- [Computation time](#computation-time)
- [Primal error](#primal-error)
- [Cost error](#cost-error)

They are presented in more detail in [Metrics](../README.md#metrics).

## Results

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |        15 |              14 |             15 |
| ecos     |         8 |               8 |              8 |
| highs    |        76 |              71 |             76 |
| osqp     |        68 |              53 |             61 |
| proxqp   |       100 |             100 |             97 |
| qpoases  |        59 |              59 |             58 |
| qpswift  |        15 |              15 |             15 |
| quadprog |        34 |              29 |             34 |
| scs      |        80 |              69 |             80 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |       100 |              98 |            100 |
| ecos     |       100 |             100 |            100 |
| highs    |       100 |              95 |            100 |
| osqp     |        75 |             100 |            100 |
| proxqp   |       100 |             100 |             97 |
| qpoases  |        97 |              95 |             95 |
| qpswift  |       100 |             100 |            100 |
| quadprog |       100 |              95 |            100 |
| scs      |        83 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |    1230.8 |          1176.9 |         1529.0 |
| ecos     |    1692.0 |          1617.9 |         2101.9 |
| highs    |      51.8 |            49.6 |           64.4 |
| osqp     |       9.3 |           190.9 |          157.6 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     119.7 |           117.3 |          145.9 |
| qpswift  |    1230.6 |          1176.6 |         1528.6 |
| quadprog |     506.0 |           483.8 |          628.5 |
| scs      |       4.7 |            74.7 |           49.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal errors over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal error of Y is Y times less precise
on constraints than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric means of solver primal errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| cvxopt   |  518090.4 |             4.1 |            4.8 |
| ecos     |  561373.7 |             4.1 |            5.1 |
| highs    |  140872.6 |             2.7 |            1.3 |
| osqp     | 5799824.2 |             2.5 |            2.5 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |  761412.8 |    3949268243.1 |        54309.7 |
| qpswift  |  518090.4 |             3.8 |            4.8 |
| quadprog |  400493.3 |             5.8 |            3.7 |
| scs      | 1820826.5 |             1.6 |            1.7 |

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
| cvxopt   |     956.3 |          1591.7 |          110.1 |
| ecos     |    1314.7 |          2188.4 |          151.4 |
| highs    |      39.1 |            65.1 |            4.5 |
| osqp     |     489.2 |           258.1 |           11.5 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     135.7 |           279.8 |           25.8 |
| qpswift  |     956.3 |          1591.7 |          110.1 |
| quadprog |     393.2 |           654.5 |           45.3 |
| scs      |      88.1 |           100.4 |            3.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
