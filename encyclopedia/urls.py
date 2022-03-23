from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search_results", views.search_results, name="search_results"),
    path("wiki/<str:title>", views.entery, name= "entery"),
]
