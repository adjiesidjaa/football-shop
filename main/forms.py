from django import forms
from django.forms import ModelForm
from .models import Product,Car

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "thumbnail", "is_featured"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-300"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-300",
                "rows": 4
            }),
            "price": forms.NumberInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-300"
            }),
            "category": forms.Select(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-lg bg-white focus:ring focus:ring-blue-300"
            }),
            "thumbnail": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring focus:ring-blue-300"
            }),
            "is_featured": forms.CheckboxInput(attrs={
                "class": "h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
            }),
        }

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["name","brand","stock"]
