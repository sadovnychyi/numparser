#!/usr/bin/env python

import distribute_setup
# User may not have setuptools installed on their machines.
# This script will automatically install the right version from PyPI.
distribute_setup.use_setuptools()
import setuptools

setuptools.setup(
  name='numparser',
  packages=setuptools.find_packages(),
  description='Python library for parsing numbers from strings.',
  long_description='''Python library for parsing numbers from strings.
Originally meant to be used to process results from Named Entity Recognizer.
For more description visit https://github.com/sadovnychyi/numparser''',
  version='0.0.1',
  url='https://github.com/sadovnychyi/numparser',
  author='Dmitry Sadovnychyi',
  author_email='numparser@dmit.ro',
  license='GNU General Public License v2.0',
  keywords=['numbers', 'parser', 'num', 'digits', 'digit'],
  classifiers=[
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Development Status :: 5 - Production/Stable',
    'Natural Language :: English',
    "Topic :: Software Development :: Libraries :: Python Modules",
    'Topic :: Text Processing :: Linguistic',
  ]
)
