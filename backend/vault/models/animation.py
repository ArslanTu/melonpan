# -*- coding: utf-8 -*-
"""

@File    : animation.py
@Time    : 2024-01-20, Sat, 16:50
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .person import PersonSubject


class AnimationSubject(Subject, RateableSubject):
    chinese_title = models.CharField(max_length=255, verbose_name='中文名', blank=True, null=False)
    number_of_episodes = models.PositiveSmallIntegerField(verbose_name='话数', default=1, blank=False, null=False)
    airing_date = models.DateField(verbose_name='放送开始', blank=True, null=True)
    release_date = models.DateField(verbose_name='上映年度', blank=True, null=True)
    original_authors = models.ManyToManyField(PersonSubject, related_name='original_work_animation_tv_set',
                                              verbose_name='原作者', blank=True)
    directors = models.ManyToManyField(PersonSubject, related_name='direct_animation_tv_set', verbose_name='导演',
                                       blank=True)
    screenwriters = models.ManyToManyField(PersonSubject, related_name='write_animation_tv_set', verbose_name='脚本',
                                           blank=True)
    music_directors = models.ManyToManyField(PersonSubject, related_name='direct_music_of_animation_tv_set',
                                             verbose_name='音乐', blank=True)
    op_singers = models.ManyToManyField(PersonSubject, related_name='sing_op_of_animation_tv_set',
                                        verbose_name='主题歌演出',
                                        blank=True)
    ins_singers = models.ManyToManyField(PersonSubject, related_name='sing_ins_of_animation_tv_set',
                                         verbose_name='插入歌演出',
                                         blank=True)
    anime_producers = models.ManyToManyField(PersonSubject, related_name='produce_animation_tv_set',
                                             verbose_name='动画制作',
                                             blank=True)
    alternative_names = models.CharField(max_length=255, verbose_name='别名', blank=True, null=False)
    actors = models.ManyToManyField(PersonSubject, related_name='act_animation_tv_set', verbose_name='声优', blank=True)
    official_site = models.URLField(verbose_name='官方网站', blank=True, null=False)

    class Meta:
        verbose_name = '动画'
