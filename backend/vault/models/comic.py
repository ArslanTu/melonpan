# -*- coding: utf-8 -*-
"""

@File    : comic.py
@Time    : 2024-01-22, Mon, 16:42
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .organization import OrganizationSubject
from .person import PersonSubject


class ComicSubject(Subject, RateableSubject):
    chinese_title = models.CharField(max_length=255, verbose_name='中文名', blank=True, null=False)
    number_of_episode = models.PositiveIntegerField(verbose_name='话数', default=1, blank=True, null=True)
    authors = models.ManyToManyField(PersonSubject, verbose_name='作者', blank=True)
    press = models.ManyToManyField(OrganizationSubject, related_name='publish_comic_set', verbose_name='出版社',
                                   blank=True)
    magazines = models.ManyToManyField(OrganizationSubject, related_name='serialize_comic_set', verbose_name='连载杂志',
                                       blank=True)
    alternative_names = models.CharField(max_length=255, verbose_name='别名', blank=True)
    release_date = models.DateField(verbose_name='发售日', blank=True, null=True)
    ISBN = models.CharField(max_length=255, verbose_name='ISBN', blank=True)

    class Meta:
        verbose_name = '漫画'


class ComicSeriesSubject(Subject, RateableSubject):
    chinese_title = models.CharField(max_length=255, verbose_name='中文名', blank=True, null=False)
    number_of_episode = models.PositiveIntegerField(verbose_name='话数', default=1, blank=True, null=True)
    number_of_volumes = models.PositiveIntegerField(verbose_name='册数', default=1, blank=True, null=True)
    authors = models.ManyToManyField(PersonSubject, verbose_name='作者', blank=True)
    press = models.ManyToManyField(OrganizationSubject, related_name='publish_comic_series_set', verbose_name='出版社',
                                   blank=True)
    magazines = models.ManyToManyField(OrganizationSubject, related_name='serialize_comic_series_set',
                                       verbose_name='连载杂志',
                                       blank=True)
    alternative_names = models.CharField(max_length=255, verbose_name='别名', blank=True)
    release_date = models.DateField(verbose_name='发售日', blank=True, null=True)
    volumes = models.ManyToManyField(ComicSubject, verbose_name='单行本', blank=True)

    class Meta:
        verbose_name = '漫画系列'
