from django.contrib import admin

from apps.order.models import Order, OrderStatusHistory, CurrencyRateHistory
from apps.directory.models.currency import Currency

admin.site.register(Order)
admin.site.register(OrderStatusHistory)
admin.site.register(Currency)
admin.site.register(CurrencyRateHistory)