# Maros-Meszaros dense subset

- CPU: Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz
- Date: 2022-11-10 10:41:40.623152+00:00
- Run by: [@stephane-caron](https://github.com/stephane-caron/)

## Solvers

| solver   | version     |
|:---------|:------------|
| cvxopt   | 1.3.0       |
| ecos     | 2.0.10      |
| highs    | 1.1.2.dev3  |
| osqp     | 0.6.2.post5 |
| proxqp   | 0.2.5       |
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
| cvxopt   |    1601.9 |          1487.6 |
| ecos     |    2202.2 |          2045.0 |
| highs    |      67.4 |            62.7 |
| osqp     |      12.1 |           241.3 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |     130.0 |           120.8 |
| qpswift  |    1601.6 |          1487.3 |
| quadprog |     658.6 |           611.5 |
| scs      |     841.6 |           847.6 |

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
| cvxopt   |  527043.5 |             4.8 |
| ecos     |  571074.8 |             4.8 |
| highs    |  143307.0 |             3.2 |
| osqp     | 5900050.7 |             2.9 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |  751863.1 |    4408882348.0 |
| qpswift  |  527043.5 |             4.4 |
| quadprog |  407414.2 |             6.7 |
| scs      |  440625.3 |             3.8 |

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
| cvxopt   |     945.1 |          1591.8 |
| ecos     |    1299.3 |          2188.5 |
| highs    |      38.7 |            65.1 |
| osqp     |     483.5 |           258.1 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |     112.1 |           188.9 |
| qpswift  |     945.1 |          1591.8 |
| quadprog |     388.6 |           654.5 |
| scs      |     498.6 |           906.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
