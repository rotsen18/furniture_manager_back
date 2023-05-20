from django.db import models

from mixins.models import SingleNameMixin


class OrderStatus(SingleNameMixin):
    class OrderStatusesChoices(models.TextChoices):
        NEW = ("New", "New")
        PROCESS = ('Process', 'Process')
        SEND = ("Send", "Send")
        DELIVERY = ("Delivery", "Delivery")
        DELIVERED = ("Delivered", "Delivered")
        COMPLETED = ("Completed", "Completed")
        CANCELED = ("Canceled", "Canceled")
