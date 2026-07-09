from django.urls import path
from .views import *



urlpatterns = [
    #path("", services, name="services"),
    #path("", ServicesListView.as_view(), name="services"),
    #path("detail/<int:pk>/", service_detail, name="services-detail")
    #path("detail/<int:pk>/", ServiceDetailView.as_view(), name="services-detail")
    path("", SerivcesView.as_view({"get":"list", "post" : "create"}), name="services"),
    path("detail/<int:pk>/", SerivcesView.as_view({"get":"retrieve", "put" : "update", "delete" : "destroy"}), name="services-detail")
    ]
