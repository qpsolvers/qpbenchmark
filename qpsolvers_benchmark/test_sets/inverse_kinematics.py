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
Inverse kinematics test set.
"""

from copy import deepcopy
from dataclasses import dataclass
from typing import Dict, Iterator, List

from qpsolvers import available_solvers

from ..problem import Problem
from ..solver_settings import SolverSettings
from ..test_set import TestSet
from ..tolerance import Tolerance

try:
    from robot_descriptions.loaders.pinocchio import load_robot_description
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "This test set requires 'robot_descriptions', "
        "which can be installed by ``pip install robot_descriptions``"
    ) from e

try:
    import pink
    from pink import solve_ik
    from pink.tasks import BodyTask, PostureTask, Task
    from pink.utils import RateLimiter, custom_configuration_vector
    from pink.visualization import start_meshcat_visualizer
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "This test set requires 'pink', "
        "which can be installed by ``pip install pin-pink``"
    ) from e


@dataclass
class Scenario:
    name: str
    robot_description: str
    posture: Dict[str, float]
    tasks: List[Task]


SCENARIOS = [
    Scenario(
        name="upkie_knee_flexing",
        robot_description="upkie_description",
        posture={
            "left_hip": -0.2,
            "left_knee": 0.4,
            "right_hip": 0.2,
            "right_knee": -0.4,
        },
        tasks=[
            BodyTask(
                "base",
                position_cost=1.0,  # [cost] / [m]
                orientation_cost=1.0,  # [cost] / [rad]
            ),
            BodyTask(
                "left_contact",
                position_cost=[0.1, 0.0, 0.1],  # [cost] / [m]
                orientation_cost=0.0,  # [cost] / [rad]
            ),
            BodyTask(
                "right_contact",
                position_cost=[0.1, 0.0, 0.1],  # [cost] / [m]
                orientation_cost=0.0,  # [cost] / [rad]
            ),
            PostureTask(
                cost=1e-3,  # [cost] / [rad]
            ),
        ],
    )
]


class Scene:
    def __init__(self, scenario: Scenario):
        robot = load_robot_description(scenario.robot_description)
        posture = custom_configuration_vector(robot, **scenario.posture)
        tasks = deepcopy(scenario.tasks)

        configuration = pink.apply_configuration(robot, posture)
        for task in tasks:
            if isinstance(task, BodyTask):
                task.set_target_from_configuration(configuration)
            elif isinstance(task, PostureTask):
                task.set_target(posture)

        self.configuration = configuration
        self.robot = robot
        self.tasks = tasks

    def display(self):
        viz = start_meshcat_visualizer(self.robot)
        viz.display(self.configuration.q)
        rate = RateLimiter(frequency=200.0)
        dt = rate.period
        t = 0.0  # [s]
        while True:
            # Compute velocity and integrate it into next configuration
            solver = available_solvers[0]
            if "quadprog" in available_solvers:
                solver = "quadprog"
            velocity = solve_ik(
                self.configuration, self.tasks, dt, solver=solver
            )
            q = self.configuration.integrate(velocity, dt)
            self.configuration = pink.apply_configuration(self.robot, q)

            # Visualize result at fixed FPS
            viz.display(q)
            rate.sleep()
            t += dt


class InverseKinematics(TestSet):
    @property
    def title(self) -> str:
        return "Inverse kinematics test set"

    @property
    def sparse_only(self) -> bool:
        return False

    def define_tolerances(self) -> None:
        self.tolerances = {
            "default": Tolerance(
                cost=1000.0,
                primal=1e-2,
                runtime=1.0,
            ),
        }

    def define_solver_settings(self) -> None:
        default = SolverSettings()
        default.set_time_limit(self.tolerances["default"].runtime)

        self.solver_settings = {
            "default": default,
        }

    def __iter__(self) -> Iterator[Problem]:
        for scenario in SCENARIOS:
            scene = Scene(scenario)
            scene.display()
