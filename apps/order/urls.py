from django.urls import path

from apps.configurator.views import duplicate_order_view, change_serie
from apps.order import views


urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('orders/create', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/copy/', duplicate_order_view, name='order_copy'),
    path('orders/<int:pk>/change_serie/', change_serie, name='change_series'),
]

app_name = 'order'
