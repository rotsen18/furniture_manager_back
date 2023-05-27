from rest_framework import routers

from apps.directory.api.v1.views.address import CountryViewSet

router = routers.SimpleRouter()
router.register('country', CountryViewSet, basename='country')

urlpatterns = [
]

urlpatterns += router.urls
