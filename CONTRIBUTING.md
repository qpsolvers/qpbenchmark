# 👷 Contributing

This project's goal is to facilitate the comparison of quadratic programming solvers for the community of solver users. All contributions are welcome, for example here are some ways to help:

- [Add a solver to the benchmark](#add-a-solver-to-the-benchmark)
- [Submit a new problem](https://github.com/qpsolvers/qpbenchmark/issues/new?template=new_problem.md), *e.g.* one that reflects an application you are working on.
- [Create a new test set](#creating-a-new-test-set), distribute it in its own repository, and open a PR to reference it here

## Add a solver to the benchmark

- Add a corresponding entry (in the Added section of the upcoming version) to the changelog
- Add the solver name to the `IMPLEMENTED_SOLVERS` list in `solver_settings.py`
- Add the solver to `environment.yaml` (update the version of `qpsolvers` if applicable)
- Add the solver to the Solvers table in the readme
- Set any other relevant solver settings in the `define_solver_settings` function in `test_set.py`
- Set the solver's absolute tolerance in the `set_eps_abs` function in `solver_settings.py`
- Set the solver's relative tolerance (if applicable) in the `set_eps_rel` function in `solver_settings.py`
- Set the solver's time limit (if applicable) in the `set_time_limit` function in `solver_settings.py`

## Creating a new test set

- Create a new repository for your test set
- Add a main Python file named after the test set, say ``foo_bar.py``
- Implement a `FooBar` class in this file deriving from `qpbenchmark.TestCase`
    - The class name should match the file name in PascalCase)

Check out how this is done in *e.g.* the [Maros-Meszaros test set](https://github.com/qpsolvers/maros_meszaros_qpbenchmark).
