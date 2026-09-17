from django.urls import path
from .views import *

app_name = "api_root"

urlpatterns = [
    path("last-services/", last_services, name="last-services"),
    path("categories/", categories, name="categories"),
]
