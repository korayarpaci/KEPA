from django.urls import path
from . import views

urlpatterns = [
    path('', views.gold_chart, name='gold_chart'),  # Altın ana sayfası
]