from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

class Rating(models.Model):
    DIRECTION_CHOICES = (
        ('up', 'Up'),
        ('down', 'Down')
    )

    direction = models.CharField(max_length=4, choices=DIRECTION_CHOICES)
    target_content_type = models.ForeignKey(ContentType)
    target_object_id = models.PositiveIntegerField()
    target_object = generic.GenericForeignKey(
        'target_content_type', 'target_object_id'
    )
    user = models.ForeignKey(getattr(settings, 'AUTH_USER_MODEL', 'auth.User'))
