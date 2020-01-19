"""Setup for the ac_transit package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Ira Horecka",
    author_email="ira89@icloud.com",
    name='ac_transit',
    license="MIT",
    description='ac_transit is a python package for querying data from the AC Transit API.',
    version='v0.0.2',
    long_description=README,
    url='https://github.com/irahorecka/python-ac-transit',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests', 'gtfs-realtime-bindings', 'protobuf3-to-dict'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)