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
import logging
import platform

from .utils import bool_as_emoji

try:
    import cpuinfo
except ImportError:
    cpuinfo = None
    logging.warn("Run ``pip install py-cpuinfo`` for a more CPU info")


class Report:
    def __init__(self):
        """
        Initialize report written to file.

        Args:
            fname: File to write report to.
        """
        self.cpu_info = (
            platform.processor()
            if cpuinfo is None
            else cpuinfo.get_cpu_info()["brand_raw"]
        )
        self.datetime = str(datetime.datetime.now(datetime.timezone.utc))

    def title(self, title: str) -> None:
        """
        Set report title.

        Args:
            title: Report title.
        """
        self.__title = title

    def write(self, results, fname: str) -> None:
        with open(fname, "w") as output:
            output.write(
                f"""# {self.__title}

- Date: {self.datetime}
- CPU: {self.cpu_info}
"""
            )

            output.write("\n\n")
            output.write("## Finding solutions\n\n")

            found_df = results.build_found_df()
            found_table = found_df.to_markdown(index=True)
            found_table = found_table.replace(
                "False", bool_as_emoji(False) + " " * 3
            )
            found_table = found_table.replace(
                "True", bool_as_emoji(True) + " " * 3
            )
            output.write(found_table)
