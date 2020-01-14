# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname


with open(join(dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setup(
    name='rockethook',
    version='1.0.4',
    description='Simple library for posting to Rocket.Chat via webhooks a.k.a. integrations.',
    long_description=readme,
    license='MIT',
    author='Baxytra',
    author_email='git@baxytra.eu',
    url='https://github.com/baxytra/rockethook',
    packages=find_packages(exclude=('tests', 'docs'))
)
