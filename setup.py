#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from setuptools import setup, find_packages

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

here = os.path.abspath(os.path.dirname(__file__))

# put package test requirements here
requirements = [
    "sh",
    "requests",
    "PyYaml",
    "colorlog",
    "werkzeug",
    "json-rpc",
]

# put package test requirements here
test_requirements = []

setup(
    name='stackhut-common',
    version='0.5.6',
    description="Run your software in the cloud",
    long_description=(read('README.rst') + '\n\n' +
                      read('AUTHORS.rst')),
    license='Apache',
    author="StackHut",
    author_email='stackhut@stackhut.com',
    url='https://github.com/stackhut/stackhut-common',
    # download_url = 'https://github.com/stackhut/stackhut-tool/tarball/0.1.0'
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", ""]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
    keywords='stackhut',
    platforms=['POSIX'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
        # 'Private :: Do Not Upload',  # hack to force invalid package for upload
    ],
)

