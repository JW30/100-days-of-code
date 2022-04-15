import requests

SHEETY_ENDPOINT: str = "YOUR SHEETY ENDPOINT"


class DataManager:

    @staticmethod
    def get_sheet_data() -> list:
        response: requests.models.Response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        return response.json()["prices"]
