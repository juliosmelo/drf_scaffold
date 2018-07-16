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
PACKAGES = ['drf_scafolld']

setuptools.setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      packages=PACKAGES,
      zip_safe=False)
