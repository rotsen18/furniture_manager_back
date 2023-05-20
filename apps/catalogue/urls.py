from django.urls import path

from apps.catalogue.views import ManufacturerCreateView

urlpatterns = [
    path(
        'manufacturers/create/',
        ManufacturerCreateView.as_view(),
        name='manufacturer_create',
    ),
]

app_name = 'catalogue'
