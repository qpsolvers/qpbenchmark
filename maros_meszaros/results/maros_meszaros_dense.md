# Maros-Meszaros dense subset

| Version | 1.1.0 |
|:--------|:--------------------|
| Date    | 2023-08-30 12:33:12.633624+00:00 |
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

Subset of the Maros-Meszaros test set restricted to smaller dense problems.

## Solvers

| solver   | version               |
|:---------|:----------------------|
| clarabel | 0.5.1                 |
| cvxopt   | 1.3.2                 |
| daqp     | 0.5.1                 |
| ecos     | 2.0.11                |
| gurobi   | 10.0.2 (size-limited) |
| highs    | 1.5.3                 |
| osqp     | 0.6.3                 |
| piqp     | 0.2.2                 |
| proxqp   | 0.4.1                 |
| qpoases  | 3.2.1                 |
| qpswift  | 1.0.0                 |
| quadprog | 0.1.11                |
| scs      | 3.2.3                 |

All solvers were called via [qpsolvers](https://github.com/stephane-caron/qpsolvers) v4.0.0.

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

| solver   | parameter                        | default   | high_accuracy          | low_accuracy          |
|:---------|:---------------------------------|:----------|:-----------------------|:----------------------|
| clarabel | ``tol_feas``                     | -         | 1e-09                  | 0.001                 |
| clarabel | ``tol_gap_abs``                  | -         | 1e-09                  | 0.001                 |
| clarabel | ``tol_gap_rel``                  | -         | 0.0                    | 0.0                   |
| cvxopt   | ``feastol``                      | -         | 1e-09                  | 0.001                 |
| daqp     | ``dual_tol``                     | -         | 1e-09                  | 0.001                 |
| daqp     | ``primal_tol``                   | -         | 1e-09                  | 0.001                 |
| ecos     | ``feastol``                      | -         | 1e-09                  | 0.001                 |
| gurobi   | ``FeasibilityTol``               | -         | 1e-09                  | 0.001                 |
| gurobi   | ``OptimalityTol``                | -         | 1e-09                  | 0.001                 |
| gurobi   | ``TimeLimit``                    | 1000.0    | 1000.0                 | 1000.0                |
| highs    | ``dual_feasibility_tolerance``   | -         | 1e-09                  | 0.001                 |
| highs    | ``primal_feasibility_tolerance`` | -         | 1e-09                  | 0.001                 |
| highs    | ``time_limit``                   | 1000.0    | 1000.0                 | 1000.0                |
| hpipm    | ``tol_comp``                     | -         | 1e-09                  | 0.001                 |
| hpipm    | ``tol_eq``                       | -         | 1e-09                  | 0.001                 |
| hpipm    | ``tol_ineq``                     | -         | 1e-09                  | 0.001                 |
| hpipm    | ``tol_stat``                     | -         | 1e-09                  | 0.001                 |
| osqp     | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| osqp     | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
| osqp     | ``time_limit``                   | 1000.0    | 1000.0                 | 1000.0                |
| piqp     | ``check_duality_gap``            | -         | True                   | True                  |
| piqp     | ``eps_abs``                      | -         | 1e-09                  | 0.001                 |
| piqp     | ``eps_duality_gap_abs``          | -         | 1e-09                  | 0.001                 |
| piqp     | ``eps_duality_gap_rel``          | -         | 0.0                    | 0.0                   |
| piqp     | ``eps_rel``                      | -         | 0.0                    | 0.0                   |
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

The following [issues](https://github.com/qpsolvers/qpsolvers_benchmark/issues) have been identified as impacting the fairness of this benchmark. Keep them in mind when drawing conclusions from the results.

- [#60](https://github.com/qpsolvers/qpsolvers_benchmark/issues/60): Conversion to SOCP limits performance of ECOS

## Results by settings

### Default

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                96.8 |                                  6.6 |                                     27044.4 |                                 42820.4 |                                 1.0 |                               6.0 |
| cvxopt   |                                66.1 |                                 94.5 |                                    218701.0 |                                345841.1 |                                35.0 |                              49.2 |
| daqp     |                                30.6 |                                956.1 |                                    600178.5 |                                949079.0 |                                20.7 |                             470.5 |
| ecos     |                                12.9 |                               2057.1 |                                    745533.1 |                               1209371.0 |                                25.7 |                            1012.5 |
| gurobi   |                                37.1 |                                262.6 |                                    372208.9 |                              17512535.1 |                               645.8 |                             129.2 |
| highs    |                                61.3 |                                103.6 |                                    232549.3 |                                403411.7 |                                52.0 |                              51.1 |
| hpipm    |                                24.2 |                                338.1 |                                   7527265.0 |                                655503.5 |                                14.6 |                             167.6 |
| osqp     |                                51.6 |                                 27.8 |                                   4204778.0 |                               4635783.3 |                              3099.2 |                             421.0 |
| piqp     |                                95.2 |                                  6.7 |                                     27044.4 |                                 42774.4 |                                 2.0 |                               3.9 |
| proxqp   |                                96.8 |                                  1.0 |                                         1.0 |                                     1.0 |                                 5.8 |                               1.0 |
| qpoases  |                                24.2 |                                293.6 |                                   6001873.6 |                              30019506.1 |                                13.3 |                             528.0 |
| qpswift  |                                25.8 |                               1205.1 |                                    643550.4 |                               1017664.4 |                                22.2 |                             593.2 |
| quadprog |                                32.3 |                                884.3 |                                    585765.4 |                                926287.3 |                                20.2 |                             435.3 |
| scs      |                                71.0 |                                  7.7 |                                   2500525.0 |                                475864.5 |                               432.6 |                             107.3 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                72.6 |                                  2.1 |                                         1.1 |                                    15.2 |                               282.9 |                               2.7 |
| cvxopt   |                                 3.2 |                                 16.4 |                                         5.0 |                                   959.7 |                         828721099.4 |                              18.1 |
| daqp     |                                24.2 |                                120.0 |                                       248.0 |                                     4.1 |                           1343168.0 |                             131.4 |
| ecos     |                                 0.0 |                                239.0 |                                         6.5 |                              28777958.1 |                            992912.4 |                             261.7 |
| gurobi   |                                11.3 |                                 30.5 |                                         8.9 |                           66691063931.3 |                       44215628581.3 |                              33.4 |
| highs    |                                 0.0 |                                 12.0 |                                         3.1 |                             142759814.4 |                        3123675547.7 |                              13.2 |
| hpipm    |                                32.3 |                                 54.6 |                                         4.2 |                                     3.2 |                                 5.5 |                             155.7 |
| osqp     |                                41.9 |                                 39.3 |                                         4.2 |                                     3.2 |                                 3.6 |                              43.0 |
| piqp     |                                80.6 |                                  3.2 |                                         1.0 |                                     1.4 |                                 2.6 |                               3.6 |
| proxqp   |                                80.6 |                                  1.0 |                                         1.1 |                                     1.0 |                                72.0 |                               1.0 |
| qpoases  |                                19.4 |                                 37.6 |                               46275210514.5 |                          114700822389.8 |                                 1.7 |                             136.4 |
| qpswift  |                                17.7 |                                140.0 |                                         5.6 |                                     4.4 |                             47354.4 |                             153.3 |
| quadprog |                                25.8 |                                102.7 |                                         9.6 |                                    15.5 |                                11.3 |                             112.5 |
| scs      |                                67.7 |                                 16.3 |                                         2.8 |                                     2.3 |                                 1.0 |                              17.7 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                93.5 |                                  6.3 |                                         1.0 |                                    11.2 |                                 1.0 |                               9.4 |
| cvxopt   |                                51.6 |                                 81.8 |                                         7.5 |                                    24.3 |                              5107.8 |                              69.6 |
| daqp     |                                25.8 |                                920.4 |                                        26.0 |                                    67.6 |                                 7.5 |                             741.2 |
| ecos     |                                11.3 |                               2136.4 |                                        27.0 |                                    96.2 |                                 5.1 |                            1720.7 |
| gurobi   |                                37.1 |                                252.6 |                                        13.5 |                               1140327.0 |                            115512.4 |                             203.6 |
| highs    |                                45.2 |                                 99.8 |                                         8.5 |                                  2467.6 |                              8161.8 |                              80.5 |
| hpipm    |                                27.4 |                                416.9 |                                        16.6 |                                    54.9 |                                20.6 |                             878.8 |
| osqp     |                                38.7 |                                194.2 |                                        14.5 |                                    52.0 |                               783.4 |                             159.1 |
| piqp     |                                95.2 |                                  9.9 |                                         1.6 |                                    14.7 |                                 1.4 |                               8.1 |
| proxqp   |                                96.8 |                                  1.0 |                                         1.6 |                                     1.0 |                                52.5 |                               1.0 |
| qpoases  |                                19.4 |                                326.9 |                                    123757.7 |                               1327588.7 |                                 2.8 |                             746.9 |
| qpswift  |                                24.2 |                               1160.1 |                                        23.0 |                                    73.6 |                                15.2 |                             934.6 |
| quadprog |                                32.3 |                                851.3 |                                        21.0 |                                    66.1 |                                 3.9 |                             685.7 |
| scs      |                                80.6 |                                 58.3 |                                         9.4 |                                    27.2 |                                 2.1 |                              45.8 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |        97 |              73 |             94 |
| cvxopt   |        66 |               3 |             52 |
| daqp     |        31 |              24 |             26 |
| ecos     |        13 |               0 |             11 |
| gurobi   |        37 |              11 |             37 |
| highs    |        61 |               0 |             45 |
| hpipm    |        24 |              32 |             27 |
| osqp     |        52 |              42 |             39 |
| piqp     |        95 |              81 |             95 |
| proxqp   |        97 |              81 |             97 |
| qpoases  |        24 |              19 |             19 |
| qpswift  |        26 |              18 |             24 |
| quadprog |        32 |              26 |             32 |
| scs      |        71 |              68 |             81 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              81 |             97 |
| cvxopt   |        92 |              35 |             76 |
| daqp     |       100 |              95 |             95 |
| ecos     |        98 |              85 |             98 |
| gurobi   |        81 |              55 |             81 |
| highs    |        89 |              27 |             73 |
| hpipm    |        73 |              87 |             81 |
| osqp     |        63 |              90 |             77 |
| piqp     |        98 |              92 |            100 |
| proxqp   |        97 |              84 |             97 |
| qpoases  |        69 |              65 |             68 |
| qpswift  |       100 |              92 |             98 |
| quadprog |       100 |              94 |            100 |
| scs      |        74 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       6.6 |             2.1 |            6.3 |
| cvxopt   |      94.5 |            16.4 |           81.8 |
| daqp     |     956.1 |           120.0 |          920.4 |
| ecos     |    2057.1 |           239.0 |         2136.4 |
| gurobi   |     262.6 |            30.5 |          252.6 |
| highs    |     103.6 |            12.0 |           99.8 |
| hpipm    |     338.1 |            54.6 |          416.9 |
| osqp     |      27.8 |            39.3 |          194.2 |
| piqp     |       6.7 |             3.2 |            9.9 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     293.6 |            37.6 |          326.9 |
| qpswift  |    1205.1 |           140.0 |         1160.1 |
| quadprog |     884.3 |           102.7 |          851.3 |
| scs      |       7.7 |            16.3 |           58.3 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |   27044.4 |             1.1 |            1.0 |
| cvxopt   |  218701.0 |             5.0 |            7.5 |
| daqp     |  600178.5 |           248.0 |           26.0 |
| ecos     |  745533.1 |             6.5 |           27.0 |
| gurobi   |  372208.9 |             8.9 |           13.5 |
| highs    |  232549.3 |             3.1 |            8.5 |
| hpipm    | 7527265.0 |             4.2 |           16.6 |
| osqp     | 4204778.0 |             4.2 |           14.5 |
| piqp     |   27044.4 |             1.0 |            1.6 |
| proxqp   |       1.0 |             1.1 |            1.6 |
| qpoases  | 6001873.6 |   46275210514.5 |       123757.7 |
| qpswift  |  643550.4 |             5.6 |           23.0 |
| quadprog |  585765.4 |             9.6 |           21.0 |
| scs      | 2500525.0 |             2.8 |            9.4 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |    default |   high_accuracy |   low_accuracy |
|:---------|-----------:|----------------:|---------------:|
| clarabel |    42820.4 |            15.2 |           11.2 |
| cvxopt   |   345841.1 |           959.7 |           24.3 |
| daqp     |   949079.0 |             4.1 |           67.6 |
| ecos     |  1209371.0 |      28777958.1 |           96.2 |
| gurobi   | 17512535.1 |   66691063931.3 |      1140327.0 |
| highs    |   403411.7 |     142759814.4 |         2467.6 |
| hpipm    |   655503.5 |             3.2 |           54.9 |
| osqp     |  4635783.3 |             3.2 |           52.0 |
| piqp     |    42774.4 |             1.4 |           14.7 |
| proxqp   |        1.0 |             1.0 |            1.0 |
| qpoases  | 30019506.1 |  114700822389.8 |      1327588.7 |
| qpswift  |  1017664.4 |             4.4 |           73.6 |
| quadprog |   926287.3 |            15.5 |           66.1 |
| scs      |   475864.5 |             2.3 |           27.2 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.0 |           282.9 |            1.0 |
| cvxopt   |      35.0 |     828721099.4 |         5107.8 |
| daqp     |      20.7 |       1343168.0 |            7.5 |
| ecos     |      25.7 |        992912.4 |            5.1 |
| gurobi   |     645.8 |   44215628581.3 |       115512.4 |
| highs    |      52.0 |    3123675547.7 |         8161.8 |
| hpipm    |      14.6 |             5.5 |           20.6 |
| osqp     |    3099.2 |             3.6 |          783.4 |
| piqp     |       2.0 |             2.6 |            1.4 |
| proxqp   |       5.8 |            72.0 |           52.5 |
| qpoases  |      13.3 |             1.7 |            2.8 |
| qpswift  |      22.2 |         47354.4 |           15.2 |
| quadprog |      20.2 |            11.3 |            3.9 |
| scs      |     432.6 |             1.0 |            2.1 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).

### Cost error

The cost error measures the difference between the known optimal objective and the objective at the solution returned by a solver. We use the shifted geometric mean to compare solver cost errors over the whole test set. Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times less precise on the optimal cost than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       6.0 |             2.7 |            9.4 |
| cvxopt   |      49.2 |            18.1 |           69.6 |
| daqp     |     470.5 |           131.4 |          741.2 |
| ecos     |    1012.5 |           261.7 |         1720.7 |
| gurobi   |     129.2 |            33.4 |          203.6 |
| highs    |      51.1 |            13.2 |           80.5 |
| hpipm    |     167.6 |           155.7 |          878.8 |
| osqp     |     421.0 |            43.0 |          159.1 |
| piqp     |       3.9 |             3.6 |            8.1 |
| proxqp   |       1.0 |             1.0 |            1.0 |
| qpoases  |     528.0 |           136.4 |          746.9 |
| qpswift  |     593.2 |           153.3 |          934.6 |
| quadprog |     435.3 |           112.5 |          685.7 |
| scs      |     107.3 |            17.7 |           45.8 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a cost error equal to the [cost tolerance](#settings).
