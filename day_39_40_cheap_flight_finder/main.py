from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

DataManager.populate_iata_codes()
my_destinations: list = DataManager.get_sheet_data()
emails: list = DataManager.get_emails()

for dst in my_destinations:
    flight_data: list = FlightSearch.get_flight_data(iata=dst["iataCode"], max_price=dst["lowestPrice"])
    if flight_data:
        sms_text: str = NotificationManager.create_alert_text(flight_data=flight_data[0])
        NotificationManager.send_sms(text=sms_text)
        email_text: str = "Subject:New Low Price Alert!\n\n" + sms_text
        for email in emails:
            NotificationManager.send_email(email=email, text=email_text)
