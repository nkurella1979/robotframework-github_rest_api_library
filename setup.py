#####!/usr/bin/env python
from setuptools import setup, find_packages
from version import __VERSION__

setup(
    name = 'robotframework_github_restapi_library',
    version = __VERSION__, # resolved with execfile
    description = 'Robot Framework Github Library for REST API',
    classifiers=[
        'Programming Language :: Python :: 2.x',
        'Programming Language :: Python :: 3.x',
    ],
    author='Narendra Kurella',
    author_email='kurellanarendra@gmail.com',
    url='',
    license='Apache License 2.0',
    keywords='robotframework testing testautomation rest api',
    platforms='any',
	packages=find_packages(),
    install_requires =['robotframework', 'urllib3', 'jinja2', 'jsondiff', 'flatdict'],
    package_data={
        'GithubRestAPILibrary.templates': ['*'],
    },
    include_package_data=True,
)
