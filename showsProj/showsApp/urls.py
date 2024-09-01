from django.urls import path
from showsApp import views

urlpatterns = [
    path("", views.index),
    path("add/",views.addShow)
]