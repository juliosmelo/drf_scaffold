import codecs
import re
import os

from setuptools import find_packages, setup


def get_version(filename):
    with codecs.open(filename, 'r', 'utf-8') as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)

NAME = 'drf_scaffold'
VERSION = get_version(os.path.join('drf_scaffold', '__init__.py'))
DESCRIPTION = 'Dead simple custom command to create a django app with djando rest framework CRUD RESTFull API'
URL = 'https://github.com/juliosmelo/drf_scaffold'
AUTHOR = 'juliocsmelo'
AUTHOR_EMAIL = 'juliocsmelo@gmail.com'
LICENSE = 'MIT'
PACKAGES=[
        'drf_scaffold',
        'drf_scaffold.management',
        'drf_scaffold.management.commands']
REQUIREMENTS = ['django']
CLASSIFIERS=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Installation/Setup']

EXCLUDE_FROM_PACKAGES = ['drf_scaffold.conf.drf_app_template',]

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
      install_requires=REQUIREMENTS,
      include_package_data=True,
      classifiers=CLASSIFIERS,
      zip_safe=False)
