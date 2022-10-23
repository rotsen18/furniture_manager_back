from django.db import models
from furniture_manager import settings


User = settings.AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    # TODO add photo field

    def __str__(self):
        return self.name


class Component(models.Model):  # switcher with 1 button
    name = models.CharField(max_length=255)
    size = models.FloatField(default=1)
    cover = models.ForeignKey(
        "Component",
        null=True,
        blank=True,
        related_name="covers",
        on_delete=models.CASCADE,
    )
    additional_component = models.ForeignKey(
        "Component",
        null=True,
        blank=True,
        related_name="components",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Type(models.Model):  # switcher, socket, frame
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    series = models.ManyToManyField("Series")
    type = models.ForeignKey("Type", on_delete=models.CASCADE)
    component = models.ForeignKey("Component", on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    color = models.ForeignKey("Color", default=2, on_delete=models.SET_DEFAULT)
    article = models.CharField(max_length=255, unique=True)
    ean = models.IntegerField(null=True, blank=True, unique=True)
    price = models.FloatField(null=True)
    price_currency = models.FloatField(null=True)
    type_currency = models.ForeignKey(
        "order.Currency", default=1, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        if self.description is None:
            self.description = ""
        series = ", ".join([serie.name for serie in self.series.all()])
        return f"{self.manufacturer} {series} {self.component} {self.description} {self.color} {self.article}"
