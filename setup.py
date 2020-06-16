# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in locator/__init__.py
from locator import __version__ as version

setup(
	name='locator',
	version=version,
	description=' locating business or dealers',
	author='valiantsystems',
	author_email='info@valiantsystems.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
