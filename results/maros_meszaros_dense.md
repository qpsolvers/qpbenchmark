# Maros-Meszaros dense subset

- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-11-10 17:23:53.559879+00:00
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
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v2.6.0rc4.

## Settings

There are 2 settings: **default** and
**high_accuracy**. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |
|:------------|----------:|----------------:|
| ``cost``    |      1000 |        1000     |
| ``primal``  |         1 |           1e-09 |
| ``runtime`` |      1000 |        1000     |

Solvers for each group of settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |
|:---------|:---------------------------------|:----------|----------------:|
| cvxopt   | ``feastol``                      | -         |     1e-09       |
| ecos     | ``feastol``                      | -         |     1e-09       |
| highs    | ``dual_feasibility_tolerance``   | -         |     1e-09       |
| highs    | ``primal_feasibility_tolerance`` | -         |     1e-09       |
| highs    | ``time_limit``                   | 1000.0    |  1000           |
| osqp     | ``eps_abs``                      | -         |     1e-09       |
| osqp     | ``eps_rel``                      | -         |     0           |
| osqp     | ``time_limit``                   | 1000.0    |  1000           |
| proxqp   | ``eps_abs``                      | -         |     1e-09       |
| proxqp   | ``eps_rel``                      | -         |     0           |
| qpoases  | ``termination_tolerance``        | -         |     1e-07       |
| qpoases  | ``time_limit``                   | 1000.0    |  1000           |
| qpswift  | ``RELTOL``                       | -         |     1.73205e-09 |
| scs      | ``eps_abs``                      | -         |     1e-09       |
| scs      | ``eps_rel``                      | -         |     0           |
| scs      | ``time_limit_secs``              | 1000.0    |  1000           |

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

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |        15 |              14 |
| ecos     |         8 |               8 |
| highs    |        76 |              71 |
| osqp     |        68 |              53 |
| proxqp   |       100 |             100 |
| qpoases  |        63 |              56 |
| qpswift  |        15 |              15 |
| quadprog |        34 |              29 |
| scs      |        29 |              27 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). The second table below summarizes the frequency at
which solvers return success (1) and the corresponding solution did indeed pass
tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |       100 |              98 |
| ecos     |       100 |             100 |
| highs    |       100 |              95 |
| osqp     |        75 |             100 |
| proxqp   |       100 |             100 |
| qpoases  |        97 |              90 |
| qpswift  |       100 |             100 |
| quadprog |       100 |              95 |
| scs      |       100 |             100 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](../README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |    1230.8 |          1176.9 |
| ecos     |    1692.0 |          1617.9 |
| highs    |      51.8 |            49.6 |
| osqp     |       9.3 |           190.9 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |      99.9 |            95.6 |
| qpswift  |    1230.6 |          1176.6 |
| quadprog |     506.0 |           483.8 |
| scs      |     646.6 |           670.6 |

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

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |  518090.4 |             4.1 |
| ecos     |  561373.7 |             4.1 |
| highs    |  140872.6 |             2.7 |
| osqp     | 5799824.2 |             2.5 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |  739090.9 |    3798407616.5 |
| qpswift  |  518090.4 |             3.8 |
| quadprog |  400493.3 |             5.8 |
| scs      |  433140.2 |             3.3 |

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

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |     956.3 |          1591.7 |
| ecos     |    1314.7 |          2188.4 |
| highs    |      39.1 |            65.1 |
| osqp     |     489.2 |           258.1 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |     113.5 |           188.9 |
| qpswift  |     956.3 |          1591.7 |
| quadprog |     393.2 |           654.5 |
| scs      |     504.5 |           906.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
