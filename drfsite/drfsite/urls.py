from django.contrib import admin
from django.urls import path

from main.views import IndicatorsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/indicators/', IndicatorsAPIView.as_view(), name='indicators')
]
