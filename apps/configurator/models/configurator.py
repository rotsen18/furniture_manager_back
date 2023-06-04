from django.db import models

from mixins.models import AuthorMixin, DateTimeMixin


class PlaceSet(AuthorMixin, DateTimeMixin):
    """
    Set of places
    """
    size = models.IntegerField(default=1)
    frame = models.ForeignKey('catalogue.Product', null=True, on_delete=models.CASCADE)


class Place(AuthorMixin, DateTimeMixin):
    """
    Place in set
    """
    mechanism = models.ForeignKey('catalogue.Product', null=True, related_name='mech', on_delete=models.CASCADE)
    cover = models.ForeignKey('catalogue.Product', null=True, related_name='cover', on_delete=models.CASCADE)
    additional = models.ForeignKey('catalogue.Product', null=True, related_name='additional', on_delete=models.CASCADE)
    set = models.ForeignKey('PlaceSet', related_name='places', on_delete=models.CASCADE)
