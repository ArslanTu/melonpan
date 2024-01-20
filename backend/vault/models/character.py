# -*- coding: utf-8 -*-
"""

@File    : character.py
@Time    : 2024-01-20, Sat, 19:44
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject
from .animation_tv import AnimationTVSubject
from .movie import MovieSubject
from .person import PersonSubject
from .tv import TVSubject


class CharacterSubject(Subject):
    tvs = models.ManyToManyField(TVSubject, verbose_name='电视剧', blank=True)
    movies = models.ManyToManyField(MovieSubject, verbose_name='电影', blank=True)
    animation_tvs = models.ManyToManyField(AnimationTVSubject, verbose_name='动画番组', blank=True)

    actors = models.ManyToManyField(PersonSubject, verbose_name='演员', blank=True)

    class Meta:
        verbose_name = '角色'
