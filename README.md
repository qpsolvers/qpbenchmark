# qpsolvers benchmark

Benchmark for quadratic programming solvers available in Python.

## Results

...

## Running the benchmark

To run the benchmark on your machine, you will first need to install [qpsolvers](https://github.com/stephane-caron/qpsolvers) along with solvers you want to test. For instance, to install a base set of open source solvers:

```console
$ pip install qpsolvers[open_source_solvers]
```

Then, run the benchmark by:

```console
$ python run_benchmark.py
```

## Design

### Validation

...

## See also

- [OSQP paper](https://arxiv.org/pdf/1711.08013.pdf) where the validation process was proposed
- [jrl-qp/benchmarks](https://github.com/jrl-umi3218/jrl-qp/tree/master/benchmarks)
- [proxqp\_benchmark](https://github.com/Simple-Robotics/proxqp_benchmark)
