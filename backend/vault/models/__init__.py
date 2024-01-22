# -*- coding: utf-8 -*-
"""All models of vault

@File    : __init__.py
@Time    : 2024-01-20, Sat, 10:30
@Author  : ArslanTu
@Mail    : arslantu@arslantu

"""

from .abstract import Subject, RateableSubject
from .animation import AnimationSubject
from .book import BookSubject
from .character import CharacterSubject
from .country import Country
from .language import Language
from .movie import MovieGenre, MovieSubject
from .organization import OrganizationSubject
from .person import PersonSubject
from .tv import TVGenre, TVSubject
