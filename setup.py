# -*- coding: utf-8 -*-
"""
Flask-Realtime-Import
-------------

import the modules in every request if you need
"""

from setuptools import setup

setup(
    name='Flask-Realtime-Import',
    version='0.0.1.dev0',
    url='https://github.com/caimaoy/flask-realtime-import',
    license='BSD',
    author='caimaoy',
    keywords=['flask', 'realtime', 'import'],
    author_email='i@caimaoy.com',
    description='import the modules in every request',
    long_description=__doc__,
    py_modules=['flask_realtime_import'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask_realtime_import'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask>0.8'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ])
