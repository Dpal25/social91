from rest_framework import serializers
from get_pricing import models


class GetPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PricePerPart
        fields = '__all__'