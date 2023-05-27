from django.contrib import admin

from apps.directory.models import Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
