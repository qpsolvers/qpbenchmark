# SPDX-License-Identifier: Apache-2.0

"""Unit tests for results."""

import unittest

import pandas

from qpbenchmark import Results

from .custom_test_set import CustomTestSet


def make_results(rows) -> Results:
    """Build a Results instance with a hand-crafted results dataframe.

    Args:
        rows: List of row dictionaries with at least the ``solver``,
            ``settings``, ``found`` and metric columns.

    Returns:
        Results instance whose dataframe holds the given rows.
    """
    results = Results(file_path=None, test_set=CustomTestSet())
    results.df = pandas.DataFrame(rows)
    return results


def constant_rows(solver, settings, metric, value, count=3):
    """Return ``count`` rows with a constant metric value for a solver."""
    return [
        {
            "problem": f"p{i}",
            "solver": solver,
            "settings": settings,
            "runtime": 1.0,
            "found": True,
            "primal_residual": value if metric == "primal_residual" else 0.0,
            "dual_residual": value if metric == "dual_residual" else 0.0,
            "duality_gap": value if metric == "duality_gap" else 0.0,
        }
        for i in range(count)
    ]


class TestResults(unittest.TestCase):
    """Test fixutre for the Results class."""

    SETTINGS = "high_accuracy"
    METRIC = "primal_residual"
    SHIFT = 10.0

    # Per-settings tolerance, used both as floor and not-found value:
    TOL = 1e-9

    def _shgeom(self, rows, floor):
        return make_results(rows).get_shgeom_for_metric_and_settings(
            self.METRIC,
            self.SETTINGS,
            shift=self.SHIFT,
            not_found_value=self.TOL,
            floor=floor,
        )

    def test_floor_ignores_precision_beyond_tolerance(self):
        """Two solvers both below tolerance are ranked identically."""
        rows = constant_rows("precise", self.SETTINGS, self.METRIC, 1e-15)
        rows += constant_rows(
            "less_precise", self.SETTINGS, self.METRIC, 1e-11
        )
        means = self._shgeom(rows, floor=self.TOL)
        # Both solve better than asked, so neither is rewarded for it.
        self.assertAlmostEqual(means["precise"], 1.0)
        self.assertAlmostEqual(means["less_precise"], 1.0)
        self.assertEqual(means["precise"], means["less_precise"])

    def test_over_precision_rewarded_without_floor(self):
        """Without the floor, solving beyond tolerance changes the ranking.

        This documents the behavior the floor is meant to fix: a solver that
        goes to machine precision looks arbitrarily better than one that merely
        meets the tolerance.
        """
        rows = constant_rows("precise", self.SETTINGS, self.METRIC, 1e-15)
        rows += constant_rows(
            "less_precise", self.SETTINGS, self.METRIC, 1e-11
        )
        means = self._shgeom(rows, floor=None)
        self.assertNotAlmostEqual(means["precise"], means["less_precise"])
        self.assertGreater(means["less_precise"], means["precise"])

    def test_floor_penalizes_above_tolerance(self):
        """A solver worse than tolerance is penalized proportionally."""
        rows = constant_rows("precise", self.SETTINGS, self.METRIC, 1e-15)
        rows += constant_rows("sloppy", self.SETTINGS, self.METRIC, 1e-3)
        means = self._shgeom(rows, floor=self.TOL)
        self.assertAlmostEqual(means["precise"], 1.0)
        # 1e-3 residual against a 1e-9 floor is 1e6 times the tolerance.
        self.assertAlmostEqual(means["sloppy"] / 1e6, 1.0, places=4)

    def test_floor_yields_positive_finite_means(self):
        """With the floor, means are finite, positive and normalized to >= 1.

        Regression test for the degenerate case where the best solver reaches
        zero residual. An un-floored best mean would then divide by zero.
        """
        rows = constant_rows("precise", self.SETTINGS, self.METRIC, 0.0)
        rows += constant_rows("sloppy", self.SETTINGS, self.METRIC, 1e-2)
        means = self._shgeom(rows, floor=self.TOL)
        for value in means.values():
            self.assertGreater(value, 0.0)
            self.assertTrue(pandas.notna(value))
            self.assertGreaterEqual(round(value, 6), 1.0)

    def test_not_found_is_floored_like_a_solved_tolerance(self):
        """A solver that did not find a solution sits at the tolerance."""
        rows = constant_rows("precise", self.SETTINGS, self.METRIC, 1e-15)
        failed = constant_rows("failed", self.SETTINGS, self.METRIC, 0.0)
        for row in failed:
            row["found"] = False
        means = self._shgeom(rows + failed, floor=self.TOL)
        self.assertAlmostEqual(means["failed"], 1.0)

    def test_build_shgeom_df_with_floors(self):
        """Floors are applied across settings in build_shgeom_df."""
        rows = []
        floors = {}
        not_found = {}
        for settings, tol in [("low_accuracy", 1e-3), ("high_accuracy", 1e-9)]:
            rows += constant_rows("precise", settings, self.METRIC, 1e-15)
            rows += constant_rows("sloppy", settings, self.METRIC, 1e-1)
            floors[settings] = tol
            not_found[settings] = tol
        df = make_results(rows).build_shgeom_df(
            metric=self.METRIC,
            shift=self.SHIFT,
            not_found_values=not_found,
            floors=floors,
        )
        self.assertEqual(sorted(df.index), ["precise", "sloppy"])
        self.assertEqual(sorted(df.columns), ["high_accuracy", "low_accuracy"])
        self.assertTrue((df.to_numpy() > 0.0).all())
        self.assertAlmostEqual(df.loc["precise", "high_accuracy"], 1.0)
        self.assertGreater(
            df.loc["sloppy", "high_accuracy"],
            df.loc["sloppy", "low_accuracy"],
        )


if __name__ == "__main__":
    unittest.main()
