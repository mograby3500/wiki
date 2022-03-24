from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/edit_entry", views.edit_entry, name= "edit_entry"),
    path("wiki/new_entry", views.new_entry, name= "new_entry"),
    path("wiki/search_results", views.search_results, name="search_results"),
    path("wiki/random_entry", views.random_entry, name= "random_entry"),
    path("wiki/<str:title>", views.entery, name= "entery"),
]
