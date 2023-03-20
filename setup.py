"""Setup file for installing dependencies for mibilib.

Copyright (C) 2022 Ionpath, Inc.  All rights reserved."""

from setuptools import setup

setup(
    name="mibilib",
    author="IONpath, Inc.",
    author_email="support@ionpath.com",
    version="1.5.0",
    url="https://github.com/ionpath/mibilib",
    description="Python utilities for IONpath MIBItracker and MIBItiff data",
    license="GNU General Public License v3.0",
    python_requires=">=3.11",
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
        "pillow",
        "requests",
        "scikit-image",
        "scikit-learn",
        "tifffile",
        "tqdm",
    ],
    packages=["mibitracker", "mibidata"],
)
