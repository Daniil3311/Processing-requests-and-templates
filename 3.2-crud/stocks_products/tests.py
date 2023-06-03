from unittest import TestCase
from rest_framework.test import APIClient
import 
osos.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()


class TestSampleView(TestCase):
    def test_view_200(self):
        url = 'api/v1/test'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
