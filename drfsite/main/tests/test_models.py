import pytest

from django.urls import reverse

from main.models import Indicators
from main.serializers import IndicatorsSerializer


@pytest.mark.django_db
def test_indicators_create():
    indicator = Indicators.objects.create(
        title='Motor Vehicle Retail Sales: Heavy Weight Trucks',
        symbol='HTRUCKSSAAR',
        link='https://fred.stlouisfed.org/series/HTRUCKSSAAR'
    )
    assert indicator.title == 'Motor Vehicle Retail Sales: Heavy Weight Trucks'
    assert indicator.symbol == 'HTRUCKSSAAR'
    assert indicator.link == 'https://fred.stlouisfed.org/series/HTRUCKSSAAR'
