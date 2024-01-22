from django.test import TestCase

from .models import PersonSubject, AnimationSubject, CharacterSubject


# Create your tests here.


class CharacterSubjectTests(TestCase):
    @staticmethod
    def create_data():
        person = PersonSubject.objects.create(title='花澤香菜')
        animation_tv = AnimationSubject.objects.create(title='Angel Beats!')
        animation_tv.actors.add(person)
        character = CharacterSubject.objects.create(title='立华奏')
        character.actors.add(person)
        character.animation_tvs.add(animation_tv)

    def test_query(self):
        self.create_data()
        person = PersonSubject.objects.get(title='花澤香菜')
        character = CharacterSubject.objects.get(title='立华奏')
        animation_tv = AnimationSubject.objects.get(title='Angel Beats!')

        assert animation_tv.charactersubject_set.filter(actors=person).first() == character
