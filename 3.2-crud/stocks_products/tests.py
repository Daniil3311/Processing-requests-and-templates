from unittest import TestCase
from rest_framework.test import APIClient
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'stocks_products.settings'
django.setup()



class TestSampleView(TestCase):
    def test_view_200(self):
        url = 'api/v1/test'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
