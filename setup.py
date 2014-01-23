# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='holydate',
    version='0.1',
    author='Maxim Chernyatevich',
    author_email='vechnoe.info@gmail.com',
    packages=['holydate'],
    url='https://github.com/vechnoe/holydate/',
    license='GNU General Public License v3 or later',
    description=('This package represents the ancient '
                 'Orthodox calendar for oldbeliever.'),
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    entry_points='''\
    [console_scripts]
    holydate = holydate:main
    ''',
    package_data = {'': ['README.rst']},
    install_requires=['pytils'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Religion',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: Russian',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Religion'
    ]
)