#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 inria
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

"""Test sets of the benchmark."""


from .maros_meszaros import MarosMeszaros
from .maros_meszaros_dense import maros_meszaros_dense
from .maros_meszaros_dense_posdef import maros_meszaros_dense_posdef
from .problem import problem

__all__ = [
    "MarosMeszaros",
    "maros_meszaros_dense",
    "maros_meszaros_dense_posdef",
    "problem",
]
