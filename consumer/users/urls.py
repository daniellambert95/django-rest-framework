from django.contrib import admin
from django.urls import path

from .views import (
    index,
    user_info_view,
    list_of_users,
    list_of_books,
    list_of_cars,
)


urlpatterns = [
    path("", index),
    path("users/", list_of_users, name="users" ),
    path("users/<int:pk>/", user_info_view, name="user-info" ),
    path("cars/",  list_of_cars, name="cars" ),
    path("books/", list_of_books, name="books" ),
]
