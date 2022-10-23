from django.db import models

from mixins.models import DateTimeMixin


class Currency(models.Model):
    class CurrencyChoices(models.TextChoices):
        UAH = ("UAH", "Гривня")
        USD = ("USD", "Долар")
        EUR = ("EUR", "Євро")
        PLN = ("PLN", "Злотий")
    code = models.CharField(max_length=63, choices=CurrencyChoices.choices)

    def __str__(self):
        return self.code


class CurrencyRateHistory(DateTimeMixin):
    from_currency = models.ForeignKey("Currency", related_name="currency_from", on_delete=models.PROTECT, default=Currency.CurrencyChoices.USD)
    to_currency = models.ForeignKey("Currency", related_name="currency_to",  on_delete=models.PROTECT, default=Currency.CurrencyChoices.UAH)
    rate = models.FloatField()

    def __str__(self):
        return f"1 {self.from_currency} = {self.rate} {self.to_currency}"
