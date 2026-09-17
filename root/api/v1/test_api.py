import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.fixture
def client():
    c = APIClient()
    return c


@pytest.mark.django_db
class TestRoot:
    def test_api_home(self, client):
        url = reverse("api_root:last-services")
        #url = "http://127.0.0.1:8000/api/v1/root/last-services/"
        response = client.get(url)
        assert response.status_code == 200



    def test_api_category(self, client):
            url = "http://127.0.0.1:8000/api/v1/root/categories/"
            response = client.get(url)
            assert response.status_code == 401