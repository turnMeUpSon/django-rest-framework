from rest_framework import serializers
from .models import Indicators


class IndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicators
        fields = ('title', 'symbol', 'link', 'cat_id')
