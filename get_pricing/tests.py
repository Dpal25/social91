from rest_framework import status, reverse
from .models import PricePerPart
from social91_coding.serializer import GetPricingSerializer
from unittest import TestCase
import requests


class GetSingleDataTestCase(TestCase):
    def test_get_single_data_positive(self):
        data = {
            'date' : '2013-01-01'
        }

        url = 'http://localhost:8000/getprice/'
        response = requests.post(url, data=data)
        price = PricePerPart.objects.get(date=data['date'])
        serializer = GetPricingSerializer(price)
        assert response.status_code == status.HTTP_200_OK

    def test_get_single_data_nagative(self):
        data = {
            'date' : '2020-01-01'
        }

        url = 'http://localhost:8000/getprice/'
        response = requests.post(url, data=data)
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


