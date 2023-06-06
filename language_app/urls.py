from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_alone, name="home"),
    path("myhtmx/", views.myhtmx, name="myhtmx"),
    path("page/", views.page, name="page"),
]
