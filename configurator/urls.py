from django.urls import path
from django.contrib.auth import views

from configurator.models import OrderSet
from configurator.views import (
    index,
    change_q3,
    OrderListView,
    OrderDetailView,
    ClientListView,
    ClientDetailView,
    ProductListView,
    ManagerDetailView,
    OrderDeleteView,
    OrderCreateView,
    ClientCreateView,
    ManufacturerCreateView,
    SeriesCreateView,
    ColorCreateView,
    OrderUpdateView,
    SetUpdateView,
    SetDeleteView, copy_order
)


urlpatterns = [
    path("", index, name="index"),
    path("change_q3/", change_q3, name="change_q3"),
    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/edit/", OrderUpdateView.as_view(), name="order_edit"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
    path("orders/create", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/copy/", copy_order, name="order_copy"),
    path("managers/<int:pk>/", ManagerDetailView.as_view(), name="manager_detail"),
    path("clients/", ClientListView.as_view(), name="client_list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("clients/create/", ClientCreateView.as_view(), name="client_create"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("manufacturers/create/", ManufacturerCreateView.as_view(), name="manufacturer_create"),
    path("series/create/", SeriesCreateView.as_view(), name="series_create"),
    path("color/create/", ColorCreateView.as_view(), name="color_create"),
    path("sets/<int:pk>/edit/", SetUpdateView.as_view(), name="set_edit"),
    path("sets/<int:pk>/delete/", SetDeleteView.as_view(), name="set_delete"),
    #
    # path("login/", views.LoginView.as_view),
    # path("logout/", views.LogoutView.as_view),
]


app_name = "configurator"
