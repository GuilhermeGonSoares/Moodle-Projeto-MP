from django.apps import AppConfig

"""
Configuração dos apps Django presentes no projeto
"""


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
