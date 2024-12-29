from django.shortcuts import render
import requests

# OpenWeather API Anahtarınız
API_KEY = "8a0dbb8511cc188e62055ba49f7c5ba8"


def weather_home(request):
    city = request.GET.get('city', 'Istanbul')  # Varsayılan şehir İstanbul
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json() if response.status_code == 200 else None

    context = {
        'city': city,
        'weather': data,
    }
    return render(request, 'weather/weather.html', context)