from django.db import models

from mixins.models import NameMixin


class Country(NameMixin):
    country_code = models.CharField(max_length=10, null=True, default='')


class Region(NameMixin):
    pass


class City(NameMixin):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    county = models.ForeignKey(Country, on_delete=models.CASCADE)


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=200, null=True, default='')
    building = models.CharField(max_length=15)
    flat = models.SmallIntegerField(null=True)
    postal_code = models.SmallIntegerField(null=True)

    @property
    def address(self):
        return f'{self.city.name}, {self.city.county}'

    @property
    def full_address(self):
        street = f'vul.{self.street}' if self.street else ''
        building = f'bud.{self.building}/{self.flat}'
        if self.flat is not None:
            building += f'/{self.flat}'
        city = self.city
        if city.region is not None:
            city += f', {city.region} obl.'
        if self.postal_code is not None:
            city += f', {self.postal_code}'
        values = [street, building, city, city.county]
        return ', '.join(values)
