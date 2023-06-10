from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_POST
from django.core import serializers

# Create your views here.
def index(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    reviews = product.review_set.all()
    grade = 0
    cnt = 0
    for review in reviews:
        grade += review.grade
        cnt += 1
    if grade:
        grade /= cnt
    context = {
        "reviews": reviews,
        "product": product,
        "grade": grade,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.account = request.user
            review.save()
            return redirect("products:products_detail", product_pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return redirect(request, "products/products_detail.html", context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    product_pk = review.product.pk
    if request.user.pk == review.account.pk:
        review.delete()
    return redirect("products:products_detail", product_pk)


@login_required
def update(
    request,
    review_pk,
):
    cnt = Review.objects.count()
    review = Review.objects.get(pk=review_pk)
    reviewForm = list(Review.objects.values())
    is_update = False
    product_pk = review.product.pk
    if request.user.pk == review.account.pk:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            # data = list(review_form.values())
            is_update = True
            if review_form.is_valid():
                review_form.save()
                return redirect("products:products_detail", product_pk)
        else:
            review_form = ReviewForm(instance=review)
            is_update = False
            reviewForm = review_form.values()
            return JsonResponse(
                reviewForm,
                safe=False,
            )
    else:
        return JsonResponse(
            reviewForm,
            safe=False,
        )
    return JsonResponse(
        reviewForm,
        safe=False,
    )

    # return render(request, "reviews/update.html", context)


# @login_required
# def likes(request, review_pk):
#     review = Review.objects.get(pk=review_pk)
#     print(review)
#     if request.user.is_authenticated:
#         if request.user.pk != review.account.pk:
#             if review.like.filter(pk=request.user.pk).exists():
#                 review.like.remove(request.user)
#                 is_likes = False
#             else:
#                 review.like.add(request.user)
#                 is_likes = True
#     context = {"islikes": is_likes, "likecount": review.like.all().count()}
#     return JsonResponse(context)


# def likes(request, review_pk):
#     if request.user.is_authenticated:
#         review = Review.objects.get(pk=review_pk)
#         if review.like_users.filter(pk=request.user.pk).exists():
#             review.like_users.remove(request.user)
#             is_liked = False
#         else:
#             review.like_users.add(request.user)
#             is_liked = True
#         context = {
#             "is_liked": is_liked,
#         }
#         return JsonResponse(context)
#     return redirect("accounts:login")


def likes(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user in review.like.all():
        review.like.remove(request.user)
        is_liked = False
    else:
        review.like.add(request.user)
        is_liked = True
    context = {
        "isLiked": is_liked,
        "likeCount": review.like.count(),
    }
    return JsonResponse(context)
