import codecs
import re
import os
import setuptools


def get_version(filename):
    with codecs.open(filename, 'r', 'utf-8') as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)

NAME = 'drf_scafolld'
VERSION = get_version(os.path.join('drf_scafolld', '__init__.py'))
DESCRIPTION = 'Dead simple custom command to create a django app with djando rest framework CRUD RESTFull API'
URL = 'https://github.com/juliosmelo/drf_scafolld'
AUTHOR = 'juliocsmelo'
AUTHOR_EMAIL = 'juliocsmelo@gmail.com'
LICENSE = 'MIT'
PACKAGES=[
        'drf_scafolld',
        'drf_scafolld.management',
        'drf_scafolld.management.commands']
REQUIREMENTS = ['Django>=1.11', 'djangorestframework>=3.8.2']
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

setuptools.setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      packages=PACKAGES,
      install_requires=REQUIREMENTS,
      classifiers=CLASSIFIERS,
      zip_safe=False)
