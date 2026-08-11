from django.urls import path
from .views import SignupApiView
from .views import LoginView





urlpatterns = [
    path("signup", SignupApiView.as_view()),
    path("login", LoginView.as_view()),
    #path("logout"),
    #path("change-password"),
    #path("reset-password"),

]
