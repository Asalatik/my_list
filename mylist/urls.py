"""mylist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import index, register_user, login_user, logout_user, user_wishlists, user_shoplists, delete_wish_or_product, edit_list, delete_wishlist, delete_shoplist


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index_page'),
    path('register_page/', register_user, name='register_page'),
    path('login/', login_user, name='login_page'),
    path('logout/', logout_user, name='logout_page'),
    path('my_wishlists/<str:username>', user_wishlists, name='user_wishlists'),
    path('my_shoplists/<str:username>', user_shoplists, name='user_shoplists'),
    path('delete_wish_or_product/<str:type_page>/<str:list_type>/<int:list_pk>/<int:product_pk>', delete_wish_or_product, name='delete_wish_or_product'),
    path('<str:list_type>/<str:username>/<int:list_pk>', edit_list, name='edit_list'),
    path('delete_wishlist/<int:wishlist_pk>', delete_wishlist, name='delete_wishlist'),
    path('delete_shoplist/<int:shoplist_pk>', delete_shoplist, name='delete_shoplist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
