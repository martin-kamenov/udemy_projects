import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "f0470a9bdc5cf7d198614887fa60fcd7"
account_sid = "AC9ca173c1db2c22d46c2050f813bfb4bc"
auth_token = "0c42a5d68e5bf3c530a38cf71b62199f"

parameters = {
    "lat": 43.51,
    "lon":  25.57,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()

print(f"Status code: {response.status_code}")

data_list = data['list']

will_rain = False
for hour_data in data_list:
    condition_code = hour_data["weather"][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+12564483845',
        to='+359883315717'
    )

    print(message.status)
