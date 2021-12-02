from setuptools import find_packages
from setuptools import setup

from aoc_dan import __doc__
from aoc_dan import __version__


setup(
    name="advent-of-code-dan",
    version=__version__,
    description=__doc__,
    url="https://github.com/ddugovic/advent-of-code-2021",
    author="Daniel Dugovic",
    author_email="ddugovic@users.noreply.github.com",
    license="GPLv3",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.9.8",
        "anytree",
        "bidict",
        "numpy",
        "parse",
        "scipy",
        "sympy",
        "fields",
        "networkx",
        "wimpy",
        "marshmallow",
        "regex",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["dan = aoc_dan:plugin"],
        "console_scripts": [
            "aocw = aoc_dan.cli:run_one",
            "s = aoc_dan.cli:speedhack",
            "_set_docstrings = aoc_dan.util:set_docstrings",
            "aoc-init = aoc_dan.util:start",
        ],
    },
)
