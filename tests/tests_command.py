import unittest
import django
import os

from django.conf import settings
from django.core.management import call_command
from django.test import override_settings
from django.test.testcases import SimpleTestCase

settings.configure()
django.setup()

@override_settings(
    INSTALLED_APPS=[
        'drf_scaffold',
    ],
)

class CommandTestCase(SimpleTestCase):

    def test_command(self):
        call_command('startdrfapp', 'test_drfscafolld', '-m', 'my_model', '--fields', 'name:string, username:string, age:integer, id:uuid')
        self.assertTrue(os.path.exists('./test_drfscafolld'))
        self.assertTrue(os.path.exists('./test_drfscafolld/models.py'))
        self.assertTrue(os.path.exists('./test_drfscafolld/views.py'))
        self.assertTrue(os.path.exists('./test_drfscafolld/urls.py'))
        self.assertTrue(os.path.exists('./test_drfscafolld/apps.py'))
        self.assertTrue(os.path.exists('./test_drfscafolld/admin.py'))
        self.assertTrue(os.path.exists('./test_drfscafolld/serializers.py'))
        self.assertTrue(os.path.exists('./test_drfscafolld/__init__.py'))
        self.assertTrue(os.path.exists('./test_drfscafolld/migrations'))
        self.assertTrue(os.path.exists('./test_drfscafolld/migrations/__init__.py'))
