from django.urls import path
from .views import *



urlpatterns = [
    path("last-services/", last_services, name="last-services"),
    path("categories/", categories, name="categories"),
    ]
