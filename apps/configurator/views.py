from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from apps.catalogue.models.product import Product
from apps.configurator.forms import SetCreateForm, PlaceCreateForm
# from apps.configurator.forms import PlaceCreateForm, SetCreateForm
from apps.configurator.models import PlaceSet, Place
from apps.order.forms import OrderChangeForm
from apps.order.models import OrderSet, Order
from apps.configurator.services.queries import (
    copy_order, get_products_list_in_order, change_order_serie,
    get_filtered_fields_form,
)


def duplicate_order_view(request, pk):
    new_order = copy_order(pk)
    return HttpResponseRedirect(reverse_lazy("order:order_detail", args=[new_order.id]))


class ManagerDetailView(LoginRequiredMixin, generic.DetailView):
    model = User


def set_create_view(request):
    size = request.GET.get("size")
    order_id = request.GET.get("order", "")
    order = Order.objects.get(id=order_id)
    frame = Product.objects.filter(
        component__name__contains="frame",
        component__size=size,
        series=order.series,
        color=order.frame_color
    ).first()
    form = SetCreateForm(initial={"size": size, "frame": frame})
    if request.method == "POST":
        form = SetCreateForm(request.POST)
        if form.is_valid():
            place_set_ = form.save()
            OrderSet.objects.create(order=order, place_set=place_set_)
            return HttpResponseRedirect(
                reverse("order:order_detail", args=[order.id]))
        else:
            print(form.errors)
    return render(request, "configurator/set_form.html", {"form": form})


class SetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = PlaceSet
    fields = "__all__"

    def get_success_url(self):
        order_id = OrderSet.objects.filter(set=self.object).first().order.id
        self.success_url = reverse_lazy("order:order_detail",
                                        args=[order_id])
        return str(self.success_url)


class SetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PlaceSet

    def get_success_url(self):
        order_id = OrderSet.objects.filter(place_set=self.object).first().order.id
        self.success_url = reverse_lazy("order:order_detail",
                                        args=[order_id])
        return str(self.success_url)


class OrderSetCreateView(LoginRequiredMixin, generic.CreateView):
    model = OrderSet
    fields = "__all__"
    success_url = reverse_lazy("order:orders_list")


def change_serie(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderChangeForm(instance=order)
    products = get_products_list_in_order(order)
    context = {"products": products, }
    if request.method == "POST":
        form = OrderChangeForm(request.POST)
        if form.is_valid():
            new_serie = form.cleaned_data["serie"]
            new_order = change_order_serie(order, new_serie)
            context["new_products"] = get_products_list_in_order(new_order)

    context["form"] = form

    return render(request, "order/order_change_serie.html",
                  context=context)


def create_place_view(request, pk):
    set_ = PlaceSet.objects.get(id=pk)
    order = set_.order_set.first()

    if set_.places.count() >= set_.size:
        return render(request, "configurator/place_too_mach.html")

    form = PlaceCreateForm(initial={"set": set_})
    form = get_filtered_fields_form(form, order)

    if request.method == "POST":
        form = PlaceCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("order:order_detail", args=[order.id]))
        else:
            print(form.errors)
    context = {
        "form": form,
        "set": set_,
        "order": order
    }
    return render(request, "configurator/place_form.html", context=context)


class PlaceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Place
    fields = ("mechanism", "cover", "additional")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["set"] = self.object.place_set
        context["order"] = self.object.place_set.order_set.first()

        return context

    def get_success_url(self):
        order_id = OrderSet.objects.filter(
            set=self.object.place_set).first().order.id
        self.success_url = reverse_lazy("order:order_detail",
                                        args=[order_id])
        return str(self.success_url)


class PlaceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Place

    def get_success_url(self):
        order_id = OrderSet.objects.filter(
            set=self.object.place_set).first().order.id
        self.success_url = reverse_lazy("order:order_detail",
                                        args=[order_id])

        return str(self.success_url)
