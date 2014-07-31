Django Polarize
======================

## Compatability

- Django >= 1.5
- South >= 1.0 (not required if using Django >= 1.7)

## Installation

First, simply pip install the app

```
$ pip install django-polarize
```

Then add it to your `INSTALLED_APPS`

```python
INSTALLED_APPS = (
    ...
    'polarize',
)
```

## Usage

### Creating Ratings

```python
from django.contrib.auth.models import User
from polarize.models import Rating
from my_articles_app.models import Article

user = User.objects.get(...)
article = Article.objects.get(...)

Rating.objects.create(
    user=user,
    target_object=article,
    direction='up' # or 'down'
)
```

### Getting Ratings for Model

```python
from polarize.model_mixins import RatingTargetMixin

class Article(RatingTargetMixin, models.Model):
    ...

...

my_article.get_ratings_totals()
# {'up': 137, 'down': 26}
```
