#!/usr/bin/env python
from os.path import join, dirname
from setuptools import setup, find_packages

from settings import __version__

def long_description():
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return ''

setup(
    name='djlime-settings',
    author='Andrey Butenko',
    author_email='whitespysoftware@yandex.ru',
    url='https://github.com/whitespy/djlime-settings',
    description='The application settings.',
    long_description=long_description(),
    version = __version__,
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=['Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License']
)
