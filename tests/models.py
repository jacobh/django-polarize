from __future__ import unicode_literals
from django.db import models

from generic_ratings.model_mixins import RatingTargetMixin


class TextSnippet(RatingTargetMixin, models.Model):
    text = models.TextField()
    user = models.ForeignKey('auth.User')
