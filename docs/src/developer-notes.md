# Developer notes

These notes complement the [contribution guidelines](https://github.com/qpsolvers/qpbenchmark/blob/main/CONTRIBUTING.md) with details for developers working on `qpbenchmark` itself.

## Development environment

The repository uses [pixi](https://pixi.sh) to manage environments and tasks:

| Command | Description |
|:--------|:------------|
| `pixi run test` | Run unit tests |
| `pixi run coverage` | Run unit tests with a coverage report |
| `pixi run lint` | Check formatting, lint with ruff and type-check with mypy |
| `pixi run format` | Format source code with ruff |
| `pixi run -e py39 test` | Run unit tests on a given Python version (`py39` to `py312`) |
| `pixi run qpbenchmark --test-set my_test_set.py run` | Run the benchmark with all solvers of the `solvers` environment |
| `pixi run docs-serve` | Serve this website locally, with live reload |

## Working on qpbenchmark and a test set together

Test sets are separate repositories that depend on the `qpbenchmark` package. Their `pixi.toml` gets it from PyPI:

```toml
[pypi-dependencies]
qpbenchmark = ">=3.0.0"
```

When a change spans both repositories, for instance a new benchmark feature and the test-set results that use it, point the test set to your development version of `qpbenchmark` instead. Either use a local clone, installed in editable mode so that your changes apply without reinstalling:

```toml
[pypi-dependencies]
qpbenchmark = { path = "../qpbenchmark", editable = true }
```

Or use a branch from a Git repository, for instance from your fork:

```toml
[pypi-dependencies]
qpbenchmark = { git = "https://github.com/your-username/qpbenchmark.git", branch = "your-branch" }
```

Note that we use `qpbenchmark` as a Python package from PyPI, with its source going under `[pypi-dependencies]` rather than under `[dependencies]`. 

Don't forget to revert to a released version, *e.g.* `qpbenchmark = ">=2.8.0"`, before merging changes to the test set.
