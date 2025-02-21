import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def get_weather(request):

    weather_data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "76d43a3b5d928ed1c96b84436812d616"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),
            }
        else:
            weather_data = {'error': 'City not found. Please try again.'}

    return render(request, 'index.html', {'weather_data': weather_data})