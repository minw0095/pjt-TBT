from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:user_pk>/detail/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("changeps/", views.changeps, name="changeps"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("<int:user_pk>/order_list/", views.order_list, name="order_list"),
    path("<int:user_pk>/wishlist/", views.wishlist, name="wishlist"),
    path("<int:user_pk>/review_list/", views.review_list, name="review_list"),
    # path("<int:user_pk>/like_delete/", views.like_delete, name="like_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
