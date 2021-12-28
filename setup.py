#!/usr/bin/env python3

from setuptools import setup

setup(
  name='diceware',
  version='1',
  description='Secure password generator',
  author='Douglas Maieski',
  url='https://github.com/cmovz/diceware-password-generator',
  packages=['diceware'],
  package_data={'diceware': ['words.txt']},
  entry_points={
    'console_scripts': [
      'diceware = diceware.diceware:main',
    ],
  },
  license='BSD',
  zip_safe=False,
)