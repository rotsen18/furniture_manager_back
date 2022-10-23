from django.db import models


class Set(models.Model):  # PlaceSet consists of several products
    size = models.IntegerField(default=1)
    frame = models.ForeignKey("product.Product", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Set {self.id}"


class Place(models.Model):
    mechanism = models.ForeignKey("product.Product", null=True, blank=True, related_name="mech", on_delete=models.CASCADE)
    cover = models.ForeignKey("product.Product", null=True, blank=True, related_name="cover", on_delete=models.CASCADE)
    additional = models.ForeignKey("product.Product", null=True, blank=True, related_name="additional", on_delete=models.CASCADE)
    set = models.ForeignKey("Set", related_name="places", on_delete=models.CASCADE)

    def __str__(self):
        return f"Place {self.id}"


class OrderSet(models.Model):
    order = models.ForeignKey("order.Order", on_delete=models.CASCADE)
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
