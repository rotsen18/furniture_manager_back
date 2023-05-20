from django.forms import ModelForm

from apps.configurator.models import Place, PlaceSet


class PlaceCreateForm(ModelForm):
    class Meta:
        model = Place
        fields = ("mechanism", "cover", "additional")


class SetCreateForm(ModelForm):
    class Meta:
        model = PlaceSet
        fields = "__all__"
