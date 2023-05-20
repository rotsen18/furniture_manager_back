from django.urls import path

from apps.configurator.views import (
    SetUpdateView,
    SetDeleteView,
    PlaceUpdateView,
    PlaceDeleteView,
    ManagerDetailView, set_create_view, create_place_view,
)
from apps.order import views
from apps.catalogue.views import ProductListView, SeriesCreateView

urlpatterns = [
    path('', views.index, name='index'),


    path('managers/<int:pk>/', ManagerDetailView.as_view(), name='manager_detail'),
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('series/create/', SeriesCreateView.as_view(), name='series_create'),
    path('sets/<int:pk>/edit/', SetUpdateView.as_view(), name='set_edit'),
    path('sets/<int:pk>/delete/', SetDeleteView.as_view(), name='set_delete'),
    path('sets/create/', set_create_view, name='set_create'),

    path('place/<int:pk>/create/', create_place_view, name='place_create'),
    path('place/<int:pk>/update/', PlaceUpdateView.as_view(), name='place_update'),
    path('place/<int:pk>/delete/', PlaceDeleteView.as_view(), name='place_delete'),

    # path("login/", views.LoginView.as_view),
    # path("logout/", views.LogoutView.as_view),
]


app_name = 'configurator'
