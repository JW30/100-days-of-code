import requests

USERS_ENDPOINT: str = "https://api.sheety.co/3e77334dd66abc624a0e070adc56239a/flightdeals/users"

# Get user data via console input.
print("*** Welcome to the Flight Club!")
print("*** We find the best Flight Deals and Email them directly to you")
first_name: str = input("What is your first name? ")
last_name: str = input("What is your last name? ")
matching_emails = False
while not matching_emails:
    email1: str = input("What is your email? ")
    email2: str = input("Please type your email again. ")
    matching_emails: bool = email1 == email2
    if not matching_emails:
        print("The emails you have entered do not match, please try again!")

# Check if email does already exist.
response = requests.get(url=USERS_ENDPOINT)
user_already_exists: bool = any(user["email"] == email1 for user in response.json()["users"])

# Add user to Google Sheet.
if user_already_exists:
    print("*** Email already registered!")
else:
    params: dict = {
        "user": {
            "first-name": first_name,
            "last-name": last_name,
            "email": email1
        }
    }

    response = requests.post(url=USERS_ENDPOINT, json=params)

    print("*** Success! Your email has been added, look forward to receive emails from us soon.")
