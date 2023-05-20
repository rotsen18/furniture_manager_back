from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.catalogue.models.product import Manufacturer, Series, Product


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product


class SeriesCreateView(LoginRequiredMixin, generic.CreateView):
    model = Series
    fields = '__all__'
    success_url = reverse_lazy('configurator:index')


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = '__all__'
    success_url = reverse_lazy('configurator:index')
