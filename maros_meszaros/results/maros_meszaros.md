# Maros-Meszaros test set

| Version | 1.1.0 |
|:--------|:--------------------|
| Date    | 2023-08-23 11:41:27.391824+00:00 |
| CPU     | [Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz](#cpu-info) |
| Run by  | [@stephane-caron](https://github.com/stephane-caron/) |

## Contents

* [Description](#description)
* [Solvers](#solvers)
* [Settings](#settings)
* [CPU info](#cpu-info)
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

Standard set of problems designed to be difficult.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.5.1                 |
| cvxopt   | 1.3.2                 |
| gurobi   | 10.0.2 (size-limited) |
| highs    | 1.5.3                 |
| osqp     | 0.6.3                 |
| proxqp   | 0.4.1                 |
| scs      | 3.2.3                 |

All solvers were called via [qpsolvers](https://github.com/stephane-caron/qpsolvers) v3.5.0.

## CPU info

| Property | Value |
|----------|-------|
| `arch` | X86_64 |
| `arch_string_raw` | x86_64 |
| `bits` | 64 |
| `brand_raw` | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz |
| `count` | 4 |
| `cpuinfo_version_string` | 9.0.0 |
| `family` | 6 |
| `flags` | `3dnowprefetch`, `abm`, `acpi`, `adx`, `aes`, `aperfmperf`, `apic`, `arat`, `arch_capabilities`, `arch_perfmon`, `art`, `avx`, `avx2`, `bmi1`, `bmi2`, `bts`, `clflush`, `clflushopt`, `cmov`, `constant_tsc`, `cpuid`, `cpuid_fault`, `cx16`, `cx8`, `de`, `ds_cpl`, `dtes64`, `dtherm`, `dts`, `epb`, `ept`, `ept_ad`, `erms`, `est`, `f16c`, `flexpriority`, `flush_l1d`, `fma`, `fpu`, `fsgsbase`, `fxsr`, `ht`, `hwp`, `hwp_act_window`, `hwp_epp`, `hwp_notify`, `ibpb`, `ibrs`, `ida`, `intel_pt`, `invpcid`, `invpcid_single`, `lahf_lm`, `lm`, `mca`, `mce`, `md_clear`, `mmx`, `monitor`, `movbe`, `mpx`, `msr`, `mtrr`, `nonstop_tsc`, `nopl`, `nx`, `osxsave`, `pae`, `pat`, `pbe`, `pcid`, `pclmulqdq`, `pdcm`, `pdpe1gb`, `pebs`, `pge`, `pln`, `pni`, `popcnt`, `pse`, `pse36`, `pti`, `pts`, `rdrand`, `rdrnd`, `rdseed`, `rdtscp`, `rep_good`, `sdbg`, `sep`, `sgx`, `smap`, `smep`, `ss`, `ssbd`, `sse`, `sse2`, `sse4_1`, `sse4_2`, `ssse3`, `stibp`, `syscall`, `tm`, `tm2`, `tpr_shadow`, `tsc`, `tsc_adjust`, `tsc_deadline_timer`, `tscdeadline`, `vme`, `vmx`, `vnmi`, `vpid`, `x2apic`, `xgetbv1`, `xsave`, `xsavec`, `xsaveopt`, `xsaves`, `xtopology`, `xtpr` |
| `hz_actual_friendly` | 2.6000 GHz |
| `hz_advertised_friendly` | 2.5000 GHz |
| `l1_data_cache_size` | 65536 |
| `l1_instruction_cache_size` | 65536 |
| `l2_cache_associativity` | 6 |
| `l2_cache_line_size` | 256 |
| `l2_cache_size` | 524288 |
| `l3_cache_size` | 4194304 |
| `model` | 78 |
| `python_version` | 3.10.12.final.0 (64 bit) |
| `stepping` | 3 |
| `vendor_id_raw` | GenuineIntel |

## Settings

There are 3 settings: *default*, *high_accuracy* and *low_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   low_accuracy |   high_accuracy |
|:------------|----------:|---------------:|----------------:|
| ``cost``    |      1000 |       1000     |        1000     |
| ``dual``    |         1 |          0.001 |           1e-09 |
| ``gap``     |         1 |          0.001 |           1e-09 |
| ``primal``  |         1 |          0.001 |           1e-09 |
| ``runtime`` |      1000 |       1000     |        1000     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |   low_accuracy |
|:---------|:---------------------------------|:----------|----------------:|---------------:|
| clarabel | ``tol_feas``                     | -         |           1e-09 |          0.001 |
| clarabel | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |
| clarabel | ``tol_gap_rel``                  | -         |           0     |          0     |
| cvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |
| gurobi   | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |
| gurobi   | ``OptimalityTol``                | -         |           1e-09 |          0.001 |
| gurobi   | ``TimeLimit``                    | 1000.0    |        1000     |       1000     |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |
| highs    | ``time_limit``                   | 1000.0    |        1000     |       1000     |
| osqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| osqp     | ``eps_rel``                      | -         |           0     |          0     |
| osqp     | ``time_limit``                   | 1000.0    |        1000     |       1000     |
| proxqp   | ``check_duality_gap``            | -         |           1     |          1     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| proxqp   | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |
| proxqp   | ``eps_duality_gap_rel``          | -         |           0     |          0     |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |
| scs      | ``time_limit_secs``              | 1000.0    |        1000     |       1000     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpsolvers_benchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpsolvers_benchmark/issues/60): Conversion to SOCP limits performance of ECOS

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                89.9 |                                  1.0 |                                         1.0 |                                     1.9 |                                 1.0 |                               1.0 |
| cvxopt   |                                53.6 |                                 13.8 |                                         5.3 |                                     2.6 |                                22.9 |                               6.6 |
| gurobi   |                                16.7 |                                 57.8 |                                        10.5 |                                    37.5 |                                94.0 |                              34.9 |
| highs    |                                53.6 |                                 11.3 |                                         5.3 |                                     2.6 |                                21.2 |                               6.1 |
| osqp     |                                41.3 |                                  1.8 |                                        58.7 |                                    22.6 |                              1950.7 |                              42.4 |
| proxqp   |                                77.5 |                                  4.6 |                                         2.0 |                                     1.0 |                                11.5 |                               2.2 |
| scs      |                                60.1 |                                  2.1 |                                        37.5 |                                     3.4 |                               133.1 |                               8.4 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                61.6 |                                  1.0 |                                         1.0 |                                742803.1 |                                44.9 |                               1.0 |
| cvxopt   |                                 5.8 |                                  5.8 |                                   1484115.0 |                                   126.3 |                        1612205372.0 |                               5.0 |
| gurobi   |                                 5.1 |                                 19.2 |                                         4.3 |                            7166137621.8 |                        9769259351.6 |                              19.8 |
| highs    |                                 0.0 |                                  3.7 |                                      5416.6 |                                884752.7 |                        1987500500.6 |                               3.5 |
| osqp     |                                26.1 |                                 11.5 |                                         2.8 |                                     1.2 |                              3235.1 |                              11.7 |
| proxqp   |                                59.4 |                                  2.4 |                                         1.4 |                                     1.0 |                              5387.0 |                               2.2 |
| scs      |                                42.8 |                                  8.0 |                                         2.5 |                                     1.0 |                                 1.0 |                               7.6 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                91.3 |                                  1.0 |                                         1.8 |                                  1086.8 |                                 1.0 |                               1.0 |
| cvxopt   |                                42.8 |                                 21.8 |                                         3.5 |                                     3.9 |                              6604.3 |                               7.4 |
| gurobi   |                                16.7 |                                106.5 |                                         3.6 |                                 23665.7 |                             26882.1 |                              45.5 |
| highs    |                                37.7 |                                 20.8 |                                         1.8 |                                     5.1 |                              5469.8 |                               8.0 |
| osqp     |                                21.0 |                                 19.7 |                                         2.9 |                                     3.2 |                              4982.6 |                              11.6 |
| proxqp   |                                78.3 |                                  7.9 |                                         1.0 |                                     1.0 |                                19.6 |                               2.9 |
| scs      |                                71.0 |                                  9.3 |                                        31.3 |                                     2.2 |                                 1.6 |                               4.2 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        90 |              62 |             91 |
| cvxopt   |        54 |               6 |             43 |
| gurobi   |        17 |               5 |             17 |
| highs    |        54 |               0 |             38 |
| osqp     |        41 |              26 |             21 |
| proxqp   |        78 |              59 |             78 |
| scs      |        60 |              43 |             71 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        97 |              80 |             95 |
| cvxopt   |        91 |              49 |             78 |
| gurobi   |        91 |              79 |             91 |
| highs    |        91 |              38 |             75 |
| osqp     |        55 |              89 |             61 |
| proxqp   |        92 |              88 |             95 |
| scs      |        72 |              97 |             95 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |
| cvxopt   |      13.8 |             5.8 |           21.8 |
| gurobi   |      57.8 |            19.2 |          106.5 |
| highs    |      11.3 |             3.7 |           20.8 |
| osqp     |       1.8 |            11.5 |           19.7 |
| proxqp   |       4.6 |             2.4 |            7.9 |
| scs      |       2.1 |             8.0 |            9.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.8 |
| cvxopt   |       5.3 |       1484115.0 |            3.5 |
| gurobi   |      10.5 |             4.3 |            3.6 |
| highs    |       5.3 |          5416.6 |            1.8 |
| osqp     |      58.7 |             2.8 |            2.9 |
| proxqp   |       2.0 |             1.4 |            1.0 |
| scs      |      37.5 |             2.5 |           31.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.9 |        742803.1 |         1086.8 |
| cvxopt   |       2.6 |           126.3 |            3.9 |
| gurobi   |      37.5 |    7166137621.8 |        23665.7 |
| highs    |       2.6 |        884752.7 |            5.1 |
| osqp     |      22.6 |             1.2 |            3.2 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| scs      |       3.4 |             1.0 |            2.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |            44.9 |            1.0 |
| cvxopt   |      22.9 |    1612205372.0 |         6604.3 |
| gurobi   |      94.0 |    9769259351.6 |        26882.1 |
| highs    |      21.2 |    1987500500.6 |         5469.8 |
| osqp     |    1950.7 |          3235.1 |         4982.6 |
| proxqp   |      11.5 |          5387.0 |           19.6 |
| scs      |     133.1 |             1.0 |            1.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).

### Cost error

The cost error measures the difference between the known optimal objective and the objective at the solution returned by a solver. We use the shifted geometric mean to compare solver cost errors over the whole test set. Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times less precise on the optimal cost than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |             1.0 |            1.0 |
| cvxopt   |       6.6 |             5.0 |            7.4 |
| gurobi   |      34.9 |            19.8 |           45.5 |
| highs    |       6.1 |             3.5 |            8.0 |
| osqp     |      42.4 |            11.7 |           11.6 |
| proxqp   |       2.2 |             2.2 |            2.9 |
| scs      |       8.4 |             7.6 |            4.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a cost error equal to the [cost tolerance](#settings).
