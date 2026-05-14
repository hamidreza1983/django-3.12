from django.urls import path
from .views import *


app_name = "services"

urlpatterns = [
    path("", ServicesView.as_view(), name="services"),
    path("category/<str:category>/", ServicesView.as_view(), name="services_by_category"),
    path("tags/<str:tag>/", ServicesView.as_view(), name="services_by_tag"),
    path("detail/<int:pk>/", ServicesDetailView.as_view(), name="detail")
]
