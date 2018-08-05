# -*- coding: utf8 -*-
from distutils.core import setup

setup(
    name='dstream',
    version='0.0.3',
    description='An experimental Java-8-stream-like lib.',
    long_description=open('README.rst').read(),
    author='manxisuo',
    author_email='manxisuo@gmail.com',
    platforms=["all"],
    url='https://github.com/manxisuo/dstream',
    package_dir={'dstream': 'src'},
    packages=['dstream'])
