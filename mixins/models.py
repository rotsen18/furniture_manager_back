from django.conf import settings
from django.db import models
from django.utils import timezone


User = settings.AUTH_USER_MODEL


class SingleNameMixin(models.Model):
    name = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthorMixin(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True




