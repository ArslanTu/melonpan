# -*- coding: utf-8 -*-
"""

@File    : language.py
@Time    : 2024-01-20, Sat, 19:37
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models


class Language(models.Model):
    name = models.CharField(unique=True, max_length=32, verbose_name='语言名')

    class Meta:
        verbose_name = '语言'

    def __str__(self):
        return self.name
