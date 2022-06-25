from django import forms
from store.models import Customer,Product


class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer

class ProductForm (forms.ModelForm):
    price = forms.FloatField()

    class Meta:
        model = Product 
