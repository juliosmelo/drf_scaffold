import unittest
import django
from django.conf import settings
from django.core.management import call_command
from django.test import override_settings
from django.test.testcases import SimpleTestCase

settings.configure()
django.setup()

@override_settings(
    INSTALLED_APPS=[
        'drf_scafolld',
    ],
)

class CommandTestCase(SimpleTestCase):

    def test_command(self):
        call_command('startdrfapp', 'test_drfscafolld', '-m', 'my_model', '--fields', 'name:string, username:string, age:integer, id:uuid')
