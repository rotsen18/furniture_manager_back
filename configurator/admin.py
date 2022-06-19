from django.contrib import admin

from configurator.models import Set, ProductSet, OrderSet, Product
from configurator.models import Series, Order, Manufacturer
from configurator.models import Type, Component, Currency, Color


admin.site.register(Set)
admin.site.register(Series)
admin.site.register(ProductSet)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Type)
admin.site.register(Component)
admin.site.register(Currency)
admin.site.register(Color)
admin.site.register(OrderSet)
