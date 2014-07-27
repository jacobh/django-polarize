from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User

from generic_ratings.models import Rating
from .models import TextSnippet


class RatingTargetMixinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('justin', 'password')
        self.snippet = TextSnippet.objects.create(
            text="Here's some *wonderfully* informative text",
            user=self.user
        )

    def test_get_ratings_totals_returns_totals_for_ups_and_downs(self):
        user2 = User.objects.create_user('kate', 'password')
        user3 = User.objects.create_user('tim', 'password')

        Rating.objects.create(
            direction='up',
            target_object=self.snippet,
            user=self.user
        )
        Rating.objects.create(
            direction='up',
            target_object=self.snippet,
            user=user2
        )
        Rating.objects.create(
            direction='down',
            target_object=self.snippet,
            user=user3
        )

        result = self.snippet.get_rating_totals()
        self.assertEqual({'up': 2, 'down': 1}, result)
