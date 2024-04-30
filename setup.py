from setuptools import setup, find_packages, Extension
import os

classifiers = [
    "Development Status :: 1 - Pre-Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Earth and Environmental Sciences"
    ]

with open("README.rst", "r") as fp:
    long_description = fp.read()

setup(
    name="pywx",
    version="0.0.0",
    author="Junjie Yu",
    author_email="yjj1997@live.cn",
    url="https://github.com/JunjieYU-UoM/pywx",
    description="A Python package for obtaining observational meteorology data",
    long_description=long_description,
    license="MIT",
    classifiers=classifiers,
    install_requires=['pandas', 'geopy'],
    packages=find_packages(),
    )