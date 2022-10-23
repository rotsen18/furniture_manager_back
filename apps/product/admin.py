from django.contrib import admin

from apps.product.models import Series, Product, Manufacturer, Type, Component, Color

admin.site.register(Series)
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Type)  # TODO rename
admin.site.register(Component)  # TODO rename
admin.site.register(Color)
