# Maros-Meszaros dense subset

- Author: [@stephane-caron](https://github.com/stephane-caron/)
- CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
- Date: 2022-11-08 18:28:12.417047+00:00

## Solvers

| package   | version     |
|:----------|:------------|
| cvxopt    | 1.3.0       |
| ecos      | 2.0.10      |
| osqp      | 0.6.2.post5 |
| proxqp    | 0.2.5       |
| scs       | 3.2.2       |

All solvers were called via
[qpsolvers](https://github.com/stephane-caron/qpsolvers) v2.5.0.

## Settings

- Cost tolerance: 1000.0
- Primal tolerance: 1.0
- Time limit: 1000.0 seconds

| solver   | parameter           | default   |   high_accuracy |
|:---------|:--------------------|:----------|----------------:|
| cvxopt   | ``feastol``         | -         |           1e-09 |
| ecos     | ``feastol``         | -         |           1e-09 |
| osqp     | ``eps_abs``         | -         |           1e-09 |
| osqp     | ``eps_rel``         | -         |           0     |
| osqp     | ``time_limit``      | 1000.0    |        1000     |
| proxqp   | ``eps_abs``         | -         |           1e-09 |
| proxqp   | ``eps_rel``         | -         |           0     |
| scs      | ``eps_abs``         | -         |           1e-09 |
| scs      | ``eps_rel``         | -         |           0     |
| scs      | ``time_limit_secs`` | 1000.0    |        1000     |

## Metrics

We look at the following statistics:

- [Success rate](#success-rate)
- [Computation time](#computation-time)
- [Primal error](#primal-error)
- [Cost error](#cost-error)

They are presented in more detail in [Metrics](README.md#metrics).

## Results

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |        15 |              15 |
| ecos     |         8 |               8 |
| highs    |        76 |              76 |
| osqp     |        68 |              53 |
| proxqp   |       100 |             100 |
| qpoases  |        75 |              75 |
| qpswift  |        15 |              15 |
| quadprog |        34 |              34 |
| scs      |        29 |              29 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider
that a solver successfully solved a problem when (1) it returned with a success
status and (2) its solution is within cost and primal error
[tolerances](#settings). Here is a summary of the frequency at which solvers
returned success (1) but the corresponding solution did not pass tolerance
checks:

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |       100 |             100 |
| ecos     |       100 |             100 |
| highs    |       100 |             100 |
| osqp     |        75 |             100 |
| proxqp   |       100 |             100 |
| qpoases  |        78 |              78 |
| qpswift  |       100 |             100 |
| quadprog |       100 |             100 |
| scs      |        73 |              73 |

### Computation time

We compare solver computation times over the whole test set using the shifted
geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of
Y is Y times slower than the best solver over the test set. See
[Metrics](README.md#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |
|:---------|----------:|----------------:|
| cvxopt   |    2773.3 |          2714.1 |
| ecos     |    3812.7 |          3731.4 |
| highs    |     116.9 |           114.6 |
| osqp     |      20.9 |           440.2 |
| proxqp   |       1.0 |             1.0 |
| qpoases  |      21.5 |            21.1 |
| qpswift  |    2773.1 |          2714.0 |
| quadprog |    1140.2 |          1115.9 |
| scs      |     406.4 |           399.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in
the OSQP and ProxQP benchmarks, we assume a solver's run time is at the time
limit when it fails to solve a problem.

### Primal error

The primal error measures the maximum (equality and inequality) constraint
violation in the solution returned by a solver. We use the shifted geometric
mean to compare solver primal errors over the whole test set. Intuitively, a
solver with a shifted-geometric-mean primal error of Y is Y times less precise
on constraints than the best solver over the test set. See
[Metrics](README.md#metrics) for details.

Shifted geometric means of solver primal errors (1.0 is the best):

|          |      default |    high_accuracy |
|:---------|-------------:|-----------------:|
| cvxopt   |     527798.3 |     5261657573.6 |
| ecos     |     571892.7 |     5701237334.8 |
| highs    |     143512.2 |     1430683413.5 |
| osqp     |    9066171.1 |     2894091781.5 |
| proxqp   |          1.0 |              1.0 |
| qpoases  |    8958208.9 |    89304997137.3 |
| qpswift  |     527798.3 |     5261657573.1 |
| quadprog |     407997.7 |     4067357227.8 |
| scs      | 4870961855.1 | 48553184278317.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a primal error equal to the
[primal tolerance](#settings).

### Cost errors

The cost error measures the difference between the known optimal objective and
the objective at the solution returned by a solver. We use the shifted
geometric mean to compare solver cost errors over the whole test set.
Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times
less precise on the optimal cost than the best solver over the test set. See
[Metrics](README.md#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |     default |   high_accuracy |
|:---------|------------:|----------------:|
| cvxopt   |       805.7 |          1591.8 |
| ecos     |      1107.8 |          2188.5 |
| highs    |        33.0 |            65.1 |
| osqp     |       558.7 |           258.1 |
| proxqp   |         1.0 |             1.0 |
| qpoases  |       198.5 |           392.2 |
| qpswift  |       805.7 |          1591.8 |
| quadprog |       331.3 |           654.5 |
| scs      | 318497951.6 |     626636328.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A
solver that fails to find a solution receives a cost error equal to the [cost
tolerance](#settings).
