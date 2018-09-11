#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name='comparator',
    version='0.1.0',
    author='Aaron Biller',
    author_email='aaronbiller@gmail.com',
    description='Utility for comparing results between data sources',
    license='Apache 2.0',
    keywords='utility compare database',
    url='https://github.com/aaronbiller/comparator',
    packages=find_packages(),
    tests_require=[
        'pytest',
        'pytest-cov',
        'mock',
    ],
    install_requires=[
        'future==0.16.0',
        'google-cloud-bigquery==1.5.0',
        'psycopg2-binary==2.7.5',
        'PyYAML',
        'SQLAlchemy==1.2.11',
        'sqlalchemy-redshift==0.7.1',
        'pytest-runner==4.2',
    ],
    extras_require={
        ':python_version == "2.7"': [
            'pathlib2==2.3.2',
        ],
    },
    include_package_data=True,
    scripts=[],
    classifiers=[
        'Topic :: Database',
        'Topic :: Utilities',
    ],
)
