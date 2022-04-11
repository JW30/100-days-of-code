import requests
from twilio.rest import Client

LAT: float = 51.5072
LON: float = 0.1276
API_KEY: str = ""
TWILIO_ACCOUNT_SID: str = ""
TWILIO_AUTH_TOKEN: str = ""
TWILIO_PHONE_NUMBER: str = ""
MY_PHONE_NUMBER: str = ""

params: dict = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alert"
}

response: requests.models.Response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data: dict = response.json()

is_going_to_rain: bool = any(int(hour["weather"][0]["id"]) < 700 for hour in data["hourly"][:12])

if is_going_to_rain:

    client: Client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
                    .create(
                         body="It will rain in the next 12 hours, don't forget to take an umbrella with you!",
                         from_=TWILIO_PHONE_NUMBER,
                         to=MY_PHONE_NUMBER
                     )

    print(message.status)
