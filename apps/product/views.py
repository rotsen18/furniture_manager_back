from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.product.models import Product, Manufacturer, Series, Color


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"


class SeriesCreateView(LoginRequiredMixin, generic.CreateView):
    model = Series
    fields = "__all__"
    success_url = reverse_lazy("configurator:index")


class ColorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Color
    fields = "__all__"
    success_url = reverse_lazy("configurator:index")