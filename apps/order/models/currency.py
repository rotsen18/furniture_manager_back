from django.db import models

from mixins.models import DateTimeMixin


class CurrencyRateHistory(DateTimeMixin):
    from_currency = models.ForeignKey(
        'directory.Currency', related_name='currency_from', on_delete=models.PROTECT)
    to_currency = models.ForeignKey(
        'directory.Currency', related_name='currency_to', on_delete=models.PROTECT)
    rate = models.FloatField()

    def __str__(self):
        return f'1 {self.from_currency} = {self.rate} {self.to_currency}'
