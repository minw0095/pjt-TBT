from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("products_create/", views.products_create, name="products_create"),
    path("<int:products_pk>/", views.products_detail, name="products_detail"),
    path("<int:products_pk>/update/", views.products_update, name="products_update"),
    path("<int:products_pk>/delete/", views.products_delete, name="products_delete"),
    path("<int:products_pk>/like/", views.like, name="like"),
    path("note/", views.note, name="note"),
    path("diary/", views.diary, name="diary"),
    path("pencil/", views.pencil, name="pencil"),
    path("file/", views.file, name="file"),
    path("search/", views.search, name="search"),
    path("searchfail/", views.searchfail, name="searchfail"),
    path("card/", views.card, name="card"),
    path("decoration/", views.decoration, name="decoration"),
    path("wreath/", views.wreath, name="wreath"),
]
