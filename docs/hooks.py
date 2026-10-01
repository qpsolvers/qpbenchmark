# SPDX-License-Identifier: Apache-2.0

"""MkDocs hooks generating the website from the readme and test-set reports."""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.livereload import LiveReloadServer
from mkdocs.structure.files import File, Files

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
TEST_SETS = ROOT / "test_sets"

# Markdown links whose target is neither absolute nor an anchor
RELATIVE_LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")

# Inline math such as $Y$ or $sh = 10$, as rendered by GitHub
INLINE_MATH = re.compile(r"(?<![\\$\w])\$(?=\S)([^$\n]+?)(?<=\S)\$(?![$\w])")

# Inline code spans, in which dollar signs are literal
CODE_SPAN = re.compile(r"(`+).+?\1")


@dataclass
class Report:
    """Benchmark report of a test set or one of its subsets.

    Attributes:
        path: Path to the Markdown report.
        uri: Path of the generated page in the website.
        title: Title of the report, read from its first heading.
    """

    path: Path
    uri: str
    title: str


@dataclass
class TestSetReports:
    """Main report of a test set and reports of its subsets."""

    main: Report
    subsets: List[Report]


def read_title(path: Path) -> str:
    """Read the title of a Markdown file from its first heading.

    Args:
        path: Path to the Markdown file.

    Returns:
        Title of the file.
    """
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("# "):
                return line[2:].strip()
    return path.stem


def find_test_sets() -> List[TestSetReports]:
    """Find reports from all test sets in the `test_sets/` directory.

    Returns:
        Reports of each test set, sorted by test-set directory name.

    Raises:
        ValueError: if a test set has no report, or if no report name
            prefixes all others.
    """
    test_sets = []
    for repo in sorted(TEST_SETS.iterdir()):
        if not repo.is_dir():
            continue
        names = sorted(
            script.stem
            for script in repo.glob("*.py")
            if (repo / "results" / f"{script.stem}.md").exists()
        )
        if not names:
            raise ValueError(
                f"no report found in '{repo}': is the submodule checked out?"
            )
        main_name = min(names, key=len)
        if not all(name.startswith(main_name) for name in names):
            raise ValueError(
                f"no main report in '{repo}': report names are {names}"
            )

        def make_report(name: str) -> Report:
            path = repo / "results" / f"{name}.md"
            suffix = name[len(main_name) :].strip("_")
            page = suffix if suffix else "index"
            uri = f"{repo.name}/{page}.md"
            return Report(path=path, uri=uri, title=read_title(path))

        test_sets.append(
            TestSetReports(
                main=make_report(main_name),
                subsets=[
                    make_report(name) for name in names if name != main_name
                ],
            )
        )
    return test_sets


def italicize_inline_math(markdown: str) -> str:
    """Render inline math as italics, outside of code blocks and spans.

    Our pages only have a few short expressions such as $Y$ or $sh = 10$, for
    which italics are enough and spare loading a math rendering library.

    Args:
        markdown: Markdown source of a page.

    Returns:
        Markdown source with inline math in italics.
    """
    lines = markdown.split("\n")
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        if in_fence or "$" not in line:
            continue
        parts = []
        last = 0
        for code in CODE_SPAN.finditer(line):
            parts.append(INLINE_MATH.sub(r"*\1*", line[last : code.start()]))
            parts.append(code.group(0))
            last = code.end()
        parts.append(INLINE_MATH.sub(r"*\1*", line[last:]))
        lines[i] = "".join(parts)
    return "\n".join(lines)


def on_config(config: MkDocsConfig) -> MkDocsConfig:
    """Build the navigation menu from the test sets.

    Args:
        config: MkDocs configuration.

    Returns:
        Updated configuration.
    """
    test_sets = []
    for test_set in find_test_sets():
        section = [test_set.main.uri]
        section.extend(subset.uri for subset in test_set.subsets)
        # Titles are listed under "Test sets" in the menu, so we drop the
        # redundant suffix, e.g. "Free-for-all test set" -> "Free-for-all"
        title = re.sub(r"\s+test set$", "", test_set.main.title, flags=re.I)
        test_sets.append({title: section})
    config.nav = [
        "index.md",
        {"Test sets": test_sets},
        {"Development": ["api.md", "developer-notes.md"]},
    ]
    return config


def on_files(files: Files, config: MkDocsConfig) -> Files:
    """Add the readme and test-set reports to the website.

    Args:
        files: Files of the website.
        config: MkDocs configuration.

    Returns:
        Updated files.
    """
    repo_url = config.repo_url.rstrip("/")
    readme = README.read_text(encoding="utf-8")
    readme = RELATIVE_LINK.sub(
        lambda match: f"]({repo_url}/blob/main/{match.group(1)})", readme
    )
    files.append(File.generated(config, "index.md", content=readme))
    for test_set in find_test_sets():
        for report in [test_set.main] + test_set.subsets:
            files.append(
                File.generated(config, report.uri, abs_src_path=report.path)
            )
    return files


def on_page_markdown(markdown: str, **kwargs) -> str:
    """Process the Markdown source of each page.

    Args:
        markdown: Markdown source of the page.
        kwargs: Page, configuration and files of the website.

    Returns:
        Processed Markdown source.
    """
    return italicize_inline_math(markdown)


def on_serve(server: LiveReloadServer, config: MkDocsConfig, builder):
    """Rebuild the website when the readme or test-set reports change.

    Args:
        server: Live-reload server.
        config: MkDocs configuration.
        builder: Function rebuilding the website.

    Returns:
        Live-reload server.
    """
    server.watch(str(README))
    for path in TEST_SETS.glob("*/results/*.md"):
        server.watch(str(path))
    return server
