from django.db import models

class PlaceSet(models.Model):
    size = models.IntegerField(default=1)
    frame = models.ForeignKey('catalogue.Product', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Set {self.id}'


class Place(models.Model):
    mechanism = models.ForeignKey('catalogue.Product', null=True, related_name='mech', on_delete=models.CASCADE)
    cover = models.ForeignKey('catalogue.Product', null=True, related_name='cover', on_delete=models.CASCADE)
    additional = models.ForeignKey('catalogue.Product', null=True, related_name='additional', on_delete=models.CASCADE)
    set = models.ForeignKey('PlaceSet', related_name='places', on_delete=models.CASCADE)

    def __str__(self):
        return f'Place {self.id}'
