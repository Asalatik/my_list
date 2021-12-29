from django.contrib import admin
from .models import Product, Wishlist, Shoplist


admin.site.register(Wishlist)
admin.site.register(Product)
admin.site.register(Shoplist)
