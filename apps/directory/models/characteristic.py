from django.db import models

from mixins.models import NameMixin


class Color(NameMixin):
    # TODO add validators or find app
    # TODO create mixin with default color and few another
    hex_code = models.CharField(max_length=10)
