from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404

from .forms import CreateUserForm, ProductForm, WishListForm
from .models import Wishlist, Product
#color: lightcoral;
#BASE_DIR = Path(__file__).resolve().parent.parent
#'NAME': BASE_DIR / 'db.sqlite3',


def index(request):
    context = {
        'title': 'Home',
        'username': request.user,
        'user_id': request.user.id,
    }

    return render(request, 'index.html', context)


@login_required(login_url='login_page')
def user_wishlists(request, username):
    username = request.user
    user_id = request.user.id
    wishlists = get_list_or_404(Wishlist, owner=username)

    if request.method == 'POST':
        form = WishListForm(request.POST)
        instance_wishlist = form.save()
        Wishlist.save(instance_wishlist)

        return redirect('user_wishlists', username)

    elif request.method == 'GET':
        context = {
            'title': str(username) + 's wishlists',
            'wishlists': wishlists,
            'is_owner_list': wishlists[0].owner == request.user,
            'username': username,
            'user_id': user_id,
        }

        return render(request, 'user_wishlists.html', context)


@login_required(login_url='login_page')
def delete_wish(request, wishlist_pk, product_pk):
    username = request.user
    wishlist = get_object_or_404(Wishlist, pk=wishlist_pk)
    pr = get_object_or_404(Product, pk=product_pk)
    wishlist.product.remove(pr)

    return redirect('user_wishlists', username)


@login_required(login_url='login_page')
def delete_wishlist(request, wishlist_pk):
    username = request.user
    wishlist = get_object_or_404(Wishlist, pk=wishlist_pk)
    Wishlist.delete(wishlist)

    return redirect('user_wishlists', username)


@login_required(login_url='login_page')
def add_wish(request, username, wishlist_pk):
    username = request.user
    wishlist = get_object_or_404(Wishlist, pk=wishlist_pk)

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
            'form': form,
            'wishlist': wishlist,
        }

        return render(request, 'add_wish.html', context)


@login_required(login_url='login_page')
def user_shoplists(request, username):
    username = request.user
    context = {
        'title': str(username) + 's shopping lists',
        'username': request.user,
        'user_id': request.user.id,
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
