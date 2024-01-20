# -*- coding: utf-8 -*-
"""

@File    : tv.py
@Time    : 2024-01-20, Sat, 10:28
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .generic import Country, Language
from .person import Person


class TVGenre(models.Model):
    name = models.CharField(unique=True, max_length=32, verbose_name='类型名', blank=False, null=False)

    class Meta:
        verbose_name = "电视剧类型"

    def __str__(self):
        return self.name


class TVSubject(Subject, RateableSubject):
    directors = models.ManyToManyField(Person, verbose_name='导演', blank=True, null=True)
    screenwriters = models.ManyToManyField(Person, verbose_name='编剧', blank=True, null=True)
    actors = models.ManyToManyField(Person, verbose_name='主演', blank=True, null=True)
    genres = models.ManyToManyField(TVGenre, verbose_name='类型', blank=False, null=False)
    official_site = models.URLField(max_length=255, verbose_name='官方网站', blank=True, null=False)
    countries = models.ManyToManyField(Country, verbose_name='制片国家/地区', blank=False, null=False)
    languages = models.ManyToManyField(Language, verbose_name='语言', blank=False, null=False)
    airing_date = models.DateField(verbose_name='首播时间', blank=True, null=True)
    number_of_episodes = models.PositiveSmallIntegerField(verbose_name='集数', default=1, blank=False, null=False)
    number_of_seasons = models.PositiveSmallIntegerField(verbose_name='季数', default=1, blank=False, null=False)
    duration_per_episode = models.PositiveSmallIntegerField(verbose_name='单集片长', blank=True, null=True,
                                                            help_text="单位：分钟")
    alternative_names = models.CharField(max_length=255, verbose_name='又名', blank=True,
                                         null=False)  # separated by slash

    class Meta:
        verbose_name = "电视剧"
