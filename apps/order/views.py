from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from apps.configurator.services.queries import get_list_with_kits, get_products_list_in_order
from apps.order.models import Order
from apps.order.models.client import Client


@login_required
def index(request):
    context = {
        "orders_count": Order.objects.filter(manager=request.user).count(),
        "clients_count": -1,
    }
    return render(request, "configurator/index.html", context=context)


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    queryset = Order.objects.all()

    def get_queryset(self):
        return self.queryset.filter(manager=self.request.user)


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_sets = get_list_with_kits(self.object)
        products = get_products_list_in_order(self.object)

        context.update(order_sets)
        context["products"] = products

        return context


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
        "frame_color",
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
        "frame_color",
    ]


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Client
    fields = "__all__"


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy("configurator:client_list")
