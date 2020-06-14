#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json
import requests
import sys
from pytemperature import k2c
# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API.
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={appid}&units=metric'
response = requests.get(url)
response.raise_for_status()
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData
degree = u"\N{DEGREE SIGN}"
print('Current weather in %s:' % location)
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])
print(f"{(w['main']['temp'])}{degree}C feels like {k2c(w['main']['feels_like'])}{degree}C")
