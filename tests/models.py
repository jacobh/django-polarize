from __future__ import unicode_literals
from django.db import models


class TextSnippet(models.Model):
    text = models.TextField()
    user = models.ForeignKey('auth.User')