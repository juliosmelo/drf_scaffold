# Setup

## install

copy this repository an only add drf_scaffold in your project or in your sys.path


## Add it to installed apps in django settings.py:

```python
INSTALLED_APPS = (
    ...
    'drf_scaffold',
)
```

## Now create the drf app 

```bash
python manage.py startdrfapp -m my_model --fields "name:string, nickname:string, age:integer, email:email, user:fk auth.User CASCADE" app_name
```

The command above will generate a django app with models, serializers, views and urls.py. You must add to the to installed apps django settings, run migrations commands and add the url in root projects's urls.py.

# Run tests
```bash
python -m unittest
```
