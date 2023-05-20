from django.urls import path
from apps.directory.views import ColorCreateView

urlpatterns = [
    path('color/create/', ColorCreateView.as_view(), name='color_create'),
]

app_name = 'directory'
