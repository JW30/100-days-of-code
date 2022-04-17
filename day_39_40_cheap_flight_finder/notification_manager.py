from twilio.rest import Client
from link_manager import LinkManager
import smtplib

# Constants
TWILIO_ACCOUNT_SID: str = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN: str = "YOUR TIWLIO AUTH TOKEN"
TWILIO_PHONE_NUMBER: str = "YOUR VIRTUAL PHONE NUMBER"
VERIFIED_NUMBER: str = "YOUR PHONE NUMBER VERIFIED WITH TWILIO"

MY_EMAIL: str = "someone@example.com"
MY_EMAIL_HOST: str = "smtp.example.com"
MY_PASSWORD: str = "YOUR EMAIL PASSWORD"


class NotificationManager:

    @staticmethod
    def create_alert_text(flight_data: dict):
        city_from: str = flight_data["cityFrom"]
        city_code_from: str = flight_data["cityCodeFrom"]
        city_to: str = flight_data["cityTo"]
        city_code_to: str = flight_data["cityCodeTo"]
        price: str = flight_data["price"]
        route: list = flight_data["route"]
        date_from: str = route[0]["local_departure"].split("T")[0]
        date_to: str = route[1]["local_departure"].split("T")[0]
        link: str = LinkManager.shorten_url(flight_data["deep_link"])
        sms_text: str = f"Low price alert! Only {price} Euro to fly from {city_from}-{city_code_from} to " \
                        f"{city_to}-{city_code_to}, from {date_from} to {date_to}.\nBook here: {link}"
        return sms_text

    @staticmethod
    def send_sms(text: str) -> None:
        client: Client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
                body=text,
                from_=TWILIO_PHONE_NUMBER,
                to=VERIFIED_NUMBER
            )

        print(message.status)

    @staticmethod
    def send_email(email: str, text: str):
        with smtplib.SMTP(host=MY_EMAIL_HOST) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=text)
