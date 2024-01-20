# -*- coding: utf-8 -*-
"""

@File    : book.py
@Time    : 2024-01-20, Sat, 15:40
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .generic import Organization
from .person import Person


class BookSubject(Subject, RateableSubject):
    authors = models.ManyToManyField(Person, verbose_name='作者', blank=False, null=False)
    press = models.ForeignKey(Organization, on_delete=models.SET_NULL, verbose_name='出版社', blank=True, null=True)
    original_title = models.CharField(max_length=255, verbose_name='原作名', blank=True, null=False)
    translators = models.ManyToManyField(Person, verbose_name='译者', blank=True, null=True)
    publish_date = models.DateField(verbose_name='出版年', blank=True, null=True)
    page_number = models.PositiveSmallIntegerField(verbose_name='页数', blank=True, null=True)
    ISBN = models.CharField(max_length=32, verbose_name='ISBN', blank=True, null=True)

    class Meta:
        verbose_name = '书籍'
