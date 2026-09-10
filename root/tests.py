from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import *

# Create your tests here.

class TestRoot(TestCase):
    def test_url_home(self):
        url = reverse("root:home")
        self.assertEqual(resolve(url).func, home )

    def test_url_about(self):
        url = reverse("root:about")
        self.assertEqual(resolve(url).func.view_class, AboutView )

    def test_content_home(self):
        url = reverse("root:home")
        c = Client()
        response = c.get(url)
        if "consectetur" in str(response.content):
            r = True
        else:
            r = False
        self.assertTrue(r)