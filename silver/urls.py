from django.urls import path
from . import views

urlpatterns = [
    path('', views.silver_chart, name='silver_chart'),
]