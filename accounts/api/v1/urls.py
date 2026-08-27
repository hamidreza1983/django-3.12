from django.urls import path
from .views import SignupApiView
from .views import LoginView, LogoutView, ChangePasswordView

urlpatterns = [
    path("signup", SignupApiView.as_view()),
    path("login", LoginView.as_view()),
    path("logout", LogoutView.as_view()),
    path("change-password", ChangePasswordView.as_view()),
    # path("reset-password"),
]
