#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
from garbevents import __version__

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="garbevents",
    version=__version__,
    keywords=["pip", "garbevents", "zhugeio", "buried points", "sensors", "argo", "growingio"],
    description="grabbing buried points tools.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT Licence",

    url="https://github.com/Pactortester/garbevents",
    author="lijiawei",
    author_email="1456470136@qq.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Software Development :: Testing",
        "Typing :: Typed",
    ],
    entry_points="""
    [console_scripts]
    gb = garbevents.cli.main:main
    """,

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["mitmproxy", "jsonpath", "paramiko", "emoji"]
)
