from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("myhtmx/", views.myhtmx, name="myhtmx"),
    path("page/", views.page, name="page"),
]
