from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        "Manufacturer",
        on_delete=models.CASCADE
    )
    # TODO add photo field

    def __str__(self):
        return self.name


class Component(models.Model):  # switcher with 1 button
    name = models.CharField(max_length=255)
    size = models.FloatField(default=1)
    cover = models.ForeignKey("Component",
                              null=True,
                              blank=True,
                              related_name="covers",
                              on_delete=models.CASCADE)
    additional_component = models.ForeignKey(
        "Component",
        null=True,
        blank=True,
        related_name="components",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Type(models.Model):  # swithcer, socket, frame
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)
    hex_code = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Currency(models.Model):
    code = models.CharField(max_length=63)
    rate = models.FloatField()

    def __str__(self):
        return self.code


class Order(models.Model):  # order consists of several products
    owner = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255, null=True)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    serie = models.ForeignKey("Series", on_delete=models.CASCADE)
    mech_color = models.ForeignKey("Color", default=2,
                                   related_name="mech_colors",
                                   on_delete=models.SET_DEFAULT)
    cover_color = models.ForeignKey("Color", default=5,
                                    related_name="cover_colors",
                                    on_delete=models.SET_DEFAULT)
    frame_color = models.ForeignKey("Color", default=5,
                                    related_name="frame_colors",
                                    on_delete=models.SET_DEFAULT)
    sets = models.ManyToManyField(
        "Set",
        through="OrderSet"
    )

    def __str__(self):
        return f"{self.owner} {self.description} {self.created}"


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
        "Currency",
        default=1,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        if self.description is None:
            self.description = ""
        series = ", ".join([serie.name for serie in self.series.all()])
        return f"{self.manufacturer} {series} {self.component} {self.description} {self.color} {self.article}"


class Set(models.Model):  # ProductSet consists of several products
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(
        "Product",
        through="ProductSet"
    )

    def __str__(self):
        return self.name


class ProductSet(models.Model):
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f"set:{self.set} {self.product} {self.amount}"


class OrderSet(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    set = models.ForeignKey("Set", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
