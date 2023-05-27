"""furniture_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularJSONAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.configurator.urls', namespace='configurator')),
    # path("configurator/", include("configurator.urls", namespace="configurator")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('directory/', include('apps.directory.urls')),
    path('catalogue/', include('apps.catalogue.urls')),
    path('order/', include('apps.order.urls')),
    path('api/v1/get-api-token/', obtain_auth_token),
    path('api/v1/configurator/', include('apps.configurator.api.v1.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.SWAGGER_URL:
    urlpatterns += [
        path('api/v1/Go9lYiNcza68F2lzPrX/', SpectacularAPIView.as_view(urlconf=urlpatterns), name='schema'),
        path('api/v1/Go9lYiNcza68F2lzPrX.json', SpectacularJSONAPIView.as_view(urlconf=urlpatterns), name='schema'),
        path(f'api/v1/{settings.SWAGGER_URL}', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]
