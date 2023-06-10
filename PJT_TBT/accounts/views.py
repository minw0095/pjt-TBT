from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomCreationUserForm, CustomChangeUserForm
from .forms import CustomAuthenticationForm
from products.models import Product, ProductImage
from .models import User
from reviews.models import Review
from orders.models import Order, OrderItem
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.


def index(request):
    users = get_user_model().objects.all()
    context = {"users": users}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomCreationUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect("index")
    else:
        form = CustomCreationUserForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "index")
    else:
        form = CustomAuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("index")


def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    reviews = get_user_model().objects.get(pk=user_pk).review_set.all()

    orders = []
    order_items = get_user_model().objects.get(pk=user_pk).orderitem_set.all()
    for item in order_items:
        if item.order_set.all():
            orders.append(item.order_set.all())
    orders.reverse()
    print(orders)

    context = {
        "user": user,
        "my": request.user,
        "reviews": reviews,
        'orders': orders,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def update(request):
    if request.method == "POST":
        form = CustomChangeUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomChangeUserForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:signup")


def changeps(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("accounts:update")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/change_ps.html", {"form": form})


@login_required
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user != get_user_model().objects.get(pk=user_pk):
        if request.user not in get_user_model().objects.get(pk=user_pk).followers.all():
            request.user.followings.add(get_user_model().objects.get(pk=user_pk))
            is_follow = True
        else:
            request.user.followings.remove(get_user_model().objects.get(pk=user_pk))
            is_follow = False
        context = {
            "isFollow": is_follow,
            "followers_count": user.followers.count(),
            "followings_count": user.followings.count(),
        }

    return JsonResponse(context)


def order_list(request, user_pk):
    users = get_user_model().objects.get(pk=user_pk)

    order_list = []
    order_items = get_user_model().objects.get(pk=user_pk).orderitem_set.all()
    for item in order_items:
        if item.order_set.all():
            order_list.append(item.order_set.all())
    order_list.reverse()
    print(order_list)

    context = {
        "users": users,
        'order_list': order_list,
    }
    return render(request, "accounts/order_list.html", context)


def wishlist(request, user_pk):
    users = get_user_model().objects.get(pk=user_pk)
    like_product = users.like_products.all()
    if request.method == "POST":
        selected = request.POST.getlist("answer[]")
        for product in selected:
            for i in range(len(like_product)):
                if int(product) == like_product[i].pk:
                    like_product[i].delete()
    context = {"users": users}
    return render(request, "accounts/wishlist.html", context)


def review_list(request, user_pk):
    users = get_user_model().objects.get(pk=user_pk)
    reviews = get_user_model().objects.get(pk=user_pk).review_set.all()
    context = {
        "users": users,
        "reviews": reviews,
    }
    return render(request, "accounts/review_list.html", context)
