from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

my_destinations: list = DataManager.get_sheet_data()

for dst in my_destinations:
    flight_data: list = FlightSearch.get_flight_data(dst["iataCode"], dst["lowestPrice"])
    if flight_data:
        sms_text: str = NotificationManager.create_sms_text(flight_data[0])
        NotificationManager.send_sms(sms_text)
