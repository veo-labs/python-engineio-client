# -*- coding: utf-8 -*-
"""
python-engineio-client
----------------------

Engine.IO client.
"""
from setuptools import setup

setup(
    name='python-engineio-client',
    version='0.1',
    url='http://github.com/veo-labs/python-engineio-client/',
    license='MIT',
    author='Frédéric Sureau',
    author_email='frederic.sureau@veo-labs.com',
    description='Engine.IO client',
    long_description=open('README.rst').read(),
    packages=['engineio_client', 'engineio_client.transports'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'six>=1.9.0',
        'requests>=2.9.1',
        'gevent>=1.0.2',
        'websocket-client==0.47.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

