from configurator.models import Manufacturer, Series, Product, Type, Color, \
    Order, OrderSet


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
        "manufacturer", "type_currency", "type").filter(series__name=serie)\
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
    query = Color.objects.filter(product__series__name=serie)\
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


def change_serie(new_serie: str):
    pass


def get_list_with_kits(order):
    sets = order.sets.all()
    # TODO finish query
    result = {"vertical": {}, "horizontal": {}}
    for i in range(1, 7):
        result["horizontal"][i] = []
        result["vertical"][i] = []

    order_sets = OrderSet.objects.filter(order=order)
    for order_set in order_sets:
        if order_set.set.products.filter(component__name__contains="frame v").exists():
            result["vertical"][order_set.set.size].append(order_set)
        else:
            result["horizontal"][order_set.set.size].append(order_set)

    return result


def get_products_list_in_order(order):
    products = {}
    for set_ in order.sets.all():
        for product in set_.products.all():
            products[product] = products.get(product, 0) + 1
    return products

