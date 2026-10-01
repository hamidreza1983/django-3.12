from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = "root"

urlpatterns = [
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("about/", cache_page(600) (AboutView.as_view()), name="about"),
    path("agents/", agent, name="agent"),
    path("soft98/", Soft98.as_view(), name="soft98"),
]

