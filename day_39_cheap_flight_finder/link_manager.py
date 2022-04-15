import requests

BITLY_ENDPOINT: str = "https://api-ssl.bitly.com/v4/shorten"
TOKEN: str = "YOUR BITLY BEARER TOKEN"


class LinkManager:

    @staticmethod
    def shorten_url(url: str):
        params: dict = {
            "long_url": url
        }
        headers: dict = {
            "Authorization": f"Bearer {TOKEN}"
        }
        response: requests.models.Response = requests.post(url=BITLY_ENDPOINT, json=params, headers=headers)
        response.raise_for_status()
        return response.json()["link"]
