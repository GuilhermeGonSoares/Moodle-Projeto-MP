from django.apps import AppConfig

"""
@package moodle

@brief Define os apps do Django que serão utilizados no projeto.
"""
class MoodleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moodle'
