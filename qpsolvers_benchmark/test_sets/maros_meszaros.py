#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Maros-Meszaros test set.
"""

import json
import os.path
from typing import Dict, Iterator, Optional, Union

import numpy as np
import scipy.io as spio
import scipy.sparse as spa

from ..problem import Problem
from ..solver_settings import SolverSettings
from ..test_set import TestSet
from ..tolerance import Tolerance


class MarosMeszaros(TestSet):

    """
    Maros-Meszaros QP test set, a standard set of problems designed to be
    difficult.
    """

    data_dir: str
    optimal_costs: Dict[str, float]

    @property
    def description(self) -> Optional[str]:
        """
        No description for this test set.
        """
        return None

    @property
    def title(self) -> str:
        """
        Test set title.
        """
        return "Maros-Meszaros test set"

    @property
    def sparse_only(self) -> bool:
        """
        This test set is sparse.
        """
        return True

    def define_tolerances(self) -> None:
        """
        Define test set tolerances.
        """
        self.tolerances = {
            "default": Tolerance(
                cost=1000.0,
                primal=1.0,
                dual=1.0,
                gap=1.0,
                runtime=1000.0,
            ),
            "low_accuracy": Tolerance(
                cost=1000.0,
                primal=1e-3,
                dual=1e-3,
                gap=1e-3,
                runtime=1000.0,
            ),
            "high_accuracy": Tolerance(
                cost=1000.0,
                primal=1e-9,
                dual=1e-9,
                gap=1e-9,
                runtime=1000.0,
            ),
        }

    def define_solver_settings(self) -> None:
        """
        Define solver settings.
        """
        default = SolverSettings()
        default.set_time_limit(self.tolerances["default"].runtime)

        low_accuracy = SolverSettings()
        low_accuracy.set_time_limit(self.tolerances["low_accuracy"].runtime)
        low_accuracy.set_eps_abs(1e-3)
        low_accuracy.set_eps_rel(0.0)

        high_accuracy = SolverSettings()
        high_accuracy.set_time_limit(self.tolerances["high_accuracy"].runtime)
        high_accuracy.set_eps_abs(1e-9)
        high_accuracy.set_eps_rel(0.0)

        self.solver_settings = {
            "default": default,
            "low_accuracy": low_accuracy,
            "high_accuracy": high_accuracy,
        }

    def __init__(self, data_dir: str):
        """
        Initialize test set.

        Args:
            data_dir: Path to the benchmark data directory.
        """
        super().__init__()
        data_dir = os.path.join(data_dir, "maros_meszaros")
        cost_path = os.path.join(data_dir, "OPTCOSTS.json")
        with open(cost_path, "rb") as fh:
            file_dict = json.load(fh)
            optimal_costs = {k: float(v) for k, v in file_dict.items()}
        self.data_dir = data_dir
        self.optimal_costs = optimal_costs

    def load_problem_from_mat_file(self, path):
        """
        Load problem from MAT file.

        Args:
            path: Path to file.

        Notes:
            We assume that matrix files result from calling `sif2mat.m` in
            proxqp_benchmark. In particular, ``A = [sparse(A_c); speye(n)];``
            and the infinity constant is set to 1e20.
        """
        assert path.endswith(".mat")
        name = os.path.basename(path)[:-4]

        mat_dict = spio.loadmat(path)
        P = mat_dict["P"].astype(float).tocsc()
        q = mat_dict["q"].T.flatten().astype(float)
        r = mat_dict["r"].T.flatten().astype(float)[0]
        A = mat_dict["A"].astype(float).tocsc()
        l = mat_dict["l"].T.flatten().astype(float)
        u = mat_dict["u"].T.flatten().astype(float)
        n = mat_dict["n"].T.flatten().astype(int)[0]
        m = mat_dict["m"].T.flatten().astype(int)[0]
        assert A.shape == (m, n)

        # Infinity constant is 1e20
        A[A > +9e19] = +np.inf
        l[l > +9e19] = +np.inf
        u[u > +9e19] = +np.inf
        A[A < -9e19] = -np.inf
        l[l < -9e19] = -np.inf
        u[u < -9e19] = -np.inf

        # A = vstack([C, spa.eye(n)])
        lb = l[-n:]
        ub = u[-n:]
        C = A[:-n]
        l_c = l[:-n]
        u_c = u[:-n]

        return self.convert_problem_from_double_sided(
            P, q, C, l_c, u_c, lb, ub, name=name, cost_offset=r
        )

    @staticmethod
    def convert_problem_from_double_sided(
        P: Union[np.ndarray, spa.csc_matrix],
        q: np.ndarray,
        C: Union[np.ndarray, spa.csc_matrix],
        l: np.ndarray,
        u: np.ndarray,
        lb: np.ndarray,
        ub: np.ndarray,
        name: str,
        cost_offset: float = 0.0,
    ):
        """
        Load problem from double-sided inequality format:

        .. code::

            minimize        0.5 x^T P x + q^T x + cost_offset
            subject to      l <= C x <= u
                            lb <= x <= ub

        Args:
            P: Cost matrix.
            q: Cost vector.
            C: Constraint inequality matrix.
            l: Constraint lower bound.
            u: Constraint upper bound.
            lb: Box lower bound.
            ub: Box upper bound.
            name: Problem name.
            cost_offset: Cost offset.
        """
        bounds_are_equal = u - l < 1e-10

        eq_rows = np.asarray(bounds_are_equal).nonzero()
        A = C[eq_rows]
        b = u[eq_rows]

        ineq_rows = np.asarray(np.logical_not(bounds_are_equal)).nonzero()
        G = spa.vstack([C[ineq_rows], -C[ineq_rows]], format="csc")
        h = np.hstack([u[ineq_rows], -l[ineq_rows]])
        h_finite = h < np.inf
        if not h_finite.all():
            G = G[h_finite]
            h = h[h_finite]

        return Problem(
            P,
            q,
            G if G.size > 0 else None,
            h if h.size > 0 else None,
            A if A.size > 0 else None,
            b if b.size > 0 else None,
            lb,
            ub,
            name=name,
            cost_offset=cost_offset,
        )

    def __iter__(self) -> Iterator[Problem]:
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".mat"):
                mat_path = os.path.join(self.data_dir, fname)
                problem = self.load_problem_from_mat_file(mat_path)
                if problem.name in self.optimal_costs:
                    problem.optimal_cost = self.optimal_costs[problem.name]
                yield problem
