# -*- coding: utf-8 -*-
"""abstract class definition

@File    : abstract.py
@Time    : 2024-01-20, Sat, 10:25
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models


class Subject(models.Model):
    """Base class for all subjects"""
    title = models.CharField(max_length=255, verbose_name='条目标题', blank=False, null=False)
    intro = models.TextField(verbose_name='简介', blank=True, null=False)
    cover = models.ImageField(upload_to='images/covers/', verbose_name='封面图', blank=True, null=True)
    is_sensitive = models.BooleanField(default=False, verbose_name='是否敏感', blank=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class RateableSubject(models.Model):
    """Base class for subjects that can be rated"""
    imdb_link = models.URLField(max_length=255, verbose_name='IMDb 链接', blank=True, null=False)
    imdb_rating = models.FloatField(verbose_name='IMDb 评分', blank=True, null=True)
    imdb_rating_count = models.PositiveSmallIntegerField(verbose_name='IMDb 评分人数', blank=True, null=False)

    douban_link = models.URLField(max_length=255, verbose_name='豆瓣链接', blank=True, null=False)
    douban_rating = models.FloatField(verbose_name='豆瓣评分', blank=True, null=True)
    douban_rating_count = models.PositiveSmallIntegerField(verbose_name='豆瓣评分人数', blank=True, null=False)

    bangumi_link = models.URLField(max_length=255, verbose_name='Bangumi 链接', blank=True, null=False)
    bangumi_rating = models.FloatField(verbose_name='Bangumi 评分', blank=True, null=True)
    bangumi_rating_count = models.PositiveSmallIntegerField(verbose_name='Bangumi 评分人数', blank=True, null=False)

    class Meta:
        abstract = True
