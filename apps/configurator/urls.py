from django.urls import path

from apps.configurator.views import (
    SetUpdateView,
    SetDeleteView,
    PlaceUpdateView,
    PlaceDeleteView,
    dublicate_order_view,
    ManagerDetailView,
)
from apps.order import views
from apps.product.views import ProductListView, ManufacturerCreateView, SeriesCreateView, ColorCreateView

urlpatterns = [
    path("", views.index, name="index"),

    path("orders/", views.OrderListView.as_view(), name="orders_list"),
    # path("orders/<int:pk>/change_serie/", change_serie, name="change_serie"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/edit/", views.OrderUpdateView.as_view(), name="order_edit"),
    path("orders/<int:pk>/delete/", views.OrderDeleteView.as_view(), name="order_delete"),
    path("orders/create", views.OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/copy/", dublicate_order_view, name="order_copy"),
    path("managers/<int:pk>/", ManagerDetailView.as_view(), name="manager_detail"),
    path("clients/", views.ClientListView.as_view(), name="client_list"),
    path("clients/<int:pk>/", views.ClientDetailView.as_view(), name="client_detail"),
    path("clients/create/", views.ClientCreateView.as_view(), name="client_create"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer_create",
    ),
    path("series/create/", SeriesCreateView.as_view(), name="series_create"),
    path("color/create/", ColorCreateView.as_view(), name="color_create"),

    path("sets/<int:pk>/edit/", SetUpdateView.as_view(), name="set_edit"),
    path("sets/<int:pk>/delete/", SetDeleteView.as_view(), name="set_delete"),
    # path("sets/create/", set_create_view, name="set_create"),

    # path("place/<int:pk>/create/", create_place_view, name="place_create"),
    path("place/<int:pk>/update/", PlaceUpdateView.as_view(), name="place_update"),
    path("place/<int:pk>/delete/", PlaceDeleteView.as_view(), name="place_delete"),

    # path("login/", views.LoginView.as_view),
    # path("logout/", views.LogoutView.as_view),
]


app_name = "configurator"
