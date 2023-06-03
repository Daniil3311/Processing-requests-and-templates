from unittest import TestCase
from rest_framework.test import APIClient
from stocks_products.wsgi import *


class TestSampleView(TestCase):
    def test_view_200(self):
        url = 'api/v1/test'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
