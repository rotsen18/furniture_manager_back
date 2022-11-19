from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


def get_sentinel_user():
    return settings.AUTH_USER_MODEL.objects.get_or_create(username="deleted")[0]


class User(AbstractUser):
    class TypeUserChoices(models.TextChoices):
        ADMIN = ('Admin', 'Адмін')
        MANAGER = ('Manager', 'Менеджер')
        CONSUMER = ('Consumer', 'Користувач')

    type_user = models.CharField(choices=TypeUserChoices.choices, default=TypeUserChoices.CONSUMER, max_length=40)
    town = models.CharField(max_length=63, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
