from django.shortcuts import render, redirect, get_object_or_404

from .form import ProductsForm, ProductImageForm
from .models import Product, ProductImage
from bulletin.models import Answer
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
import random
from django.db.models import Func

# aggregate 사용시 Round로 반올림 해주는 클래스
class Round(Func):
    function = "ROUND"
    template = "%(function)s(%(expressions)s, 1)"


# Create your views here.
def index(request):
    products = Product.objects.all()

    context = {
        "products": products,
    }
    return render(request, "products/index.html", context)


# Create your views here.
def products_create(request):
    if request.method == "POST":
        create_form = ProductsForm(request.POST, request.FILES)
        product_images = request.FILES.getlist("image")
        if create_form.is_valid():
            product = create_form.save()
            for img in product_images:
                ProductImage.objects.create(product=product, image=img)
            return redirect("/")
    else:
        create_form = ProductsForm()
        product_image_form = ProductImageForm()

    context = {
        "create_form": create_form,
        "product_image_form": product_image_form,
    }

    return render(request, "products/products_create.html", context)


def products_index(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products/products_index.html", context)


def products_detail(request, products_pk):
    product = get_object_or_404(Product, pk=products_pk)
    products = Product.objects.all()
    reviews = product.review_set.all()
    questions = product.question_set.filter(name=products_pk).order_by("-pk")
    total = product.review_set.aggregate(review_avg=Round(Avg("grade")))

    recommend_products = []
    pick_3 = random.sample(list(range(len(products))), 3)
    for i in pick_3:
        recommend_products.append(products[i])

    grades = (
        product.review_set.values("grade")
        .annotate(gra=Count("grade"))
        .order_by("-grade")
    )
    grades_1 = grades.filter(grade="1")
    grades_2 = grades.filter(grade="2")
    grades_3 = grades.filter(grade="3")
    grades_4 = grades.filter(grade="4")
    grades_5 = grades.filter(grade="5")
    context = {
        "product": product,
        "reviews": reviews,
        "questions": questions,
        "total": total,
        "recommend_products": recommend_products,
        "grades_1": grades_1,
        "grades_2": grades_2,
        "grades_3": grades_3,
        "grades_4": grades_4,
        "grades_5": grades_5,
    }

    return render(request, "products/products_detail.html", context)

# https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
# https://django.fun/en/qa/251566/
def products_update(request, products_pk):
    products = get_object_or_404(Product, pk=products_pk)
    product_images_all = products.product_image.all()

    if request.method == "POST":
        form = ProductsForm(request.POST, request.FILES, instance=products)
        product_images = request.FILES.getlist("image")
        if form.is_valid():
            product = form.save()
            for product_image in product_images_all:
                product_image.delete()
            for img in product_images:
                ProductImage.objects.create(product=product, image=img)
            return redirect("products:products_detail", products_pk)

    else:
        form = ProductsForm(instance=products)
        product_image_form = ProductImageForm()

    context = {
        "form": form,
        "product_image_form": product_image_form,
    }

    return render(request, "products/products_update.html", context)


def products_delete(request, products_pk):

    products = get_object_or_404(Product, pk=products_pk)
    products.delete()
    return redirect("/")


@login_required
def like(request, products_pk):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=products_pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
            is_liked = False
        else:
            product.like_users.add(request.user)
            is_liked = True
    else:
        return redirect("products:detail", products_pk)
    return JsonResponse(
        {
            "is_liked": is_liked,
            "like_count": product.like_users.count(),
        }
    )


def note(request):
    products = Product.objects.filter(category="노트/메모지")
    filter = request.GET.get("filter", default="register")
    discount = Product.objects.annotate(
        discount=F("pay") * (100 - F("sale")) * 0.01
    ).filter(category="노트/메모지")

    if filter == "high-sale":
        products = products.order_by("-sale")
    if filter == "high-price":
        products = discount.order_by("-discount")
    if filter == "low-price":
        products = discount.order_by("discount")
    if filter == "register":
        products = products.order_by("-created_at")

    context = {
        "category": "note",
        "products": products,
        "filter": filter,
    }

    return render(request, "products/index.html", context)


def diary(request):
    products = Product.objects.filter(category="다이어리")
    filter = request.GET.get("filter", default="register")
    discount = Product.objects.annotate(
        discount=F("pay") * (100 - F("sale")) * 0.01
    ).filter(category="다이어리")

    if filter == "high-sale":
        products = products.order_by("-sale")
    if filter == "high-price":
        products = discount.order_by("-discount")
    if filter == "low-price":
        products = discount.order_by("discount")
    if filter == "register":
        products = products.order_by("-created_at")

    context = {
        "category": "diary",
        "products": products,
        "filter": filter,
    }

    return render(request, "products/index.html", context)


def pencil(request):
    products = Product.objects.filter(category="필기류/필통")
    filter = request.GET.get("filter", default="register")
    discount = Product.objects.annotate(
        discount=F("pay") * (100 - F("sale")) * 0.01
    ).filter(category="필기류/필통")

    if filter == "high-sale":
        products = products.order_by("-sale")
    if filter == "high-price":
        products = discount.order_by("-discount")
    if filter == "low-price":
        products = discount.order_by("discount")
    if filter == "register":
        products = products.order_by("-created_at")

    context = {
        "category": "pencil",
        "products": products,
        "filter": filter,
    }

    return render(request, "products/index.html", context)


def file(request):
    products = Product.objects.filter(category="파일/바인더")
    filter = request.GET.get("filter", default="register")
    discount = Product.objects.annotate(
        discount=F("pay") * (100 - F("sale")) * 0.01
    ).filter(category="파일/바인더")

    if filter == "high-sale":
        products = products.order_by("-sale")
    if filter == "high-price":
        products = discount.order_by("-discount")
    if filter == "low-price":
        products = discount.order_by("discount")
    if filter == "register":
        products = products.order_by("-created_at")

    context = {
        "category": "file",
        "products": products,
        "filter": filter,
    }

    return render(request, "products/index.html", context)


def search(request):
    search = request.GET.get("search", "")
    search_list = Product.objects.filter(name__icontains=search)

    if search:
        if search_list:
            context = {
                "search": search,
                "search_list": search_list,
            }
            return render(
                request,
                "products/search.html",
                context,
            )
        else:
            return render(request, "products/searchfail.html")
    else:
        return render(request, "products/searchfail.html")


def searchfail(request):
    return render(request, "articles/searchfail.html")


def card(request):
    products = Product.objects.filter(category="크리스마스 카드")
    filter = request.GET.get("filter", default="register")
    christmas = request.GET.get("christmas", default="card")
    discount = Product.objects.annotate(
        discount=F("pay") * (100 - F("sale")) * 0.01
    ).filter(category="크리스마스 카드")

    if filter == "high-sale":
        products = products.order_by("-sale")
    if filter == "high-price":
        products = discount.order_by("-discount")
    if filter == "low-price":
        products = discount.order_by("discount")
    if filter == "register":
        products = products.order_by("-created_at")

    context = {
        "category": "card",
        "products": products,
        "filter": filter,
        "christmas": christmas,
    }
    return render(request, "products/index.html", context)


def decoration(request):
    products = Product.objects.filter(category="크리스마스 트리 장식")
    filter = request.GET.get("filter", default="register")
    christmas = request.GET.get("christmas", default="card")
    discount = Product.objects.annotate(
        discount=F("pay") * (100 - F("sale")) * 0.01
    ).filter(category="크리스마스 트리 장식")

    if filter == "high-sale":
        products = products.order_by("-sale")
    if filter == "high-price":
        products = discount.order_by("-discount")
    if filter == "low-price":
        products = discount.order_by("discount")
    if filter == "register":
        products = products.order_by("-created_at")

    context = {
        "category": "decoration",
        "products": products,
        "filter": filter,
        "christmas": christmas,
    }
    return render(request, "products/index.html", context)


def wreath(request):
    products = Product.objects.filter(category="크리스마스 리스")
    filter = request.GET.get("filter", default="register")
    christmas = request.GET.get("christmas", default="card")
    discount = Product.objects.annotate(
        discount=F("pay") * (100 - F("sale")) * 0.01
    ).filter(category="크리스마스 리스")

    if filter == "high-sale":
        products = products.order_by("-sale")
    if filter == "high-price":
        products = discount.order_by("-discount")
    if filter == "low-price":
        products = discount.order_by("discount")
    if filter == "register":
        products = products.order_by("-created_at")

    context = {
        "category": "wreath",
        "products": products,
        "filter": filter,
        "christmas": christmas,
    }
    return render(request, "products/index.html", context)
