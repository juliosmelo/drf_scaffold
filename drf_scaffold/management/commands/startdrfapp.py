from os import path
import drf_scaffold
from drf_scaffold.constants import MODEL_FIELDS

from django.core.management.templates import TemplateCommand


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
        if model_field.split()[0] == 'fk':
            model_field = MODEL_FIELDS.get(model_field.split()[0]).format(*model_field.split()[1:])
        else:
            model_field = MODEL_FIELDS.get(model_field)
        yield field_name, model_field
