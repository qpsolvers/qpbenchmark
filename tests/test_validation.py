#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2022 Stéphane Caron and the qpsolvers contributors.
#
# This file is part of qpsolvers.
#
# qpsolvers is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# qpsolvers is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with qpsolvers. If not, see <http://www.gnu.org/licenses/>.

import os.path
import unittest

from qpsolvers_benchmark import Problem, is_valid_primal_solution


class TestValidation(unittest.TestCase):
    def setUp(self):
        path = os.path.join(os.path.dirname(__file__), "CVXQP1_S.mat")
        self.problem = Problem.from_mat_file(path)

    def test_primal_validation(self):
        primal_solution = self.problem.solve("osqp", eps_abs=1e-5, eps_rel=0)
        self.assertTrue(
            is_valid_primal_solution(
                self.problem, primal_solution, eps_abs=1e-5
            )
        )
