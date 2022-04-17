import requests
import datetime as dt
from dateutil.relativedelta import relativedelta

# Constants
MY_LAT: str = "52.520008"
MY_LON: str = "13.404954"
KIWI_ENDPOINT: str = "https://tequila-api.kiwi.com/v2/search?"
API_KEY: str = "YOUR KIWI API KEY"

# Variables
search_params: dict = {
    "fly_from": f"{MY_LAT}-{MY_LON}-100km",
    "date_from": dt.date.today().strftime("%d/%m/%Y"),
    "date_to": (dt.date.today() + relativedelta(months=6)).strftime("%d/%m/%Y"),
    "adults": "1",
    "nights_in_dst_from": "2",
    "nights_in_dst_to": "14",
    "limit": "1",

    }

headers: dict = {
    "apikey": API_KEY
}


class FlightSearch:

    @staticmethod
    def get_flight_data(iata: str, max_price: str, max_stopovers: int = 0) -> list:
        search_params["fly_to"] = iata
        search_params["price_to"] = max_price
        search_params["max_stopovers"] = str(max_stopovers)
        response = requests.get(url=KIWI_ENDPOINT, params=search_params, headers=headers)
        data = response.json()["data"]
        if max_stopovers == 0 and not data:
            data = FlightSearch.get_flight_data(iata, max_price, 1)
        return data
