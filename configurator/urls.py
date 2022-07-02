from django.urls import path
from django.contrib.auth import views

from configurator.views import index, change_q3, orders_list, order_detail, \
    manager_detail, new_order, clients_list, client_detail, products_list, \
    order_edit

urlpatterns = [
    path("", index, name="index"),
    path("change_q3/", change_q3, name="change_q3"),
    path("orders/", orders_list, name="orders_list"),
    path("orders/<int:pk>/", order_detail, name="order_detail"),
    path("orders/edit/<int:pk>/", order_edit, name="order_edit"),
    path("new_order/", new_order, name="new_order"),
    path("manager/", manager_detail, name="manager_detail"),
    path("clients/", clients_list, name="clients_list"),
    path("clients/<int:pk>/", client_detail, name="client_detail"),
    path("products/", products_list, name="products_list"),
    path("login/", views.LoginView.as_view),
    path("logout/", views.LogoutView.as_view),
]


app_name = "configurator"
