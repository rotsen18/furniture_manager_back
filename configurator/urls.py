from django.urls import path

from configurator.views import (
    index,
    change_serie,
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
    SetDeleteView,
    set_create_view,
    create_place_view,
    PlaceUpdateView,
    PlaceDeleteView,
    dublicate_order_view,
    change_frame_color,
)


urlpatterns = [
    path("", index, name="index"),

    path("orders/", OrderListView.as_view(), name="orders_list"),
    path("orders/<int:pk>/change_serie/", change_serie, name="change_serie"),
    path("orders/<int:pk>/change_frame_color/", change_frame_color, name="change_frame_color"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("orders/<int:pk>/edit/", OrderUpdateView.as_view(), name="order_edit"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
    path("orders/create", OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/copy/", dublicate_order_view, name="order_copy"),

    path("managers/<int:pk>/", ManagerDetailView.as_view(), name="manager_detail"),

    path("clients/", ClientListView.as_view(), name="client_list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("clients/create/", ClientCreateView.as_view(), name="client_create"),

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
    path("sets/create/", set_create_view, name="set_create"),

    path("place/<int:pk>/create/", create_place_view, name="place_create"),
    path("place/<int:pk>/update/", PlaceUpdateView.as_view(), name="place_update"),
    path("place/<int:pk>/delete/", PlaceDeleteView.as_view(), name="place_delete"),

]


app_name = "configurator"
