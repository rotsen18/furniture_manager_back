from django.contrib.auth.models import AbstractUser
from django.db import models
from furniture_manager import settings


def get_sentinel_user():
    return settings.AUTH_USER_MODEL.objects.get_or_create(username="deleted")[0]


class Manager(AbstractUser):
    pass


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    # TODO add photo field

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


class Type(models.Model):  # swithcer, socket, frame
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Currency(models.Model):
    code = models.CharField(max_length=63)
    rate = models.FloatField()

    def __str__(self):
        return self.code


class Client(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    username = models.CharField(max_length=63, unique=True)
    town = models.CharField(max_length=63, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username


class Order(models.Model):  # order consists of several products
    STATUTES = [
        ("New", "New"),
        ("Send", "Send"),
        ("Completed", "Completed"),
        ("Canceled", "Canceled"),
    ]

    client = models.ForeignKey(
        "Client",
        null=True,
        related_name="orders",
        on_delete=models.SET(get_sentinel_user),
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="orders",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, default="New", choices=STATUTES)
    description = models.CharField(max_length=255, null=True, blank=True)
    manufacturer = models.ForeignKey(
        "Manufacturer", null=True, on_delete=models.CASCADE
    )
    serie = models.ForeignKey("Series", null=True, on_delete=models.CASCADE)
    mech_color = models.ForeignKey(
        "Color", default=2, related_name="mech_colors", on_delete=models.SET_DEFAULT
    )
    cover_color = models.ForeignKey(
        "Color", default=5, related_name="cover_colors", on_delete=models.SET_DEFAULT
    )
    frame_color = models.ForeignKey(
        "Color", default=5, related_name="frame_colors", on_delete=models.SET_DEFAULT
    )
    sets = models.ManyToManyField("Set", through="OrderSet")

    def __str__(self):
        return f"{self.id} {self.client} {self.description}"


class Product(models.Model):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    series = models.ManyToManyField("Series")
    type = models.ForeignKey("Type", on_delete=models.CASCADE)
    component = models.ForeignKey("Component", on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    color = models.ForeignKey("Color", default=2, on_delete=models.SET_DEFAULT)
    article = models.CharField(max_length=255, unique=True)
    ean = models.IntegerField(null=True, blank=True, unique=True)
    price = models.FloatField(null=True)
    price_currency = models.FloatField(null=True)
    type_currency = models.ForeignKey(
        "Currency", default=1, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        if self.description is None:
            self.description = ""
        series = ", ".join([serie.name for serie in self.series.all()])
        return f"{self.manufacturer} {series} {self.component} {self.description} {self.color} {self.article}"


class Set(models.Model):  # PlaceSet consists of several products
    size = models.IntegerField(default=1)
    frame = models.ForeignKey("Product", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Set {self.id}"


class Place(models.Model):
    mechanism = models.ForeignKey("Product", null=True, blank=True, related_name="mech", on_delete=models.CASCADE)
    cover = models.ForeignKey("Product", null=True, blank=True, related_name="cover", on_delete=models.CASCADE)
    additional = models.ForeignKey("Product", null=True, blank=True, related_name="additional", on_delete=models.CASCADE)
    set = models.ForeignKey("Set", related_name="places", on_delete=models.CASCADE)

    def __str__(self):
        return f"Place {self.id}"


class OrderSet(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
