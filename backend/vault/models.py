# -*- coding: utf-8 -*-
"""All models of vault

@File    : models.py
@Time    : 2024-01-19, Fri, 15:49
@Author  : ArslanTu
@Mail    : arslantu@arslantu

Include subject types from douban: TV, Movie, Book,
Include subject types from bangumi: AnimationTV, AnimationMovie, Comic, ComicSeries, Novel
Include subject types from both source: Music, Game
"""

from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=256, verbose_name='条目标题')
    cover = models.ImageField(
        upload_to='images/covers/',
        verbose_name='封面图',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

