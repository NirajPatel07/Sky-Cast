import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    api_key = 'your_api_key'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    
    weather_data = []
    cities = City.objects.all()
    for city in cities:
        response = requests.get(url.format(city, api_key)).json()

        city_weather = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        }
        
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather_app/index.html', context)
