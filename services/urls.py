from django.urls import path
from .views import *


app_name = "services"

urlpatterns = [
    path("", services, name="services"),
    path("detail/", service_detail, name="detail")
]
