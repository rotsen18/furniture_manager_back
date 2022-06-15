from django.contrib.auth.models import User
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Series(models.Model):
    name = models.CharField(max_length=255)
    # TODO add photo field
    # TODO add scheme field (frame+mech+button)


class Component(models.Model):
    name = models.CharField(max_length=255)


class Type(models.Model):
    name = models.CharField(max_length=255)


class Color(models.Model):
    name = models.CharField(max_length=255)
    hex_code = models.CharField(max_length=8)


class Currency(models.Model):
    code = models.CharField(max_length=63)
    rate = models.FloatField()


class Product(models.Model):
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    series = models.ForeignKey("Series", on_delete=models.CASCADE)
    type = models.ForeignKey("Type", on_delete=models.CASCADE)
    component = models.ForeignKey("Component", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    color = models.ForeignKey("Color", null=True, on_delete=models.SET_NULL)
    article = models.CharField(max_length=255)
    ean = models.IntegerField()
    price = models.FloatField()
    price_currency = models.FloatField()
    type_currency = models.ForeignKey(
        "Currency",
        null=True,
        on_delete=models.SET_NULL
    )


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    order_created = models.DateTimeField(auto_now_add=True)
    order_changed = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    products = models.ManyToManyField(
        "Product",
        related_name="orders",
        through="OrderItem"
    )


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


# class Cart(models.Model):
#     pass
#
#
# class OrderHistory(models.Model):
#     pass
