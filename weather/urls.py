from django.urls import path
from . import views  # Doğru import

urlpatterns = [
    path('', views.weather_home, name='weather_home'),  # Fonksiyonu çağır
]