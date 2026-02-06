from django.urls import path

from .views import *

app_name = "properties"

urlpatterns = [
    path("", properties, name="properties"),
]