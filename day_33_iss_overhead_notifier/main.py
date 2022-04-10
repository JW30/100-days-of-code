import requests
import datetime as dt
import smtplib
import time

# Constants
MY_LAT = 52.520008
MY_LNG = 13.404954
MY_EMAIL = "someone@example.com"
MY_EMAIL_HOST = "smtp.example.com"
MY_PASSWORD = "Abcd1234()"

# Get ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["latitude"])

# Get sunrise and sunset UTC time for my position
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunrise"]
sunrise = int(''.join(sunrise.split("T")[1].split(":")[:2]))
sunset = int(''.join(sunset.split("T")[1].split(":")[:2]))

# Get current UTC time
time_now = dt.datetime.utcnow().time()
time_now = int(str(time_now.hour) + str(time_now.minute))

# My position within +5 or -5 degrees of the ISS position
iss_near_me = iss_lat - 5 <= MY_LAT <= iss_lat + 5 and iss_lng - 5 <= MY_LAT <= iss_lng + 5
# Current time after sunset or before sunrise
is_nighttime = sunset < time_now or time_now < sunrise

while True:
    time.sleep(60)
    if iss_near_me and is_nighttime:
        with smtplib.SMTP(host=MY_EMAIL_HOST) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject:ISS Overhead\n\n"
                                    "Hurry up!\n\nThe ISS might be visible at your position right now!")
        break
