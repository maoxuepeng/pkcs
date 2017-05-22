#!/usr/bin/env python
# coding=utf8

from setuptools import setup, find_packages

setup(
    name="pkcs",
    version="0.1.1",
    keywords=("pip", "python", "pkcs", "openssl", "x509", "certificate", "ca", "self sign"),
    description="pkcs tool set",
    long_description="pkcs tool set for manipulating pkcs file",
    license="Apache License",

    url="http://yunweipai.com",
    author="Mao",
    author_email="maoxuepeng@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[""],

    scripts=[],
    entry_points={
        'console_scripts': [
            'pkcs = pkcs.pkcs:main'
        ]
    }
)