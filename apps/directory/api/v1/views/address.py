from rest_framework import viewsets

from apps.directory.models import Country
from apps.directory.api.v1.serializers import address as serializers

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer
