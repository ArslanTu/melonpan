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
    """Base class for all subjects"""
    title = models.CharField(max_length=256, verbose_name='条目标题')
    cover = models.ImageField(upload_to='images/covers/', verbose_name='封面图', blank=True, null=True)
    is_sensitive = models.BooleanField(default=False, verbose_name='是否敏感')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class RateableSubject(models.Model):
    """Base class for subjects that can be rated"""
    imdb_link = models.URLField(max_length=256, verbose_name='IMDb 链接', blank=True, null=True)
    imdb_rating = models.FloatField(verbose_name='IMDb 评分', blank=True, null=True)
    imdb_rating_count = models.CommaSeparatedIntegerField(verbose_name='IMDb 评分人数', blank=True, null=True)

    douban_link = models.URLField(max_length=256, verbose_name='豆瓣链接', blank=True, null=True)
    douban_rating = models.FloatField(verbose_name='豆瓣评分', blank=True, null=True)
    douban_rating_count = models.CommaSeparatedIntegerField(verbose_name='豆瓣评分人数', blank=True, null=True)

    bangumi_link = models.URLField(max_length=256, verbose_name='Bangumi 链接', blank=True, null=True)
    bangumi_rating = models.FloatField(verbose_name='Bangumi 评分', blank=True, null=True)
    bangumi_rating_count = models.CommaSeparatedIntegerField(verbose_name='Bangumi 评分人数', blank=True, null=True)

    class Meta:
        abstract = True


class Person(Subject):  # IMPLEMENT
    pass


class TVGenre(models.Model):
    COMEDY = 'COMEDY'
    ROMANCE = 'ROMANCE'
    MYSTERY = 'MYSTERY'
    ANIMATION = 'ANIMATION'
    WU_XIA = 'WU_XIA'
    COSTUME = 'COSTUME'
    FAMILY = 'FAMILY'
    CRIME = 'CRIME'
    SCIENCE_FICTION = 'SCIENCE_FICTION'
    HORROR = 'HORROR'
    HISTORICAL = 'HISTORICAL'
    WAR = 'WAR'
    ACTION = 'ACTION'
    ADVENTURE = 'ADVENTURE'
    BIOGRAPHY = 'BIOGRAPHY'
    DRAMA = 'DRAMA'
    FANTASY = 'FANTASY'
    THRILLER = 'THRILLER'
    DISASTER = 'DISASTER'
    SONG_AND_DANCE = 'SONG_AND_DANCE'
    MUSICAL = 'MUSICAL'
    OTHER = 'OTHER'

    TV_GENRES = (
        (COMEDY, '喜剧'),
        (ROMANCE, '爱情'),
        (MYSTERY, '悬疑'),
        (ANIMATION, '动画'),
        (WU_XIA, '武侠'),
        (COSTUME, '古装'),
        (FAMILY, '家庭'),
        (CRIME, '犯罪'),
        (SCIENCE_FICTION, '科幻'),
        (HORROR, '恐怖'),
        (HISTORICAL, '历史'),
        (WAR, '战争'),
        (ACTION, '动作'),
        (ADVENTURE, '冒险'),
        (BIOGRAPHY, '传记'),
        (DRAMA, '剧情'),
        (FANTASY, '奇幻'),
        (THRILLER, '惊悚'),
        (DISASTER, '灾难'),
        (SONG_AND_DANCE, '歌舞'),
        (MUSICAL, '音乐'),
        (OTHER, '其他'),
    )

    name = models.CharField(max_length=64, choices=TV_GENRES, default=OTHER, verbose_name='类型名')

    class Meta:
        verbose_name = "电视剧类型"

    def __str__(self):
        return self.name


class TVSubject(Subject, RateableSubject):
    directors = models.ManyToManyField(Person, verbose_name='导演', blank=True, null=True)
    screen_writers = models.ManyToManyField(Person, verbose_name='编剧', blank=True, null=True)
    actors = models.ManyToManyField(Person, verbose_name='主演', blank=True, null=True)
    genres = models.ManyToManyField(TVGenre, verbose_name='类型')
    official_site = models.URLField(max_length=256, verbose_name='官方网站', blank=True, null=True)
    country = models.CharField(max_length=64, verbose_name='制片国家/地区', blank=True, null=True)
    language = models.CharField(max_length=64, verbose_name='语言', blank=True, null=True)
    airing_date = models.DateField(verbose_name='首播时间', blank=True, null=True)
    number_of_episodes = models.PositiveIntegerField(verbose_name='集数', default=1)
    number_of_seasons = models.PositiveIntegerField(verbose_name='季数', default=1)
    duration_per_episode = models.PositiveIntegerField(verbose_name='单集片长', default=1, help_text="单位：分钟")
    alternative_names = models.CharField(max_length=256, verbose_name='又名', blank=True,
                                         null=True)  # separate by slash

    class Meta:
        verbose_name = "电视剧"
