from django.forms import ModelForm, Form

from apps.configurator.models import Place, Set, Order


class OrderCreateForm(Form):
    pass


class OrderChangeForm(ModelForm):
    class Meta:
        model = Order
        fields = ("serie",)


class PlaceCreateForm(ModelForm):
    class Meta:
        model = Place
        fields = ("mechanism", "cover", "additional")


class SetCreateForm(ModelForm):
    class Meta:
        model = Set
        fields = "__all__"
