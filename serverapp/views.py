from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests



@api_view(['GET'])
def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
    
    # Get location and weather data from OpenWeatherMap
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=f112e3200561aa905c68fc8aca47be38&units=metric'
    weather_response = requests.get(weather_url)
    
    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        city = weather_data['name']
        temperature = weather_data['main']['temp']
    else:
        city = 'Unknown'
        temperature = 'Unknown'
    
    return Response({
        'client_ip': client_ip,
        'location': city,
        'greeting': f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {city}"
    })