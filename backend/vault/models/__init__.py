# -*- coding: utf-8 -*-
"""All models of vault

@File    : __init__.py
@Time    : 2024-01-20, Sat, 10:30
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""
from .abstract import Subject, RateableSubject
from .book import BookSubject
from .generic import Country, Language, Press
from .movie import MovieGenre, MovieSubject
from .person import Person
from .tv import TVGenre, TVSubject
