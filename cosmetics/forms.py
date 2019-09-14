""" Forms """

from django import forms


class CartForm(forms.Form):
    product = forms.HiddenField()

