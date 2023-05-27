from django.db import models

from mixins.models import SingleNameMixin


class City(SingleNameMixin):
    pass

    def __str__(self):
        return self.name


class Country(SingleNameMixin):
    code = models.CharField(max_length=2, unique=True, default='')

    def __str__(self):
        return self.name
