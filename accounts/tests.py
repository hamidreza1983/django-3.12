from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import *
from .forms import *
from .models import *

# Create your tests here.

class TestForms(TestCase):
    def test_form_valid_login(self):
        form = LoginForm(data={
            "email" : "hamid@reza.com",
            "password" : "H@midreza62"
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_login(self):
            form = LoginForm(data={
                "email" : "hamid",
                "password" : "H@midreza62"
            })
            self.assertFalse(form.is_valid())


class TestUserModel(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(email="hamid@reza.com", password="H@midreza62")

    def test_create_user_on_model(self):
        self.assertEqual(self.user.email, "hamid@reza.com")

    def test_create_user_on_model_2(self):
        self.assertTrue(UserModel.objects.filter(id=self.user.id).exists())


class TestResponseAccounts(TestCase):
    def setUp(self):
        self.c = Client()

    def test_response_login(self):
        url = reverse("accounts:login")
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_response_register(self):
        url = reverse("accounts:register")
        response = self.c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_login(self):
        url = reverse("accounts:login")
        response = self.c.get(url)
        self.assertTemplateUsed(response, template_name="accounts/login.html")