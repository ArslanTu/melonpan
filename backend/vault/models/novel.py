# -*- coding: utf-8 -*-
"""

@File    : novel.py
@Time    : 2024-01-22, Mon, 17:9
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .organization import OrganizationSubject
from .person import PersonSubject


class NovelSubject(Subject, RateableSubject):
    chinese_title = models.CharField(max_length=255, verbose_name='中文名', blank=True, null=False)
    authors = models.ManyToManyField(PersonSubject, related_name='write_novel_set', verbose_name='作者', blank=True)
    illustrators = models.ManyToManyField(PersonSubject, related_name='illustrate_novel_set', verbose_name='插画',
                                          blank=True)
    presses = models.ManyToManyField(OrganizationSubject, verbose_name='出版社', blank=True)
    alternative_names = models.CharField(max_length=255, verbose_name='别名', blank=True)
    release_date = models.DateField(verbose_name='发售日', blank=True, null=True)
    ISBN = models.CharField(max_length=255, verbose_name='ISBN', blank=True)

    class Meta:
        verbose_name = '小说'


class NovelSeriesSubject(Subject):
    chinese_title = models.CharField(max_length=255, verbose_name='中文名', blank=True, null=False)
    number_of_volumes = models.PositiveIntegerField(verbose_name='册数', default=1, blank=True, null=True)
    authors = models.ManyToManyField(PersonSubject, related_name='write_novel_series_set', verbose_name='作者',
                                     blank=True)
    illustrators = models.ManyToManyField(PersonSubject, related_name='illustrate_novel_series_set',
                                          verbose_name='插画',
                                          blank=True)
    presses = models.ManyToManyField(OrganizationSubject, verbose_name='出版社', blank=True)
    alternative_names = models.CharField(max_length=255, verbose_name='别名', blank=True)
    release_date = models.DateField(verbose_name='发售日', blank=True, null=True)
    volumes = models.ManyToManyField(NovelSubject, verbose_name='单行本', blank=True)

    class Meta:
        verbose_name = '小说系列'
