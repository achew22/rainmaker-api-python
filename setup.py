#!/usr/bin/python
from setuptools import setup

setup(
    name                = "rainmaker",
    version             = "0.1",
    author              = "Andrew Allen",
    author_email        = "rainmaker@achew22.com",
    description         = "A rainmaker client",
    long_description    = file("README").read().strip(),
    platforms           = [ 'any' ],
    license             = "MIT",
    url                 = "https://github.com/achew22/rainmaker-api-python",

    package_dir={'': 'rainmaker'},
    py_modules=[
        'rainmaker',
    ],
)
