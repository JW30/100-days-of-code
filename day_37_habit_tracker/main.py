import requests
import datetime as dt

USERNAME: str = "YOUR_PIXELA_USERNAME"
TOKEN: str = "YOUR_PIXELA_TOKEN"
GRAPH_ID: str = "push-up-tracker"
PIXELA_ENDPOINT: str = "https://pixe.la/v1/users"
GRAPH_ENDPOINT: str = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT: str = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
DATE_TODAY: str = dt.date.today().strftime("%Y%m%d")
TODAYS_PIXEL_ENDPOINT: str = f"{PIXEL_CREATION_ENDPOINT}/{DATE_TODAY}"
HEADERS: dict = {
        "X-USER-TOKEN": TOKEN
        }


# Create Account.
def create_acc():
    user_params: dict = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
        }

    response: requests.models.Response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)


# Create graph.
def create_graph():
    graph_config: dict = {
        "id": GRAPH_ID,
        "name": "Push-Up-Tracker",
        "unit": "Push-Ups",
        "type": "int",
        "color": "shibafu"
    }

    response: requests.models.Response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
    print(response.text)


# Set pixel for today's date with quantity of 20.
def set_pixel_today():
    pixel_config: dict = {
        "date": DATE_TODAY,
        "quantity": input("How many push-ups did you do today? ")
    }

    response: requests.models.Response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_config, headers=HEADERS)
    print(response.text)


# Delete today's pixel
def delete_pixel_today():
    response: requests.models.Response = requests.delete(url=TODAYS_PIXEL_ENDPOINT, headers=HEADERS)
    print(response.text)


if __name__ == "__main__":
    # create_acc()
    # create_graph()
    set_pixel_today()
    # delete_pixel_today()
