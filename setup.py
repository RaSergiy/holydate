# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='holydate',
    version=__import__('holydate').__version__,
    author='Maxim Chernyatevich',
    author_email='vechnoe.info@gmail.com',
    packages=['holydate'],
    url='https://github.com/vechnoe/holydate/',
    license='GNU General Public License v3 or later',
    description=read('DESCRIPTION'),
    keywords="calendar easter menology",
    long_description=open('README.rst').read(),
    include_package_data=True,
    entry_points='''\
    [console_scripts]
    holydate = holydate.cli:main
    ''',
    package_data = {'': ['README.rst']},
    install_requires=['pytils'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Religion',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: Russian',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Religion'
    ]
)