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

"""GitHub free-for-all test set problems."""

from .ghffa01 import problems as ghffa01_problems
from .ghffa02 import problems as ghffa02_problems
from .ghffa03 import problems as ghffa03_problems

github_ffa_problems = []
github_ffa_problems.extend(ghffa01_problems)
github_ffa_problems.extend(ghffa02_problems)
github_ffa_problems.extend(ghffa03_problems)

__all__ = [
    "github_ffa_problems",
]
