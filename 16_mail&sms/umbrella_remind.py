#! python 3

"""Check the weather forecast and text an umbrella reminder if it's raining."""

import json
import requests
from twilio.rest import TwilioRestClient


def get_onecall_json(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly' \
          f'&appid={appid}'
    response = requests.get(url)
    response.raise_for_status()
    onecall_json = json.loads(response.text)
    return onecall_json

def check_rain(onecall_json):
    if rain in onecall_json['daily'][0]['weather'][0]['main'].lower():
        return True

def send_umbrella_sms(onecall_json):
    account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    my_number = '+15559998888'
    twilo_number = '+15552225678'
    degree = u"\N{DEGREE SIGN}"
    temp = f"{(onecall_json['current']['temp'])}{degree}C feels like {(onecall_json['current']['feels_like'])}{degree}C"
    rain_status = onecall_json['daily'][0]['weather'][0]['main'] + ' - ' + onecall_json['daily'][0]['weather'][0]['description']
    message = 'Today\'s weather:' + f'\n{rain_status}' + f'\n{temp}' + '\nGrab your umbrella!'
    twilo_cli = TwilioRestClient(account_sid, auth_token)
    twilo_cli.messages.create(body=message, from_=twilo_number, to=my_number)


if __name__ == "__main__":
    rain = 'rain'
    w = get_onecall_json(lat, lon)
    if check_rain(w):
        send_umbrella_sms(w)
