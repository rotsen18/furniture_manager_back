from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    username = models.CharField(max_length=63, unique=True)
    town = models.CharField(max_length=63, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username