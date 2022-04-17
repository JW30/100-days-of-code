import requests

SHEETY_ENDPOINT: str = "YOUR SHEETY ENDPOINT FOR FLIGHT PRICES"
USERS_ENDPOINT: str = "YOUR SHEETY ENDPOINT FOR USERS"


class DataManager:

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
