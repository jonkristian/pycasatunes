#!/usr/bin/env python
import io
from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="pycasatunes",
    version=version,
    description="Asynchronous python client for CasaTunes.",
    long_description=io.open("README.md", encoding="UTF-8").read(),
    keywords="casatunes multi-room audio",
    author="Jon Kristian Nilsen (jonkristian)",
    author_email="hello@jonkristian.no",
    license="MIT",
    url="https://github.com/jonkristian/pycasatunes",
    packages=find_packages(exclude=["tests", "generator"]),
    install_requires=["aiohttp>=3.7.4"],
)
