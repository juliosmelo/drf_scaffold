import codecs
import re
import os
from distutils.core import setup


def get_version(filename):
    with codecs.open(filename, 'r', 'utf-8') as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)

NAME = 'drf_scafolld'
VERSION = get_version(os.path.join('drf_scafolld', '__init__.py'))
DESCRIPTION = 'Dead simple scafolld to create a djanfo rest framework CRUD RESTFull API'
URL = ''
AUTHOR = 'juliosmelo'
AUTHOR_EMAIL = 'julio.melo@solvd.tech'
LICENSE = ''
PACKAGES = ['drf_scafolld']

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      packages=PACKAGES,
      zip_safe=False)
