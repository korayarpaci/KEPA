from django.urls import path
from . import views

urlpatterns = [
    path('', views.petrol_chart, name='petrol_chart'),  # Petrol ana sayfası
]