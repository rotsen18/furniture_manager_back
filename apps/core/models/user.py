from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


def get_sentinel_user():
    return settings.AUTH_USER_MODEL.objects.get_or_create(username="deleted")[0]


class User(AbstractUser):
    class TypeUserChoices(models.TextChoices):
        ADMIN = ('Admin', 'Адмін')
        MANAGER = ('Manager', 'Менеджер')
        Client = ('Client', 'Клієнт')

    type_user = models.CharField(choices=TypeUserChoices.choices, default=TypeUserChoices.Client, max_length=40)
