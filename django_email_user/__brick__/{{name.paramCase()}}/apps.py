from django.apps import AppConfig


class {{name.pascalCase()}}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{name.paramCase()}}'
