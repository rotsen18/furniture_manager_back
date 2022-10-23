from django.db import transaction

from apps.configurator.models import Manufacturer, Series, Product, Color, \
    Order, OrderSet, Set


def get_manufacturers():
    return [
        producer.name
        for producer in Manufacturer.objects.all()
    ]


def get_series(manufacturer: str):
    return [
        serie.name
        for serie in Series.objects.filter(manufacturer__name=manufacturer)
    ]


def get_types(serie: str):
    """
    get from db unique types and components by serie
    :return: {'Рамка': ['рамка 2х', 'рамка 1х'], 'Механізм': ['вимикач 1кл'],
    'Накладка': ['Клавіша 1кл вимикача']}
    """
    query = Product.objects.select_related(
        "color", "serie", "component",
        "manufacturer", "type_currency", "type").filter(series__name=serie) \
        .values("type__name", "component__name").distinct()
    result = {}
    for element in query:
        type_ = element["type__name"]
        component = element["component__name"]
        if type_ in result:
            result[type_].append(component)
        else:
            result[type_] = [component]

    return result


def get_colors(serie: str):
    """
    get from db unique colors for each type by serie
    :param serie:
    :return: {'Рамка': ['полярний білий', 'антрацит'],
    'Механізм': ['без кольору'], 'Накладка': ['полярний білий']}
    """
    query = Color.objects.filter(product__series__name=serie) \
        .values("product__type__name", "name").distinct()

    result = {}
    for element in query:
        type_ = element["product__type__name"]
        color = element["name"]
        if type_ in result:
            result[type_].append(color)
        else:
            result[type_] = [color]

    return result


def change_order_serie(order, new_serie):
    pk = order.id
    order.id = None
    order.save()
    new_order = order
    old_order = Order.objects.get(pk=pk)
    for old_set in old_order.sets.all():
        old_orderset = OrderSet.objects.get(set=old_set, order=old_order)
        frame = None
        if old_set.frame:
            frame = Product.objects.filter(
                series=new_serie,
                component=old_set.frame.component,
                color=old_set.frame.color
            ).first()

        new_set = Set.objects.create(
            size=old_set.size,
            frame=frame
        )
        OrderSet.objects.create(
            order=new_order, set=new_set, amount=old_orderset.amount
        )
        for place in old_set.places.all():
            mechanism = None
            if place.mechanism:
                mechanism = Product.objects.filter(
                    series=new_serie,
                    component=place.mechanism.component,
                    color=place.mechanism.color
                ).first()

            cover = None
            if place.cover:
                cover = Product.objects.filter(
                    series=new_serie,
                    component=place.cover.component,
                    color=place.cover.color
                ).first()

            additional = None
            if place.additional:
                additional = Product.objects.filter(
                    series=new_serie,
                    component=place.additional.component,
                    color=place.additional.color
                ).first()

            new_set.places.create(
                mechanism=mechanism,
                cover=cover,
                additional=additional,
            )

    return new_order


def get_list_with_kits(order):
    result = {"vertical": {}, "horizontal": {}}
    for i in range(1, 7):
        result["horizontal"][i] = []
        result["vertical"][i] = []

    order_sets = OrderSet.objects.filter(order=order)
    for order_set in order_sets:
        if order_set.set.frame:
            if "frame v" in order_set.set.frame.component.name:
                result["vertical"][order_set.set.size].append(order_set)
                continue
        result["horizontal"][order_set.set.size].append(order_set)

    return result


def get_products_list_in_order(order):
    products = {}
    for set_ in order.sets.all():
        if set_.frame:
            products[set_.frame] = products.get(set_.frame,
                                                     0) + 1
        for place in set_.places.all():
            if place.mechanism:
                products[place.mechanism] = products.get(place.mechanism,
                                                         0) + 1
            if place.cover:
                products[place.cover] = products.get(place.cover, 0) + 1
            if place.additional:
                products[place.additional] = products.get(place.additional,
                                                          0) + 1
    return products


def get_filtered_fields_form(form, order):
    form.fields["cover"].queryset = Product.objects.filter(
        type__name="cover",
        series=order.serie,
        color=order.cover_color
    )
    form.fields["mechanism"].queryset = Product.objects.filter(
        type__name="mechanism",
        series=order.serie,
        color__name__in=[order.cover_color.name, "no color"]
    )
    form.fields["additional"].queryset = Product.objects.filter(
        type__name="additional",
        series=order.serie,
        color__name__in=[order.cover_color.name, "no color"]
    )

    return form


def copy_order(order_id):
    order = Order.objects.get(pk=order_id)
    with transaction.atomic():
        order.id = None
        order.save()
        new_order = order
        old_order = Order.objects.get(pk=order_id)
        for old_set in old_order.sets.all():
            old_orderset = OrderSet.objects.get(set=old_set, order=old_order)
            new_set = Set.objects.create(
                size=old_set.size,
                frame=old_set.frame
            )
            OrderSet.objects.create(
                order=new_order, set=new_set, amount=old_orderset.amount
            )
            for place in old_set.places.all():
                new_set.places.create(
                    mechanism=place.mechanism,
                    cover=place.cover,
                    additional=place.additional,
                )
        return new_order

    return order
