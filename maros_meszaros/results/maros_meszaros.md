# Maros-Meszaros test set

| Benchmark version | 1.2.0 |
|:------------------|:--------------------|
| Date              | 2023-11-25 15:03:11.482288+00:00 |
| CPU               | [Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz](#cpu-info) |
| Run by            | [@stephane-caron](https://github.com/stephane-caron/) |

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
    * [Mid accuracy](#mid-accuracy)
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
| piqp     | 0.2.2                 |
| proxqp   | 0.4.1                 |
| scs      | 3.2.3                 |

All solvers were called via [qpsolvers](https://github.com/qpsolvers/qpsolvers) v4.0.0.

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

There are 4 settings: *default*, *high_accuracy*, *low_accuracy* and *mid_accuracy*. They validate solutions using the following tolerances:

| tolerance   |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:------------|----------:|----------------:|---------------:|---------------:|
| ``cost``    |      1000 |        1000     |       1000     |       1000     |
| ``dual``    |         1 |           1e-09 |          0.001 |          1e-06 |
| ``gap``     |         1 |           1e-09 |          0.001 |          1e-06 |
| ``primal``  |         1 |           1e-09 |          0.001 |          1e-06 |
| ``runtime`` |      1000 |        1000     |       1000     |       1000     |

Solvers for each settings are configured as follows:

| solver   | parameter                        | default   |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|:---------------------------------|:----------|----------------:|---------------:|---------------:|
| clarabel | ``tol_feas``                     | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_abs``                  | -         |           1e-09 |          0.001 |          1e-06 |
| clarabel | ``tol_gap_rel``                  | -         |           0     |          0     |          0     |
| cvxopt   | ``feastol``                      | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``FeasibilityTol``               | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``OptimalityTol``                | -         |           1e-09 |          0.001 |          1e-06 |
| gurobi   | ``TimeLimit``                    | 1000.0    |        1000     |       1000     |       1000     |
| highs    | ``dual_feasibility_tolerance``   | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``primal_feasibility_tolerance`` | -         |           1e-09 |          0.001 |          1e-06 |
| highs    | ``time_limit``                   | 1000.0    |        1000     |       1000     |       1000     |
| osqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| osqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| osqp     | ``time_limit``                   | 1000.0    |        1000     |       1000     |       1000     |
| piqp     | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| piqp     | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| piqp     | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| piqp     | ``eps_rel``                      | -         |           0     |          0     |          0     |
| proxqp   | ``check_duality_gap``            | -         |           1     |          1     |          1     |
| proxqp   | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_abs``          | -         |           1e-09 |          0.001 |          1e-06 |
| proxqp   | ``eps_duality_gap_rel``          | -         |           0     |          0     |          0     |
| proxqp   | ``eps_rel``                      | -         |           0     |          0     |          0     |
| scs      | ``eps_abs``                      | -         |           1e-09 |          0.001 |          1e-06 |
| scs      | ``eps_rel``                      | -         |           0     |          0     |          0     |
| scs      | ``time_limit_secs``              | 1000.0    |        1000     |       1000     |       1000     |

## Known limitations

The following [issues](https://github.com/qpsolvers/qpbenchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpbenchmark/issues/60): Conversion to SOCP limits performance of ECOS

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                89.9 |                                  4.2 |                                         4.9 |                                    19.0 |                                 1.0 |                               1.9 |
| cvxopt   |                                53.6 |                                 57.1 |                                        26.0 |                                    26.4 |                                22.9 |                              12.3 |
| gurobi   |                                16.7 |                                239.8 |                                        51.8 |                                   377.3 |                                94.0 |                              64.9 |
| highs    |                                53.6 |                                 46.7 |                                        26.0 |                                    26.5 |                                21.2 |                              11.3 |
| osqp     |                                41.3 |                                  7.6 |                                       289.6 |                                   227.4 |                              1950.7 |                              79.0 |
| piqp     |                                94.2 |                                  1.0 |                                         1.0 |                                     1.0 |                                 6.6 |                               1.0 |
| proxqp   |                                77.5 |                                 19.1 |                                         9.9 |                                    10.1 |                                11.5 |                               4.1 |
| scs      |                                60.1 |                                  8.8 |                                       185.1 |                                    33.9 |                               133.1 |                              15.7 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                61.6 |                                  1.0 |                                         1.0 |                               1162631.8 |                                44.9 |                               1.0 |
| cvxopt   |                                 5.8 |                                  5.8 |                                   1484115.0 |                                   197.7 |                        1612205372.0 |                               5.0 |
| gurobi   |                                 5.1 |                                 19.2 |                                         4.3 |                           11216402921.9 |                        9769259351.6 |                              19.8 |
| highs    |                                 0.0 |                                  3.7 |                                      5416.6 |                               1384810.5 |                        1987500500.6 |                               3.5 |
| osqp     |                                26.1 |                                 11.5 |                                         2.8 |                                     1.9 |                              3235.1 |                              11.7 |
| piqp     |                                66.7 |                                  1.3 |                                         1.0 |                                     1.0 |                              7236.2 |                               1.7 |
| proxqp   |                                59.4 |                                  2.4 |                                         1.4 |                                     1.6 |                              5387.0 |                               2.2 |
| scs      |                                42.8 |                                  8.0 |                                         2.5 |                                     1.6 |                                 1.0 |                               7.6 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                91.3 |                                  2.3 |                                         1.8 |                                  1480.4 |                                 1.0 |                               1.3 |
| cvxopt   |                                42.8 |                                 49.6 |                                         3.5 |                                     5.3 |                              6604.3 |                               9.3 |
| gurobi   |                                16.7 |                                242.4 |                                         3.6 |                                 32236.4 |                             26882.1 |                              57.4 |
| highs    |                                37.7 |                                 47.2 |                                         1.8 |                                     6.9 |                              5469.8 |                              10.0 |
| osqp     |                                21.0 |                                 44.8 |                                         2.9 |                                     4.4 |                              4982.6 |                              14.6 |
| piqp     |                                94.9 |                                  1.0 |                                         2.9 |                                     1.0 |                                 1.3 |                               1.0 |
| proxqp   |                                78.3 |                                 18.0 |                                         1.0 |                                     1.4 |                                19.6 |                               3.6 |
| scs      |                                71.0 |                                 21.1 |                                        31.3 |                                     3.0 |                                 1.6 |                               5.3 |

### Mid accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpbenchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                86.2 |                                  1.8 |                                     10229.0 |                               1774899.6 |                                19.6 |                               1.5 |
| cvxopt   |                                23.2 |                                 18.8 |                                      5744.4 |                                    25.8 |                           2879762.0 |                               9.7 |
| gurobi   |                                13.8 |                                 90.6 |                                        14.3 |                              36952900.6 |                          12251728.7 |                              55.5 |
| highs    |                                13.8 |                                 22.0 |                                        34.1 |                              15506753.1 |                           2515033.6 |                              12.3 |
| osqp     |                                24.6 |                                 42.5 |                                        12.5 |                                     6.1 |                             26681.1 |                              25.6 |
| piqp     |                                90.6 |                                  1.0 |                                         1.0 |                                     1.0 |                                 9.6 |                               1.0 |
| proxqp   |                                76.1 |                                  9.2 |                                         4.9 |                                     2.0 |                                16.0 |                               4.0 |
| scs      |                                60.1 |                                 18.3 |                                         9.3 |                                     4.1 |                                 1.0 |                               9.6 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        90 |              62 |             91 |             86 |
| cvxopt   |        54 |               6 |             43 |             23 |
| gurobi   |        17 |               5 |             17 |             14 |
| highs    |        54 |               0 |             38 |             14 |
| osqp     |        41 |              26 |             21 |             25 |
| piqp     |        94 |              67 |             95 |             91 |
| proxqp   |        78 |              59 |             78 |             76 |
| scs      |        60 |              43 |             71 |             60 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |        97 |              80 |             95 |             94 |
| cvxopt   |        91 |              49 |             78 |             59 |
| gurobi   |        91 |              79 |             91 |             88 |
| highs    |        91 |              38 |             75 |             56 |
| osqp     |        55 |              89 |             61 |             83 |
| piqp     |        96 |              91 |             96 |             96 |
| proxqp   |        92 |              88 |             95 |             98 |
| scs      |        72 |              97 |             95 |             99 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       4.2 |             1.0 |            2.3 |            1.8 |
| cvxopt   |      57.1 |             5.8 |           49.6 |           18.8 |
| gurobi   |     239.8 |            19.2 |          242.4 |           90.6 |
| highs    |      46.7 |             3.7 |           47.2 |           22.0 |
| osqp     |       7.6 |            11.5 |           44.8 |           42.5 |
| piqp     |       1.0 |             1.3 |            1.0 |            1.0 |
| proxqp   |      19.1 |             2.4 |           18.0 |            9.2 |
| scs      |       8.8 |             8.0 |           21.1 |           18.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       4.9 |             1.0 |            1.8 |        10229.0 |
| cvxopt   |      26.0 |       1484115.0 |            3.5 |         5744.4 |
| gurobi   |      51.8 |             4.3 |            3.6 |           14.3 |
| highs    |      26.0 |          5416.6 |            1.8 |           34.1 |
| osqp     |     289.6 |             2.8 |            2.9 |           12.5 |
| piqp     |       1.0 |             1.0 |            2.9 |            1.0 |
| proxqp   |       9.9 |             1.4 |            1.0 |            4.9 |
| scs      |     185.1 |             2.5 |           31.3 |            9.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |      19.0 |       1162631.8 |         1480.4 |      1774899.6 |
| cvxopt   |      26.4 |           197.7 |            5.3 |           25.8 |
| gurobi   |     377.3 |   11216402921.9 |        32236.4 |     36952900.6 |
| highs    |      26.5 |       1384810.5 |            6.9 |     15506753.1 |
| osqp     |     227.4 |             1.9 |            4.4 |            6.1 |
| piqp     |       1.0 |             1.0 |            1.0 |            1.0 |
| proxqp   |      10.1 |             1.6 |            1.4 |            2.0 |
| scs      |      33.9 |             1.6 |            3.0 |            4.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.0 |            44.9 |            1.0 |           19.6 |
| cvxopt   |      22.9 |    1612205372.0 |         6604.3 |      2879762.0 |
| gurobi   |      94.0 |    9769259351.6 |        26882.1 |     12251728.7 |
| highs    |      21.2 |    1987500500.6 |         5469.8 |      2515033.6 |
| osqp     |    1950.7 |          3235.1 |         4982.6 |        26681.1 |
| piqp     |       6.6 |          7236.2 |            1.3 |            9.6 |
| proxqp   |      11.5 |          5387.0 |           19.6 |           16.0 |
| scs      |     133.1 |             1.0 |            1.6 |            1.0 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).

### Cost error

The cost error measures the difference between the known optimal objective and the objective at the solution returned by a solver. We use the shifted geometric mean to compare solver cost errors over the whole test set. Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times less precise on the optimal cost than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpbenchmark#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |   mid_accuracy |
|:---------|----------:|----------------:|---------------:|---------------:|
| clarabel |       1.9 |             1.0 |            1.3 |            1.5 |
| cvxopt   |      12.3 |             5.0 |            9.3 |            9.7 |
| gurobi   |      64.9 |            19.8 |           57.4 |           55.5 |
| highs    |      11.3 |             3.5 |           10.0 |           12.3 |
| osqp     |      79.0 |            11.7 |           14.6 |           25.6 |
| piqp     |       1.0 |             1.7 |            1.0 |            1.0 |
| proxqp   |       4.1 |             2.2 |            3.6 |            4.0 |
| scs      |      15.7 |             7.6 |            5.3 |            9.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a cost error equal to the [cost tolerance](#settings).
