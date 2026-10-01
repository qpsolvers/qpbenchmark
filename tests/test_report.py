# SPDX-License-Identifier: Apache-2.0

"""Unit tests for report generation."""

import unittest

from qpbenchmark import Report, Results

from .custom_test_set import CustomTestSet


class TestReport(unittest.TestCase):
    """Test fixture for the Report class."""

    def setUp(self):
        """Create a report from empty results."""
        self.results = Results(file_path=None, test_set=CustomTestSet())
        self.report = Report(author="foobar", results=self.results)

    def test_author(self):
        """Report keeps the author it was created with."""
        self.assertEqual(self.report.author, "foobar")
