import requests
from bs4 import BeautifulSoup
import keys
import smtplib


class PriceAlerter:

    def __init__(self):
        self.items: list = requests.get(url=keys.SHEETY_URL_AMZN).json()['sheet1']
        self.params: dict = {
            "accept-language": "en,de;q=0.9",
            "user-agent": keys.USER_AGENT
        }

    def run(self) -> None:
        for item in self.items:
            soup = self.make_soup(item.get('url'))
            if not item.get('productName'):
                name: str = self.get_name(soup)
                self.update_name(item['id'], name)
            current_price: float = self.get_price(soup)
            if current_price < item['price']:
                self.send_email(item, current_price)

    def make_soup(self, url: str):
        response = requests.get(url=url, headers=self.params)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    @staticmethod
    def get_name(soup) -> str:
        return soup.find(name="span", id="productTitle").getText().strip()

    @staticmethod
    def update_name(item_id: int, name: str) -> None:
        update_params: dict = {
            'sheet1': {
                'productName': name
            }

        }
        response = requests.put(url=f"{keys.SHEETY_URL_AMZN}/{item_id}", json=update_params)
        response.raise_for_status()

    @staticmethod
    def get_price(soup) -> float:
        price_str: str = soup.find(name="span", id="price").getText()
        price_split: list = price_str.replace("€", "").split(".")
        price: float = int(price_split[0]) + int(price_split[1]) / 100
        return price

    @staticmethod
    def send_email(item, current_price) -> None:
        email: str = item['email']
        price_limit: float = item['price']
        name: str = item['productName']
        url: str = item['url']
        with smtplib.SMTP(host=keys.MY_EMAIL_HOST) as connection:
            connection.starttls()
            connection.login(user=keys.MY_EMAIL, password=keys.MY_PASSWORD)
            connection.sendmail(from_addr=keys.MY_EMAIL, to_addrs=email,
                                msg="Subject:Amazon Price Alert!\n\n"
                                    f"Hello! :)\n"
                                    f"{name} currently is cheaper than {price_limit} Euro!\n"
                                    f"Current price: {current_price}.\n"
                                    f"Click here to buy: {url}")


if __name__ == "__main__":
    pa: PriceAlerter = PriceAlerter()
    pa.run()
