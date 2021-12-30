from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User

from .forms import CreateUserForm, ProductForm, WishListForm, ShopListForm, ShopproductForm
from .models import Wishlist, Product, Shoplist


def index(request):
    user_login = request.user
    context = {
        'title': 'Home',
        'username': user_login,
        'user_id': request.user.id,
        'user': user_login,
    }

    return render(request, 'index.html', context)


@login_required(login_url='login_page')
def user_wishlists(request, username):
    user_login = request.user
    user_id = request.user.id
    user = get_object_or_404(User, username=username)
    try:
        wishlists = get_list_or_404(Wishlist, owner=user)
        if request.method == 'POST':

            form = WishListForm(request.POST)
            instance_wishlist = form.save()
            Wishlist.save(instance_wishlist)

            return redirect('user_wishlists', username)

        elif request.method == 'GET':
            context = {
                'title': str(username) + 's wishlists',
                'wishlists': wishlists,
                'is_owner_list': wishlists[0].owner == user_login,
                'username': username,
                'user': user_login,
                'user_id': user_id,
            }

            return render(request, 'user_wishlists.html', context)

    except:
        if request.method == 'POST':

            form = WishListForm(request.POST)
            instance_wishlist = form.save()
            Wishlist.save(instance_wishlist)

            return redirect('user_wishlists', username)

        elif request.method == 'GET':
            context = {
                'title': str(username) + 's wishlists',
                'wishlists': None,
                'is_owner_list': user == user_login,
                'username': username,
                'user': user_login,
                'user_id': user_id,
            }

            return render(request, 'user_wishlists.html', context)


@login_required(login_url='login_page')
def delete_wish(request, wishlist_title, product_pk):
    user_login = request.user
    try:
        wishlist = get_object_or_404(Wishlist, title=wishlist_title)
        pr = get_object_or_404(Product, pk=product_pk)
        wishlist.product.remove(pr)

        return redirect('user_wishlists', user_login)
    except:
        shoplist = get_object_or_404(Shoplist, title=wishlist_title)
        pr = get_object_or_404(Product, pk=product_pk)
        shoplist.product.remove(pr)

        return redirect('user_shoplists', user_login)


@login_required(login_url='login_page')
def delete_wishlist(request, wishlist_pk):
    user_login = request.user
    wishlist = get_object_or_404(Wishlist, pk=wishlist_pk)
    Wishlist.delete(wishlist)

    return redirect('user_wishlists', user_login)


@login_required(login_url='login_page')
def delete_shoplist(request, shoplist_pk):
    user_login = request.user
    shoplist = get_object_or_404(Shoplist, pk=shoplist_pk)
    Shoplist.delete(shoplist)

    return redirect('user_shoplists', user_login)


@login_required(login_url='login_page')
def add_wish(request, username, wishlist_title):
    """
    попробовать pk заменить на title
    """
    username = request.user
    try:
        wishlist = get_object_or_404(Wishlist, title=wishlist_title)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                instance_product = form.save()
                wishlist.product.add(instance_product)
                wishlist.save()

                return redirect('user_wishlists', username)

        elif request.method == 'GET':
            form = ProductForm
            context = {
                'title': 'add wish in ' + str(wishlist),
                'username': username,
                'user_id': request.user.id,
                'user': request.user,
                'form': form,
                'wishlist': wishlist,
            }

            return render(request, 'add_wish.html', context)
    except:
        shoplist = get_object_or_404(Shoplist, title=wishlist_title)
        if request.method == 'POST':
            form = ShopproductForm(request.POST)

            if form.is_valid():
                instance_product = form.save()
                shoplist.product.add(instance_product)
                shoplist.save()

                return redirect('user_shoplists', username)

        elif request.method == 'GET':
            form = ShopproductForm
            context = {
                'title': 'add product in ' + str(shoplist),
                'username': username,
                'user_id': request.user.id,
                'user': request.user,
                'form': form,
                'shoplist': shoplist,
            }

            return render(request, 'add_product.html', context)


@login_required(login_url='login_page')
def user_shoplists(request, username):
    user_login = request.user
    user_id = request.user.id
    user = get_object_or_404(User, username=username)
    try:
        shoplists = get_list_or_404(Shoplist, owner=user)
        if request.method == 'POST':

            form = ShopListForm(request.POST)
            instance_shoplist = form.save()
            Shoplist.save(instance_shoplist)

            return redirect('user_shoplists', username)

        elif request.method == 'GET':
            context = {
                'title': str(username) + 's shopping lists',
                'shoplists': shoplists,
                'is_owner_list': shoplists[0].owner == user_login,
                'username': username,
                'user': user_login,
                'user_id': user_id,
            }

            return render(request, 'user_shoplists.html', context)

    except:
        if request.method == 'POST':

            form = ShopListForm(request.POST)
            instance_shoplist = form.save()
            Wishlist.save(instance_shoplist)

            return redirect('user_shoplists', username)

        elif request.method == 'GET':
            context = {
                'title': str(username) + 's shopping lists',
                'shoplists': None,
                'is_owner_list': user == user_login,
                'username': username,
                'user': user_login,
                'user_id': user_id,
            }

            return render(request, 'user_shoplists.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                return redirect('login_page')

        context = {'form': form, 'title': 'Register account'}
        return render(request, 'register_page.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index_page')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {'title': 'Login'}
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page')
