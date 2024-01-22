# -*- coding: utf-8 -*-
"""

@File    : game.py
@Time    : 2024-01-22, Mon, 17:23
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .organization import OrganizationSubject
from .person import PersonSubject


class GameGenre(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = '游戏类型'


class GameSubject(Subject, RateableSubject):
    chinese_title = models.CharField(max_length=255, verbose_name='中文名', blank=True)
    developers = models.ManyToManyField(OrganizationSubject, related_name='develope_game_set', verbose_name='开发',
                                        blank=True)
    publishers = models.ManyToManyField(OrganizationSubject, related_name='publish_game_set', verbose_name='发行',
                                        blank=True)
    screenwriters = models.ManyToManyField(PersonSubject, related_name='write_game_set', verbose_name='剧本',
                                           blank=True)
    music_writers = models.ManyToManyField(PersonSubject, related_name='music_write_game_set', verbose_name='音乐',
                                           blank=True)
    alternative_names = models.CharField(max_length=255, verbose_name='别名', blank=True)
    platforms = models.CharField(max_length=255, verbose_name='平台', blank=True, help_text='separated by comma')
    genres = models.ManyToManyField(GameGenre, verbose_name='游戏类型', blank=True)
    engine = models.CharField(max_length=64, verbose_name='游戏引擎', blank=True)
    release_date = models.DateField(verbose_name='发售日期', blank=True)
    official_site = models.URLField(verbose_name='官方网站', blank=True)

    class Meta:
        verbose_name = '游戏'
