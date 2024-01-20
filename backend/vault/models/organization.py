# -*- coding: utf-8 -*-
"""

@File    : organization.py
@Time    : 2024-01-20, Sat, 19:36
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from .abstract import Subject


class Organization(Subject):
    class Meta:
        verbose_name = '组织'
