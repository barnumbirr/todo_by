#!/usr/bin/env python3

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='todo_by',
    version='1.2.0',
    author='Martin Simon',
    author_email='me@martinsimon.me',
    description=' Runtime lifetimes for comments.',
    url='https://github.com/barnumbirr/todo_by',
    download_url='https://github.com/barnumbirr/todo_by/archive/refs/heads/master.zip',
    packages=['todo_by'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
