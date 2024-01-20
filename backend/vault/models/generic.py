# -*- coding: utf-8 -*-
"""Generic models

@File    : generic.py
@Time    : 2024-01-20, Sat, 11:48
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models


class Country(models.Model):
    name = models.CharField(primary_key=True, max_length=32, verbose_name='国家/地区名')

    class Meta:
        verbose_name = '国家/地区'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(primary_key=True, max_length=32, verbose_name='语言名')

    class Meta:
        verbose_name = '语言'

    def __str__(self):
        return self.name
