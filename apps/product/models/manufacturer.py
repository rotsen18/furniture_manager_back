from django.db import models

from apps.directory.models import Address
from mixins.models import NameMixin, DateTimeMixin


class Manufacturer(NameMixin, DateTimeMixin):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)


class ManufacturerFactory(NameMixin, DateTimeMixin):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
