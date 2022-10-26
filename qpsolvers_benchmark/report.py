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
Benchmark report generator.
"""

import datetime
import platform

CPU_INFO = platform.processor()

try:
    import cpuinfo

    CPU_INFO = cpuinfo.get_cpu_info()["brand_raw"]
except ImportError:
    pass


class Report:
    def __init__(self, fname: str):
        """
        Initialize report written to file.

        Args:
            fname: File to write report to.
        """
        self.output = open(fname, "w")

    def start(self):
        self.output.write(
            f"""# Benchmark

- Date: {str(datetime.datetime.now(datetime.timezone.utc))}
- CPU: {CPU_INFO}
"""
        )

    def finalize(self):
        pass
