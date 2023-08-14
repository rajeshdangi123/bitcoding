from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("", views.base, name="base "),
    # path("",include("app1.urls")),
]
