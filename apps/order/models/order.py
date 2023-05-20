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
    manufacturer = models.ForeignKey("catalogue.Manufacturer", null=True, on_delete=models.CASCADE)
    series = models.ForeignKey("catalogue.Series", null=True, on_delete=models.CASCADE)
    mech_color = models.ForeignKey(
        "directory.Color",
        default=2,
        related_name="mech_colors",
        on_delete=models.SET_DEFAULT
    )
    cover_color = models.ForeignKey(
        "directory.Color",
        default=5,  # TODO change default color to white, check other colors in order
        related_name="cover_colors",
        on_delete=models.SET_DEFAULT  # TODO think about default color
    )
    frame_color = models.ForeignKey(
        "directory.Color",
        default=5,
        related_name="frame_colors",
        on_delete=models.SET_DEFAULT
    )
    place_sets = models.ManyToManyField("configurator.PlaceSet", through="OrderSet")
    status = models.ForeignKey('directory.OrderStatus', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f"{self.id} {self.client} {self.description}"


class OrderSet(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    place_set = models.ForeignKey("configurator.PlaceSet", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


class OrderStatusHistory(DateTimeMixin):

    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    status = models.ForeignKey('directory.OrderStatus', on_delete=models.CASCADE)
