# Setup

## Install via pip

```bash
pip install drf_scaffold
```
## Add it to installed apps in django settings.py:

```python
INSTALLED_APPS = (
    ...
    'drf_scaffold',
)
```

## Now create the drf app 

```bash
python manage.py startdrfapp -m my_model --fields name:string, nickname:string, age:integer, email:email
```

The command above will generate a django app with models, serializers, views and urls.py. You must add to the to installed apps django settings, run migrations commands and add the url in root projects's urls.py.

# Run tests
```bash
python -m unittest
```
