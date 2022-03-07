# Source: https://www.django-rest-framework.org/tutorial/quickstart/

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"cars", views.CarViewSet)
router.register(r"books", views.BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
