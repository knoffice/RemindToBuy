from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("profile", views.profile, name="profile"),
    path("product", views.product, name="product"),
    path("add_product", views.add_product, name="add_product"),
    path("save_product", views.save_product, name="save_product")
]