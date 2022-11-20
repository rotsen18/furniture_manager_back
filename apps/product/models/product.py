from django.db import models

from apps.directory.models.characteristic import Color
from apps.product.models.manufacturer import Manufacturer
from mixins.models import NameMixin, DateTimeMixin


class Product(NameMixin, DateTimeMixin):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    series = models.ManyToManyField('Series')
    # type = models.ForeignKey("Type", on_delete=models.CASCADE)
    # component = models.ForeignKey("Component", on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_DEFAULT)  # TODO add default color
    article = models.CharField(max_length=255, unique=True)
    ean = models.IntegerField(null=True, blank=True, unique=True)  # TODO find app for ean codes
    # price = models.FloatField(null=True)
    # price_currency = models.FloatField(null=True)
    # type_currency = models.ForeignKey(
    #     "Currency", default=1, null=True, on_delete=models.SET_NULL
    # )
    instruction = models.FileField()

    # def __str__(self):
    #     if self.description is None:
    #         self.description = ""
    #     series = ", ".join([serie.name for serie in self.series.all()])
    #     return f"{self.manufacturer} {series} {self.component} {self.description} {self.color} {self.article}"


class Series(NameMixin, DateTimeMixin):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class ProductPhoto(DateTimeMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField()  # TODO add path

