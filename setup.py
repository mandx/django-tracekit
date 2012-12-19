#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-tracekit',
    version='0.1-alpha',
    description='Integrate TraceKit with your Django site (https://github.com/occ/TraceKit)',
    author='Armando Pérez',
    author_email='gmandx@gmail.com',
    url='https://github.com/mandx/django-tracekit',
    packages=[
        'tracekit',
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Javascript',
        'Topic :: Debugging',
        'Topic :: Utilities',
    ],
)
