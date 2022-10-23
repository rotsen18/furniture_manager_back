from django import forms

from apps.order.models import Order


class OrderCreateForm(forms.Form):
    pass


# class OrderChangeForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ("serie",)
