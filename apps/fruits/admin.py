from django.contrib import admin

from apps.fruits.models import Fruit, Stock

admin.site.register(Fruit)
admin.site.register(Stock)
