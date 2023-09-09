from django.urls import path
from . import views


urlpatterns = [
    path('<int:region_id>/', views.region_detail, name='region_detail'),
]
