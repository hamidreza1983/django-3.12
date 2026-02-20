from django.urls import path
from .views import *


app_name = "services"

urlpatterns = [
    path("", services, name="services"),
    path("category/<str:category>/", services, name="services_by_category"),
    path("tags/<str:tag>/", services, name="services_by_tag"),
    path("detail/<int:id>/", service_detail, name="detail")
]
