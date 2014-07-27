from __future__ import unicode_literals
from django.db import models

from polarize.model_mixins import RatingTargetMixin


class TextSnippet(RatingTargetMixin, models.Model):
    text = models.TextField()
    user = models.ForeignKey('auth.User')
