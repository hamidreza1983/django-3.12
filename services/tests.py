from django.test import TestCase
from django.urls import reverse, resolve
from .views import *

# Create your tests here.

class TestServices(TestCase):
    def test_url_detail(self):
        url = reverse("services:detail", kwargs={"pk" : 1})
        self.assertEqual(resolve(url).func.view_class, ServicesDetailView )