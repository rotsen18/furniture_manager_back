from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from configurator.models import Order, Product, Manager, Client


@login_required
def index(request):

    context = {
        "orders_count": Order.objects.filter(manager=request.user).count(),
        "clients_count": Client.objects.filter(orders__manager=request.user).distinct().count()
    }
    return render(request, "configurator/index.html", context=context)


@login_required
def orders_list(request):

    context = {
        "orders": Order.objects.filter(manager=request.user)
    }
    return render(request, "configurator/orders_list.html", context=context)


@login_required
def order_detail(request, pk):

    context = {
        "order": Order.objects.get(id=pk)
    }
    return render(request, "configurator/order_detail.html", context=context)


@login_required
def order_edit(request, pk):
    order = Order.objects.get(id=pk)

    context = {
        "order": order
    }
    return render(request, "configurator/edit_order.html", context=context)


@login_required
def new_order(request):
    context = {

    }

    return render(request, "configurator/new_order.html", context=context)


@login_required
def manager_detail(request):

    context = {
        "user": request.user
    }
    return render(request, "configurator/manager_detail.html", context=context)


@login_required
def clients_list(request):
    context = {
        "clients": Client.objects.filter(orders__manager=request.user).distinct(),

    }

    return render(request, "configurator/clients_list.html", context=context)


@login_required
def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    all_orders = Order.objects.filter(client_id=pk)
    manager_orders = all_orders.filter(manager=request.user)

    context = {
        "client": client,
        "orders": manager_orders,
        "total_orders_count": all_orders.count(),
    }

    return render(request, "configurator/client_detail.html", context=context)


@login_required
def products_list(request):
    context = {
        "products": Product.objects.all()
    }

    return render(request, "configurator/products_list.html", context=context)


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