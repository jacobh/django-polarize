#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-polarize',
    version='0.1.0',
    description='Generic ratings app for Django',
    author='Jacob Haslehurst',
    author_email='jacob@haslehurst.net',
    url='https://github.com/hzy/django-polarize',
    packages=find_packages(exclude=['tests']),
    install_requires=['django', 'south']
)
