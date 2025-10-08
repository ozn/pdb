"""
Setup script for the ArtW project.

This file defines a minimal setuptools configuration.  Modify as needed to
specify package metadata and dependencies.
"""

from setuptools import setup, find_packages


setup(
    name="artw",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        "console_scripts": [
            "artw=main:main",  # assuming main.py defines a main() function
        ],
    },
)
