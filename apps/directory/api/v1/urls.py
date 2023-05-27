from rest_framework import routers

from apps.directory.api.v1.views.address import CountryViewSet, CityViewSet

router = routers.SimpleRouter()
router.register('country', CountryViewSet, basename='country')
router.register('city', CityViewSet, basename='city')

urlpatterns = [
]

urlpatterns += router.urls
