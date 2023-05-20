from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    city = models.ForeignKey('directory.City', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=15, unique=True, default='', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
