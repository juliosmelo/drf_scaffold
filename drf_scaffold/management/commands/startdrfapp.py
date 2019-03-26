from os import path

from django.apps import apps
from django.db import models
from django.core.management.templates import TemplateCommand

import drf_scaffold
from drf_scaffold.constants import (
    MODEL_FIELDS,
    FK,
    DELETE_CONSTRAINTS
)


class Command(TemplateCommand):
    help = (
        "Creates a Django Rest Framework RESTFull CRUD app directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."

    def add_arguments(self, parser):
        parser.add_argument('--model', '-m', dest='model_name', help='Name of the model')
        
        parser.add_argument(
            '--fields', '-f', dest='fields',
            action='append', default=[],
            help='The fields name(s). Separate fields names '
                 'with commas, or use -f multiple times.'
        )
        super().add_arguments(parser)

    def handle(self, **options):
        app_name = options.pop('name')
        model_name = options.pop('model_name')
        fields = options.pop('fields')[0].split(',')
        options['template'] = path.join(drf_scaffold.__path__[0], 'conf', 'drf_app_template')
        options['model_name'] = model_name
        model_fields = [(f_name, m_field) for f_name, m_field in separate_fields(fields)]
        options['model_fields'] = model_fields
        options['camel_case_model_name'] = ''.join(x for x in model_name.title() if x != '_')
        super().handle('app', app_name, **options)


def separate_fields(fields):
    for field in fields:
        field_name, model_field = tuple(map(lambda f: f.strip(), field.split(':')))
        if model_field.split()[0] == FK:
            model_field = manage_foreign_keys_field(model_field)
        else:
            model_field = MODEL_FIELDS.get(model_field)
        yield field_name, model_field


def manage_foreign_keys_field(model_field):
    '''
    format for foreign keys, on_delete type default is CASCADE
    fk app_name.model_name [on_delete_type]
    '''
    if len(model_field.split()) < 2:
        raise ValueError('must specify at least the model to reference')
    arguments = model_field.split()[1:]
    if '.' not in arguments[0]:
        raise ValueError('must specify reference as app.model')
    apps.get_model(arguments[0]) # raise exception if not registered
    if len(arguments) < 2:
        arguments.append(models.CASCADE.__name__)
    else:
        if arguments[1] not in DELETE_CONSTRAINTS:
            raise ValueError('delete constraint not in django on_delete_options')

    return MODEL_FIELDS.get(model_field.split()[0]).format(*arguments)
