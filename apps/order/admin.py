from django.contrib import admin

from apps.order.models import Order, OrderStatusHistory, Currency, CurrencyRateHistory


admin.site.register(Order)
admin.site.register(OrderStatusHistory)
admin.site.register(Currency)
admin.site.register(CurrencyRateHistory)
