#!/usr/bin/env python
# coding: utf-8

from distribute_setup import use_setuptools
use_setuptools()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='mockito',
      version='0.5.2',
      packages=['mockito', 'mockito_test', 'mockito_util'],
      url='https://github.com/kaste/mockito-python',
      maintainer='herr.kaste',
      maintainer_email='herr.kaste@gmail.com',
      license='MIT',
      description='Spying framework',
      long_description='Mockito is a spying framework based on the Java '
                       'library with the same name.',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Testing',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      test_suite='nose.collector',
      py_modules=['distribute_setup'],
      setup_requires=['nose'],
      **extra)

