from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from configurator.forms import (
    PlaceCreateForm,
    SetCreateForm,
    OrderChangeSerieForm,
    OrderChangeFrameColorForm
)
from configurator.models import (
    Order,
    Product,
    Manager,
    Client,
    Manufacturer,
    Series,
    Color,
    Set,
    OrderSet,
    Place,
)
from configurator.queries import (
    get_products_list_in_order,
    get_list_with_kits,
    get_filtered_fields_form,
    copy_order,
    change_order_serie,
    change_order_frame_color, get_colors, get_choices, get_series
)


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("configurator:orders_list"))

    return render(request, "configurator/index.html")


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


def dublicate_order_view(request, pk):
    new_order = copy_order(pk)
    return HttpResponseRedirect(reverse_lazy("configurator:order_detail", args=[new_order.id]))


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
    success_url = reverse_lazy("configurator:index")


class ColorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Color
    fields = "__all__"
    success_url = reverse_lazy("configurator:index")


def set_create_view(request):
    size = request.GET.get("size")
    order_id = request.GET.get("order", "")
    order = Order.objects.get(id=order_id)
    frame = Product.objects.filter(
        component__name__contains="frame",
        component__size=size,
        series=order.serie,
        color=order.frame_color
    ).first()
    form = SetCreateForm(initial={"size": size, "frame": frame})
    if request.method == "POST":
        form = SetCreateForm(request.POST)
        if form.is_valid():
            set_ = form.save()
            OrderSet.objects.create(order=order, set=set_)
            return HttpResponseRedirect(
                reverse("configurator:order_detail", args=[order.id]))
        else:
            print(form.errors)
    return render(request, "configurator/set_form.html", {"form": form})


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


def change_serie(request, pk):
    order = Order.objects.get(id=pk)
    products = get_products_list_in_order(order)
    context = {"products": products, }

    form = OrderChangeSerieForm(instance=order)
    choices = get_choices(get_series(order.manufacturer))
    form.fields["serie"].choices = choices

    if request.method == "POST":
        form = OrderChangeSerieForm(request.POST)
        form.fields["serie"].choices = choices
        if form.is_valid():
            new_serie = form.cleaned_data["serie"]
            new_data = change_order_serie(order, new_serie)
            context["new_products"] = get_products_list_in_order(
                new_data["order"]
            )
            context["missing_products"] = new_data["missing_products"]
            context["multiple_products"] = new_data["multiple_products"]
            context["new_order_id"] = new_data["order"].id

    context["form"] = form
    context["old_order_id"] = order.id

    return render(
        request,
        "configurator/order_change_serie.html",
        context=context
    )


def change_frame_color(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderChangeFrameColorForm(instance=order)
    choices = get_choices(get_colors(order.serie)["frame"])
    form.fields["frame_color"].choices = choices
    products = get_products_list_in_order(order)
    context = {"products": products, }
    if request.method == "POST":
        form = OrderChangeFrameColorForm(request.POST)
        if form.is_valid():
            new_color = form.cleaned_data["frame_color"]
            new_data = change_order_frame_color(order, new_color)
            context["new_products"] = get_products_list_in_order(
                new_data["order"]
            )
            context["missing_products"] = new_data["missing_products"]
            context["multiple_products"] = new_data["multiple_products"]
            context["new_order_id"] = new_data["order"].id

    context["old_order_id"] = order.id
    context["form"] = form

    return render(
        request,
        "configurator/order_change_serie.html",
        context=context
    )


def create_place_view(request, pk):
    set_ = Set.objects.get(id=pk)
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
                reverse("configurator:order_detail", args=[order.id]))
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
