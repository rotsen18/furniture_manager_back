from django.contrib import admin

from apps.configurator.models import PlaceSet, Place
from apps.order.models import OrderSet

admin.site.register(PlaceSet)
admin.site.register(OrderSet)
admin.site.register(Place)
