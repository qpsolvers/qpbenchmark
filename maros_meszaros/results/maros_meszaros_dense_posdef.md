# Maros-Meszaros dense positive definite subset

| Benchmark version | 1.1.0 |
|:------------------|:--------------------|
| Date              | 2023-08-30 12:58:14.908876+00:00 |
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
* [Results by metric](#results-by-metric)
    * [Success rate](#success-rate)
    * [Computation time](#computation-time)
    * [Optimality conditions](#optimality-conditions)
        * [Primal residual](#primal-residual)
        * [Dual residual](#dual-residual)
        * [Duality gap](#duality-gap)
    * [Cost error](#cost-error)

## Description

Subset of the Maros-Meszaros test set restricted to smaller dense problems with positive definite Hessian matrix.

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
| piqp     | ``check_duality_gap``            | -         | 1.0                    | 1.0                   |
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
| clarabel |                               100.0 |                                  1.1 |                                       446.9 |                                  5114.3 |                                10.8 |                               1.7 |
| cvxopt   |                                84.2 |                               1455.8 |                               90710810719.0 |                             180719278.9 |                             11283.6 |                            3962.0 |
| daqp     |                               100.0 |                                  1.7 |                                    239825.3 |                                     1.0 |                               147.5 |                               1.0 |
| ecos     |                                36.8 |                              18268.3 |                              339387408823.0 |                             759362274.8 |                             42471.9 |                           49754.1 |
| gurobi   |                                57.9 |                                852.9 |                               60322069328.9 |                           12890168669.6 |                           1612059.3 |                            2312.5 |
| highs    |                               100.0 |                                  4.5 |                                        22.6 |                                 10710.7 |                              3042.0 |                               1.7 |
| hpipm    |                                52.6 |                               2226.7 |                              527740292191.2 |                             241565698.5 |                             15006.2 |                            6066.8 |
| osqp     |                                78.9 |                                  1.0 |                              625462174256.2 |                            3618509430.8 |                           2295466.7 |                           14627.4 |
| piqp     |                               100.0 |                                  1.8 |                                         1.0 |                                   195.1 |                                 1.0 |                               1.7 |
| proxqp   |                                94.7 |                                  4.5 |                                   1049423.1 |                                  1210.9 |                              7967.4 |                              39.9 |
| qpoases  |                                57.9 |                               3214.8 |                              254309453730.6 |                           23011750649.4 |                             18805.1 |                           15514.8 |
| qpswift  |                                42.1 |                              18259.1 |                              339387409048.1 |                             676146407.1 |                             42199.8 |                           49767.5 |
| quadprog |                                84.2 |                               1453.9 |                               90710810719.0 |                             180719102.8 |                             11226.4 |                            3961.8 |
| scs      |                                89.5 |                                 23.9 |                              628784917927.6 |                              80666615.1 |                            548544.3 |                            7000.5 |

### High accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                                84.2 |                                188.3 |                                         2.8 |                                    19.0 |                                 3.4 |                            1333.5 |
| cvxopt   |                                 5.3 |                                323.0 |                                         4.2 |                                   292.7 |                           3221384.9 |                            2284.6 |
| daqp     |                                78.9 |                                 82.9 |                                      2770.9 |                                     1.2 |                           8430005.5 |                             586.3 |
| ecos     |                                 0.0 |                               4050.9 |                                        15.3 |                             178183023.9 |                           6231552.4 |                           28689.7 |
| gurobi   |                                 5.3 |                                188.5 |                                         2.8 |                          114755681492.7 |                       90789765573.8 |                            1333.5 |
| highs    |                                 0.0 |                                  1.0 |                                         1.0 |                                 97221.0 |                         173856845.8 |                               1.0 |
| hpipm    |                                57.9 |                               1798.2 |                                        11.1 |                                     4.8 |                                 2.0 |                           13735.3 |
| osqp     |                                63.2 |                                493.9 |                                         8.3 |                                     3.3 |                                 2.6 |                            3498.3 |
| piqp     |                                84.2 |                                188.5 |                                         2.8 |                                     2.6 |                                 2.4 |                            1332.9 |
| proxqp   |                                84.2 |                                 85.1 |                                         5.7 |                                     1.0 |                                 2.3 |                             586.8 |
| qpoases  |                                52.6 |                                713.4 |                                4409966163.4 |                          201023358037.0 |                                 1.1 |                            8946.3 |
| qpswift  |                                26.3 |                               4049.0 |                                        15.6 |                                     6.5 |                            297175.8 |                           28689.9 |
| quadprog |                                78.9 |                                322.4 |                                         4.2 |                                     5.8 |                                 1.0 |                            2284.5 |
| scs      |                                84.2 |                                323.8 |                                         5.9 |                                     2.6 |                                 1.4 |                            2284.5 |

### Low accuracy

Solvers are compared over the whole test set by [shifted geometric mean](https://github.com/qpsolvers/qpsolvers_benchmark#shifted-geometric-mean) (shm). Lower is better, 1.0 is the best.

|          |   [Success rate](#success-rate) (%) |   [Runtime](#computation-time) (shm) |   [Primal residual](#primal-residual) (shm) |   [Dual residual](#dual-residual) (shm) |   [Duality gap](#duality-gap) (shm) |   [Cost error](#cost-error) (shm) |
|:---------|------------------------------------:|-------------------------------------:|--------------------------------------------:|----------------------------------------:|------------------------------------:|----------------------------------:|
| clarabel |                               100.0 |                                  1.0 |                                         6.6 |                                  5584.4 |                                 1.0 |                               1.7 |
| cvxopt   |                                73.7 |                                761.1 |                                   2781805.5 |                                159747.5 |                                 5.7 |                            2247.7 |
| daqp     |                                84.2 |                                  1.5 |                                  12661580.2 |                                     1.0 |                                12.9 |                               1.0 |
| ecos     |                                31.6 |                              20933.7 |                                  16691272.3 |                               1202649.5 |                                 4.4 |                           62666.8 |
| gurobi   |                                57.9 |                                752.1 |                                   2781805.5 |                           12644995937.7 |                            139251.1 |                            2248.5 |
| highs    |                                78.9 |                                  4.0 |                                         1.0 |                                 10712.6 |                               266.7 |                               1.7 |
| hpipm    |                                26.3 |                               7174.0 |                                  11472602.8 |                                605733.9 |                                38.1 |                           23164.3 |
| osqp     |                                57.9 |                                751.6 |                                   5534128.0 |                                476956.1 |                              2859.0 |                            2500.4 |
| piqp     |                               100.0 |                                  1.9 |                                       257.1 |                                239713.8 |                                 1.4 |                               1.7 |
| proxqp   |                                89.5 |                                  4.1 |                                   3778405.3 |                                 39088.2 |                               191.1 |                               1.8 |
| qpoases  |                                52.6 |                               2841.3 |                                4417036903.5 |                           22251703189.3 |                                 1.7 |                           15085.7 |
| qpswift  |                                36.8 |                              16153.2 |                                  15300315.6 |                                730158.5 |                                44.0 |                           48410.2 |
| quadprog |                                84.2 |                               1286.3 |                                   4172719.2 |                                188214.0 |                                 1.0 |                            3852.2 |
| scs      |                                89.5 |                                764.7 |                                   5457983.5 |                                210237.9 |                                 1.6 |                            2248.6 |

## Results by metric

### Success rate

Precentage of problems each solver is able to solve:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              84 |            100 |
| cvxopt   |        84 |               5 |             74 |
| daqp     |       100 |              79 |             84 |
| ecos     |        37 |               0 |             32 |
| gurobi   |        58 |               5 |             58 |
| highs    |       100 |               0 |             79 |
| hpipm    |        53 |              58 |             26 |
| osqp     |        79 |              63 |             58 |
| piqp     |       100 |              84 |            100 |
| proxqp   |        95 |              84 |             89 |
| qpoases  |        58 |              53 |             53 |
| qpswift  |        42 |              26 |             37 |
| quadprog |        84 |              79 |             84 |
| scs      |        89 |              84 |             89 |

Rows are [solvers](#solvers) and columns are [settings](#settings). We consider that a solver successfully solved a problem when (1) it returned with a success status and (2) its solution satisfies optimality conditions within [tolerance](#settings). The second table below summarizes the frequency at which solvers return success (1) and the corresponding solution did indeed pass tolerance checks.

Percentage of problems where "solved" return codes are correct:

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       100 |              95 |            100 |
| cvxopt   |       100 |              21 |             84 |
| daqp     |       100 |              84 |             84 |
| ecos     |        95 |              58 |             95 |
| gurobi   |        68 |              16 |             68 |
| highs    |       100 |               0 |             79 |
| hpipm    |        74 |             100 |             68 |
| osqp     |        79 |              84 |             68 |
| piqp     |       100 |              95 |            100 |
| proxqp   |        95 |              89 |             89 |
| qpoases  |        84 |              79 |             79 |
| qpswift  |       100 |              84 |             95 |
| quadprog |       100 |              95 |            100 |
| scs      |        89 |             100 |            100 |

### Computation time

We compare solver computation times over the whole test set using the shifted geometric mean. Intuitively, a solver with a shifted-geometric-mean runtime of Y is Y times slower than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric mean of solver computation times (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.1 |           188.3 |            1.0 |
| cvxopt   |    1455.8 |           323.0 |          761.1 |
| daqp     |       1.7 |            82.9 |            1.5 |
| ecos     |   18268.3 |          4050.9 |        20933.7 |
| gurobi   |     852.9 |           188.5 |          752.1 |
| highs    |       4.5 |             1.0 |            4.0 |
| hpipm    |    2226.7 |          1798.2 |         7174.0 |
| osqp     |       1.0 |           493.9 |          751.6 |
| piqp     |       1.8 |           188.5 |            1.9 |
| proxqp   |       4.5 |            85.1 |            4.1 |
| qpoases  |    3214.8 |           713.4 |         2841.3 |
| qpswift  |   18259.1 |          4049.0 |        16153.2 |
| quadprog |    1453.9 |           322.4 |         1286.3 |
| scs      |      23.9 |           323.8 |          764.7 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. As in the OSQP and ProxQP benchmarks, we assume a solver's run time is at the [time limit](#settings) when it fails to solve a problem.

### Optimality conditions

#### Primal residual

The primal residual measures the maximum (equality and inequality) constraint violation in the solution returned by a solver. We use the shifted geometric mean to compare solver primal residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean primal residual of Y is Y times less precise on constraints than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of primal residuals (1.0 is the best):

|          |        default |   high_accuracy |   low_accuracy |
|:---------|---------------:|----------------:|---------------:|
| clarabel |          446.9 |             2.8 |            6.6 |
| cvxopt   |  90710810719.0 |             4.2 |      2781805.5 |
| daqp     |       239825.3 |          2770.9 |     12661580.2 |
| ecos     | 339387408823.0 |            15.3 |     16691272.3 |
| gurobi   |  60322069328.9 |             2.8 |      2781805.5 |
| highs    |           22.6 |             1.0 |            1.0 |
| hpipm    | 527740292191.2 |            11.1 |     11472602.8 |
| osqp     | 625462174256.2 |             8.3 |      5534128.0 |
| piqp     |            1.0 |             2.8 |          257.1 |
| proxqp   |      1049423.1 |             5.7 |      3778405.3 |
| qpoases  | 254309453730.6 |    4409966163.4 |   4417036903.5 |
| qpswift  | 339387409048.1 |            15.6 |     15300315.6 |
| quadprog |  90710810719.0 |             4.2 |      4172719.2 |
| scs      | 628784917927.6 |             5.9 |      5457983.5 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a primal residual equal to the full [primal tolerance](#settings).

#### Dual residual

The dual residual measures the maximum violation of the dual feasibility condition in the solution returned by a solver. We use the shifted geometric mean to compare solver dual residuals over the whole test set. Intuitively, a solver with a shifted-geometric-mean dual residual of Y is Y times less precise on the dual feasibility condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of dual residuals (1.0 is the best):

|          |       default |   high_accuracy |   low_accuracy |
|:---------|--------------:|----------------:|---------------:|
| clarabel |        5114.3 |            19.0 |         5584.4 |
| cvxopt   |   180719278.9 |           292.7 |       159747.5 |
| daqp     |           1.0 |             1.2 |            1.0 |
| ecos     |   759362274.8 |     178183023.9 |      1202649.5 |
| gurobi   | 12890168669.6 |  114755681492.7 |  12644995937.7 |
| highs    |       10710.7 |         97221.0 |        10712.6 |
| hpipm    |   241565698.5 |             4.8 |       605733.9 |
| osqp     |  3618509430.8 |             3.3 |       476956.1 |
| piqp     |         195.1 |             2.6 |       239713.8 |
| proxqp   |        1210.9 |             1.0 |        39088.2 |
| qpoases  | 23011750649.4 |  201023358037.0 |  22251703189.3 |
| qpswift  |   676146407.1 |             6.5 |       730158.5 |
| quadprog |   180719102.8 |             5.8 |       188214.0 |
| scs      |    80666615.1 |             2.6 |       210237.9 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a dual residual equal to the full [dual tolerance](#settings).

#### Duality gap

The duality gap measures the consistency of the primal and dual solutions returned by a solver. A duality gap close to zero ensures that the complementarity slackness optimality condition is satisfied. We use the shifted geometric mean to compare solver duality gaps over the whole test set. Intuitively, a solver with a shifted-geometric-mean duality gap of Y is Y times less precise on the complementarity slackness condition than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of duality gaps (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |      10.8 |             3.4 |            1.0 |
| cvxopt   |   11283.6 |       3221384.9 |            5.7 |
| daqp     |     147.5 |       8430005.5 |           12.9 |
| ecos     |   42471.9 |       6231552.4 |            4.4 |
| gurobi   | 1612059.3 |   90789765573.8 |       139251.1 |
| highs    |    3042.0 |     173856845.8 |          266.7 |
| hpipm    |   15006.2 |             2.0 |           38.1 |
| osqp     | 2295466.7 |             2.6 |         2859.0 |
| piqp     |       1.0 |             2.4 |            1.4 |
| proxqp   |    7967.4 |             2.3 |          191.1 |
| qpoases  |   18805.1 |             1.1 |            1.7 |
| qpswift  |   42199.8 |        297175.8 |           44.0 |
| quadprog |   11226.4 |             1.0 |            1.0 |
| scs      |  548544.3 |             1.4 |            1.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a duality gap equal to the full [gap tolerance](#settings).

### Cost error

The cost error measures the difference between the known optimal objective and the objective at the solution returned by a solver. We use the shifted geometric mean to compare solver cost errors over the whole test set. Intuitively, a solver with a shifted-geometric-mean cost error of Y is Y times less precise on the optimal cost than the best solver over the test set. See [Metrics](https://github.com/qpsolvers/qpsolvers_benchmark#metrics) for details.

Shifted geometric means of solver cost errors (1.0 is the best):

|          |   default |   high_accuracy |   low_accuracy |
|:---------|----------:|----------------:|---------------:|
| clarabel |       1.7 |          1333.5 |            1.7 |
| cvxopt   |    3962.0 |          2284.6 |         2247.7 |
| daqp     |       1.0 |           586.3 |            1.0 |
| ecos     |   49754.1 |         28689.7 |        62666.8 |
| gurobi   |    2312.5 |          1333.5 |         2248.5 |
| highs    |       1.7 |             1.0 |            1.7 |
| hpipm    |    6066.8 |         13735.3 |        23164.3 |
| osqp     |   14627.4 |          3498.3 |         2500.4 |
| piqp     |       1.7 |          1332.9 |            1.7 |
| proxqp   |      39.9 |           586.8 |            1.8 |
| qpoases  |   15514.8 |          8946.3 |        15085.7 |
| qpswift  |   49767.5 |         28689.9 |        48410.2 |
| quadprog |    3961.8 |          2284.5 |         3852.2 |
| scs      |    7000.5 |          2284.5 |         2248.6 |

Rows are solvers and columns are solver settings. The shift is $sh = 10$. A solver that fails to find a solution receives a cost error equal to the [cost tolerance](#settings).
