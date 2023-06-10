from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add_cart/<int:product_pk>/", views.add_cart, name="add_cart"),
    path("", views.cart_detail, name="cart_detail"),
    path("cart_remove/<int:product_pk>/", views.cart_remove, name="cart_remove"),
    # path("cart_delete/<int:product_pk>/", views.cart_delete, name="cart_delete"),
]
