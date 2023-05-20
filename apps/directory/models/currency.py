from django.db import models


class Currency(models.Model):
    class CurrencyChoices(models.TextChoices):
        UAH = ("UAH", "Гривня")
        USD = ("USD", "Долар")
        EUR = ("EUR", "Євро")
        PLN = ("PLN", "Злотий")
    code = models.CharField(max_length=63, choices=CurrencyChoices.choices, default=CurrencyChoices.USD)

    def __str__(self):
        return self.code
