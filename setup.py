#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup_requirements = ['pytest-runner',]

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Fixture "data" and "case_data" for test from yaml file',
    long_description='Session scope fixture "data" for test from yaml file, '
                     'and function scope "case_data" for this test function',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'data', 'file', 'yaml'
    ],
    name='pytest-data-file',
    packages=find_packages(include=['pytest_data_file']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-data-file',
    version='0.1',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner',
        'pyyaml'
    ],
    entry_points={
        'pytest11': [
            'pytest-data-file = pytest_data_file.plugin',
        ]
    }
)
