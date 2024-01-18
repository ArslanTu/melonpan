# -*- coding: utf-8 -*-
"""A vault app for subjects like books, movies, etc

@File    : apps.py
@Time    : 2024-01-18, Thu, 22:9
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.apps import AppConfig


class VaultConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vault'
    verbose_name = '内容库'
