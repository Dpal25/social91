from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from social91_coding import serializer
from get_pricing import models
# Create your views here.


class GetPricing(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            price = models.PricePerPart.objects.get(date=request.data['date'])
        except:
            return Response({'message': 'Incorrect Input'})

        serialized = serializer.GetPricingSerializer(price)

        return Response({'message': 'Here are the details', 'Pricing': serialized.data})
