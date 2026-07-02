from django.urls import path
from .views import *



urlpatterns = [
    path("", services, name="services"),
    path("detail/<int:pk>/", service_detail, name="services-detail")
    ]
