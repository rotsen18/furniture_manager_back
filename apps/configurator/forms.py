from django.forms import ModelForm

from apps.configurator.models import Place, Set


# class PlaceCreateForm(ModelForm):
#     class Meta:
#         model = Place
#         fields = ("mechanism", "cover", "additional")
#
#
# class SetCreateForm(ModelForm):
#     class Meta:
#         model = Set
#         fields = "__all__"