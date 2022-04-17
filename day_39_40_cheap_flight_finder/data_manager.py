import requests
from flight_search import API_KEY

SHEETY_ENDPOINT: str = "YOUR SHEETY ENDPOINT"
USERS_ENDPOINT: str = "YOUR SHEETY USERS ENDPOINT"

KIWI_LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
location_params: dict = {
    "location_types": "airport",
    "limit": "1"
}
headers: dict = {
    "apikey": API_KEY
}


class DataManager:

    @staticmethod
    def populate_iata_codes() -> None:
        for i, row in enumerate(DataManager.get_sheet_data()):
            if not row["iataCode"]:
                location_params["term"] = row["city"]
                location_response: requests.models.Response = requests.get(url=KIWI_LOCATIONS_ENDPOINT,
                                                                           params=location_params,
                                                                           headers=headers)
                iata_code: str = location_response.json()["locations"][0]["id"]
                row_endpoint: str = f"{SHEETY_ENDPOINT}/{i+2}"
                edit_params: dict = {
                    "price": {
                        "iataCode": iata_code
                    }
                }
                requests.put(url=row_endpoint, json=edit_params, headers=headers)

    @staticmethod
    def get_sheet_data() -> list:
        response: requests.models.Response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        return response.json()["prices"]

    @staticmethod
    def get_emails() -> list:
        response: requests.models.Response = requests.get(url=USERS_ENDPOINT)
        response.raise_for_status()
        return [user["email"] for user in response.json()["users"]]
