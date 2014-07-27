from __future__ import unicode_literals
from django.contrib.contenttypes.models import ContentType
from .models import Rating


class RatingTargetMixin(object):
    def _get_content_type(self):
        return ContentType.objects.get_for_model(self)

    def get_rating_totals(self):
        ratings = Rating.objects.filter(
            target_content_type=self._get_content_type(),
            target_object_id=self.id,
        )

        output = {'up': 0, 'down': 0}
        for rating in ratings:
            output[rating.direction] += 1

        return output
