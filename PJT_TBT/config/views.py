from django.shortcuts import render, get_object_or_404
from products.models import Product


def index(request):
    sale_under_40 = get_object_or_404(Product, pk=26)
    sale_under_30 = get_object_or_404(Product, pk=47)
    sale_under_20 = get_object_or_404(Product, pk=129)
    weekly_planner = get_object_or_404(Product, pk=65)
    monthly_planner = get_object_or_404(Product, pk=57)
    photo_album = get_object_or_404(Product, pk=87)

    season_products = [
        get_object_or_404(Product, pk=263),
        get_object_or_404(Product, pk=166),
        get_object_or_404(Product, pk=201),
    ]

    context = {
        "sale_under_40": sale_under_40,
        "sale_under_30": sale_under_30,
        "sale_under_20": sale_under_20,
        "weekly_planner": weekly_planner,
        "monthly_planner": monthly_planner,
        "photo_album": photo_album,
        "season_products": season_products,
    }

    return render(request, "index.html", context)
