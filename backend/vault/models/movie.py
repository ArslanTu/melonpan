# -*- coding: utf-8 -*-
"""

@File    : movie.py
@Time    : 2024-01-20, Sat, 14:53
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .generic import Country, Language, Person


class MovieGenre(models.Model):
    name = models.CharField(unique=True, max_length=32, verbose_name='类型名', blank=False, null=False)

    class Meta:
        verbose_name = '电影类型'

    def __str__(self):
        return self.name


class MovieSubject(Subject, RateableSubject):
    directors = models.ManyToManyField(Person, verbose_name='导演', blank=True, null=True)
    screenwriters = models.ManyToManyField(Person, verbose_name='编剧', blank=True, null=True)
    actors = models.ManyToManyField(Person, verbose_name='主演', blank=True, null=True)
    genres = models.ManyToManyField(MovieGenre, verbose_name='类型', blank=False, null=False)
    official_site = models.URLField(max_length=256, verbose_name='官方网站', blank=True, null=False)
    countries = models.ManyToManyField(Country, verbose_name='制片国家/地区', blank=False, null=False)
    languages = models.ManyToManyField(Language, verbose_name='语言', blank=False, null=False)
    release_date = models.DateField(verbose_name='上映日期', blank=True, null=True)
    duration = models.PositiveSmallIntegerField(verbose_name='片长', blank=True, null=True, help_text='单位：分钟')
    alternative_names = models.CharField(max_length=255, verbose_name='又名', blank=True,
                                         null=False)  # separated by slash

    class Meta:
        verbose_name = '电影'
