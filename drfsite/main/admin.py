from django.contrib import admin

from .models import Indicators
from .models import Category

admin.site.register(Indicators)
admin.site.register(Category)
