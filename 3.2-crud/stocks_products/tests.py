from unittest import TestCase
from rest_framework.test import APIClient
<<<<<<< HEAD
from stocks_products.settings import *


=======
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocks_products.settings')
django.setup()
>>>>>>> 38c2ea57f0cd174e5403540aeed9619960a0567b



class TestSampleView(TestCase):
    def test_view_200(self):
        url = 'api/v1/test'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
