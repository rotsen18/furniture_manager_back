from django.forms import ModelForm, Form

from configurator.models import Place, Set, Order


class OrderCreateForm(Form):
    pass


class OrderChangeSerieForm(ModelForm):
    class Meta:
        model = Order
        fields = ("serie",)


class OrderChangeFrameColorForm(ModelForm):
    class Meta:
        model = Order
        fields = ("frame_color",)


class PlaceCreateForm(ModelForm):
    class Meta:
        model = Place
        fields = ("mechanism", "cover", "additional")


class SetCreateForm(ModelForm):
    class Meta:
        model = Set
        fields = "__all__"
