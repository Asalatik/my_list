from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import Product, Wishlist, Shoplist


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'link', 'image', 'price', 'money', 'note']


class WishListForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'is_hidden', 'owner']


class ShopListForm(forms.ModelForm):
    class Meta:
        model = Shoplist
        fields = ['title', 'is_hidden', 'owner']


class ShopproductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'product_type']
