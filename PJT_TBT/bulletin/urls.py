from django.urls import path
from . import views

app_name = "bulletin"

urlpatterns = [
    path("create/<int:product_pk>/", views.create, name="createQ"),
    path("delete/<int:question_pk>/", views.delete, name="deleteQ"),
    path("detail/<int:product_pk>/", views.detail, name="detailQ"),
    path("createA/<int:question_pk>/", views.createA, name="createA"),
    path("deleteA/<int:answer_pk>", views.deleteA, name="deleteA"),
    # path("update/<int:question_pk>/", views.update, name="update"),
    path("updateA/<int:answer_pk>/", views.updateA, name="updateA"),
]
