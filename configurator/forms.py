from django.forms import ModelForm, Form

from configurator.models import Place, Set


class OrderCreateForm(Form):
    pass


class PlaceCreateForm(ModelForm):
    class Meta:
        model = Place
        fields = ("mechanism", "cover", "additional")


class SetCreateForm(ModelForm):
    class Meta:
        model = Set
        fields = "__all__"
