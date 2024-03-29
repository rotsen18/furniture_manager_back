from django.contrib import admin

from configurator.models import Set, OrderSet, Product, Manager, Place
from configurator.models import Series, Order, Manufacturer, Client
from configurator.models import Type, Component, Currency, Color


admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Set)
admin.site.register(Series)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Type)
admin.site.register(Component)
admin.site.register(Currency)
admin.site.register(Color)
admin.site.register(OrderSet)
admin.site.register(Place)
