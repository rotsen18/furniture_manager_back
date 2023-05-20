from django.db import models

from furniture_manager import settings

User = settings.AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey('directory.Country', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    # TODO add photo field

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    series = models.ManyToManyField('Series')
    type = models.ForeignKey('directory.ComponentType', on_delete=models.CASCADE)
    component = models.ForeignKey('directory.Component', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='', blank=True)
    color = models.ForeignKey('directory.Color', default=2, on_delete=models.SET_DEFAULT)
    article = models.CharField(max_length=255, unique=True)
    ean = models.IntegerField(null=True, blank=True, unique=True)
    price = models.FloatField(null=True)
    price_currency = models.FloatField(null=True)
    currency = models.ForeignKey('directory.Currency', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.description is None:
            self.description = ''
        series = ', '.join([serie.name for serie in self.series.all()])
        return f'{self.manufacturer} {series} {self.component} {self.description} {self.color} {self.article}'
