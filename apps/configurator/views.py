from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

# from apps.configurator.forms import PlaceCreateForm, SetCreateForm
from apps.configurator.models import Set, OrderSet, Place
from apps.configurator.services.queries import copy_order


def dublicate_order_view(request, pk):
    new_order = copy_order(pk)
    return HttpResponseRedirect(reverse_lazy("configurator:order_detail", args=[new_order.id]))


class ManagerDetailView(LoginRequiredMixin, generic.DetailView):
    model = User


# def set_create_view(request):
#     size = request.GET.get("size")
#     order_id = request.GET.get("order", "")
#     order = Order.objects.get(id=order_id)
#     frame = Product.objects.filter(
#         component__name__contains="frame",
#         component__size=size,
#         series=order.serie,
#         color=order.frame_color
#     ).first()
#     form = SetCreateForm(initial={"size": size, "frame": frame})
#     if request.method == "POST":
#         form = SetCreateForm(request.POST)
#         if form.is_valid():
#             set_ = form.save()
#             OrderSet.objects.create(order=order, set=set_)
#             return HttpResponseRedirect(
#                 reverse("configurator:order_detail", args=[order.id]))
#         else:
#             print(form.errors)
#     return render(request, "configurator/set_form.html", {"form": form})


class SetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Set
    fields = "__all__"

    def get_success_url(self):
        order_id = OrderSet.objects.filter(set=self.object).first().order.id
        self.success_url = reverse_lazy("configurator:order_detail",
                                        args=[order_id])
        return str(self.success_url)


class SetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Set

    def get_success_url(self):
        order_id = OrderSet.objects.filter(set=self.object).first().order.id
        self.success_url = reverse_lazy("configurator:order_detail",
                                        args=[order_id])
        return str(self.success_url)


class OrderSetCreateView(LoginRequiredMixin, generic.CreateView):
    model = OrderSet
    fields = "__all__"
    success_url = reverse_lazy("configurator:orders_list")


# def change_serie(request, pk):
#     order = Order.objects.get(id=pk)
#     form = OrderChangeForm(instance=order)
#     products = get_products_list_in_order(order)
#     context = {"products": products, }
#     if request.method == "POST":
#         form = OrderChangeForm(request.POST)
#         if form.is_valid():
#             new_serie = form.cleaned_data["serie"]
#             new_order = change_order_serie(order, new_serie)
#             context["new_products"] = get_products_list_in_order(new_order)
#
#     context["form"] = form
#
#     return render(request, "configurator/order_change_serie.html",
#                   context=context)


# def create_place_view(request, pk):
#     set_ = Set.objects.get(id=pk)
#     order = set_.order_set.first()
#
#     if set_.places.count() >= set_.size:
#         return render(request, "configurator/place_too_mach.html")
#
#     form = PlaceCreateForm(initial={"set": set_})
#     form = get_filtered_fields_form(form, order)
#
#     if request.method == "POST":
#         form = PlaceCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(
#                 reverse("configurator:order_detail", args=[order.id]))
#         else:
#             print(form.errors)
#     context = {
#         "form": form,
#         "set": set_,
#         "order": order
#     }
#     return render(request, "configurator/place_form.html", context=context)


class PlaceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Place
    fields = ("mechanism", "cover", "additional")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["set"] = self.object.set
        context["order"] = self.object.set.order_set.first()

        return context

    def get_success_url(self):
        order_id = OrderSet.objects.filter(
            set=self.object.set).first().order.id
        self.success_url = reverse_lazy("configurator:order_detail",
                                        args=[order_id])
        return str(self.success_url)


class PlaceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Place

    def get_success_url(self):
        order_id = OrderSet.objects.filter(
            set=self.object.set).first().order.id
        self.success_url = reverse_lazy("configurator:order_detail",
                                        args=[order_id])

        return str(self.success_url)
