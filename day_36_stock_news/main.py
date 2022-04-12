import requests
import datetime as dt
from twilio.rest import Client

# Constants
STOCK: str = "TSLA"
COMPANY_NAME: str = "Tesla"
ALPHAVANTAGE_KEY: str = "Your own Alphavantage API Key"
NEWSAPI_KEY: str = "Your own NewsAPI API Key"
TWILIO_ACCOUNT_SID: str = "Your own Twilio Account SID"
TWILIO_AUTH_TOKEN: str = "Your own Twilio Authentication Token"
TWILIO_PHONE_NUMBER: str = "Your virtual Twilio Phone Number"
VERIFIED_NUMBER: str = "Your own phone number verified with Twilio"


# Get delta of yesterday's and the day before's closing price.
def get_delta(stock: str, key: str) -> float:
    params_alpha: dict = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": key
    }
    url_alpha: str = "https://www.alphavantage.co/query"
    response_alpha: requests.models.Response = requests.get(url=url_alpha, params=params_alpha)
    response_alpha.raise_for_status()
    daily_data_list: list = list(response_alpha.json()["Time Series (Daily)"].values())

    recent_closing_price: float = float(daily_data_list[0]["4. close"])
    day_before_closing_price: float = float(daily_data_list[1]["4. close"])

    delta: float = (recent_closing_price - day_before_closing_price) / day_before_closing_price

    return delta


# Get 3 most popular news headlines for the stock.
def get_articles(company: str, key: str) -> list:
    day_before_yesterday = dt.date.today() - dt.timedelta(2)
    params: dict = {
        "apiKey": key,
        "q": company,
        "searchIn": "title",
        "pageSize": 3
    }
    url: str = "https://newsapi.org/v2/top-headlines"
    response_news = requests.get(url=url, params=params)
    response_news.raise_for_status()
    articles = response_news.json()["articles"]

    return articles


# Create SMS message.
def make_sms(delta: float, articles: list) -> str:
    if delta > 0:
        icon: str = "📈"
    else:
        icon: str = "📉"
    message: str = "{} {} {:+2.2f}%\n\n".format(STOCK, icon, delta*100)

    for article in articles:
        message += "Headline: {}\n".format(article["title"]) + \
                   "URL: {}\n\n".format(article["url"])

    return message


# Send SMS.
def send_sms(sms: str) -> None:
    client: Client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
            body=sms,
            from_=TWILIO_PHONE_NUMBER,
            to=VERIFIED_NUMBER
        )

    print(message.status)


delta_prices: float = get_delta(STOCK, ALPHAVANTAGE_KEY)
if delta_prices <= -0.05 or delta_prices >= 0.05:
    headlines: list = get_articles(COMPANY_NAME, NEWSAPI_KEY)
    sms_message: str = make_sms(delta_prices, headlines)
    send_sms(sms_message)
