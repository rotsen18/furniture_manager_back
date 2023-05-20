from django.contrib import admin

from apps.catalogue.models.product import Manufacturer, Series, Product
from apps.directory.models.product import Color, ComponentType, Component

admin.site.register(Series)
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(ComponentType)  # TODO rename
admin.site.register(Component)  # TODO rename
admin.site.register(Color)
