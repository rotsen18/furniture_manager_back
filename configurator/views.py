from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from configurator.models import Order, Product, Manager, Client, Manufacturer, \
    Series, Color


@login_required
def index(request):

    context = {
        "orders_count": Order.objects.filter(manager=request.user).count(),
        "clients_count": Client.objects.filter(orders__manager=request.user).distinct().count()
    }
    return render(request, "configurator/index.html", context=context)


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    queryset = Order.objects.all()

    def get_queryset(self):
        return self.queryset.filter(manager=self.request.user)


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("configurator:orders_list")


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    fields = [
        "client",
        "manager",
        "description",
        "manufacturer",
        "serie",
        "mech_color",
        "cover_color",
        "frame_color"
    ]
    success_url = reverse_lazy("configurator:orders_list")


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    fields = [
        "client",
        "manager",
        "description",
        "manufacturer",
        "serie",
        "mech_color",
        "cover_color",
        "frame_color"
    ]


class ManagerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manager


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Client
    fields = "__all__"


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy("configurator:client_list")


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"


class SeriesCreateView(LoginRequiredMixin, generic.CreateView):
    model = Series
    fields = "__all__"


class ColorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Color
    fields = "__all__"


@login_required
def change_q3(request):
    order = Order.objects.get(id=1)
    new_products = []
    for set_ in order.sets.all():
        for product in set_.products.all():
            queryset = Product.objects.filter(
                manufacturer=product.manufacturer,
                series__name__in=["Q3"],
                type=product.type,
                component=product.component,
                color=product.color,
            )
            new_products.append(queryset.first())
    context = {
        "products": new_products
    }

    return render(request, "configurator/changed_products.html", context=context)