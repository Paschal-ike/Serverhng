from django.http import JsonResponse
import requests

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

    # Hardcoding an example IP for demonstration purposes
    if client_ip == '127.0.0.1':
        client_ip = '8.8.8.8'  # Example IP address (Google's public DNS server)

    # Get the location based on IP address
    location_response = requests.get(f"https://ipinfo.io/{client_ip}/json")
    location_data = location_response.json()
    city = location_data.get('city', 'Unknown')

    # For simplicity, use a fixed temperature. Ideally, use a weather API.
    temperature = 11

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"

    response_data = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }

    return JsonResponse(response_data)
