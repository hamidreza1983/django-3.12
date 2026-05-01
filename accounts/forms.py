from django import forms
from .models import UserModel
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=12)
    password = forms.CharField(max_length=100)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserModel
        fields = ("email", "phone", "id_code", "password1", "password2")


class ChangePasswordForm(forms.Form):
    new_pass1 = forms.CharField(max_length=12)
    new_pass2 = forms.CharField(max_length=12)

class ResetPasswordForm(forms.Form):
    email = forms.EmailField()