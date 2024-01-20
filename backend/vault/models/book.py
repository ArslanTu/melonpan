# -*- coding: utf-8 -*-
"""

@File    : book.py
@Time    : 2024-01-20, Sat, 15:40
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from django.db import models

from .abstract import Subject, RateableSubject
from .organization import OrganizationSubject
from .person import PersonSubject


class BookSubject(Subject, RateableSubject):
    authors = models.ManyToManyField(PersonSubject, related_name='write_book_set', verbose_name='作者', blank=False)
    press = models.ForeignKey(OrganizationSubject, on_delete=models.SET_NULL, verbose_name='出版社', blank=True,
                              null=True)
    original_title = models.CharField(max_length=255, verbose_name='原作名', blank=True, null=False)
    translators = models.ManyToManyField(PersonSubject, related_name='translate_book_set', verbose_name='译者',
                                         blank=True)
    publish_date = models.DateField(verbose_name='出版年', blank=True, null=True)
    page_number = models.PositiveSmallIntegerField(verbose_name='页数', blank=True, null=True)
    ISBN = models.CharField(max_length=32, verbose_name='ISBN', blank=True, null=True)

    class Meta:
        verbose_name = '书籍'
