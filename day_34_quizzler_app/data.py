import requests

response: requests.models.Response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

question_data: dict = response.json()["results"]
