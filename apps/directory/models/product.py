from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class ComponentType(models.Model):  # switcher, socket, frame
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Component(models.Model):  # switcher with 1 button
    name = models.CharField(max_length=255)
    size = models.FloatField(default=1)
    cover = models.ForeignKey(
        "Component",
        null=True,
        blank=True,
        related_name="covers",
        on_delete=models.CASCADE,
    )
    additional_component = models.ForeignKey(
        "Component",
        null=True,
        blank=True,
        related_name="components",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
