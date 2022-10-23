from django.conf import settings
from django.db import models

from apps.core.models import get_sentinel_user
from mixins.models import DateTimeMixin


User = settings.AUTH_USER_MODEL


class Order(DateTimeMixin):
    client = models.ForeignKey(
        User,
        null=True,
        related_name="clint_orders",
        on_delete=models.SET(get_sentinel_user),
    )
    manager = models.ForeignKey(
        User,
        null=True,
        related_name="manager_orders",
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.ForeignKey(
        "product.Manufacturer", null=True, on_delete=models.CASCADE
    )
    serie = models.ForeignKey("product.Series", null=True, on_delete=models.CASCADE)
    mech_color = models.ForeignKey(
        "product.Color", default=2, related_name="mech_colors", on_delete=models.SET_DEFAULT
    )
    cover_color = models.ForeignKey(
        "product.Color", default=5, related_name="cover_colors", on_delete=models.SET_DEFAULT
    )
    frame_color = models.ForeignKey(
        "product.Color", default=5, related_name="frame_colors", on_delete=models.SET_DEFAULT
    )
    sets = models.ManyToManyField("configurator.Set", through="configurator.OrderSet")

    def __str__(self):
        return f"{self.id} {self.client} {self.description}"


class OrderStatusHistory(DateTimeMixin):
    class OrderStatusesChoices(models.TextChoices):
        NEW = ("New", "New")
        PROCESS = ('Process', 'Process')
        SEND = ("Send", "Send")
        DELIVERY = ("Delivery", "Delivery")
        DELIVERED = ("Delivered", "Delivered")
        COMPLETED = ("Completed", "Completed")
        CANCELED = ("Canceled", "Canceled")

    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    status = models.CharField(max_length=33, choices=OrderStatusesChoices.choices, default=OrderStatusesChoices.NEW)
