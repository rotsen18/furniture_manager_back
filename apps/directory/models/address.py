from django.db import models

from mixins.models import SingleNameMixin, AuthorMixin, DateTimeMixin


class City(SingleNameMixin, AuthorMixin, DateTimeMixin):
    pass


class Country(SingleNameMixin, AuthorMixin, DateTimeMixin):
    code = models.CharField(max_length=2, unique=True, default='')
