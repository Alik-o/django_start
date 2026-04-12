from django import forms

from catalog.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
