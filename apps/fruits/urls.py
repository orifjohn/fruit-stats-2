from django.urls import path
from . import views

urlpatterns = [
    path('', views.fruit_statistics, name='home'),
]
