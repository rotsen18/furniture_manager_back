from rest_framework import viewsets

from apps.directory.models import Country, City
from apps.directory.api.v1.serializers import address as serializers


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.order_by('name')
    serializer_class = serializers.CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.order_by('name')
    serializer_class = serializers.CitySerializer
