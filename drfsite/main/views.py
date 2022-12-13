from django.shortcuts import render
from rest_framework import generics
from .models import Indicators
from .serializers import IndicatorsSerializer


class IndicatorsAPIView(generics.ListAPIView):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer
