import os.path
import random
import pandas as pd
import datetime as dt
import smtplib

MY_EMAIL = "me@example.com"
MY_EMAIL_HOST = "smtp.example.de"
MY_PASSWORD = "Abcd1234()"
FRIENDS = pd.read_csv("birthdays.csv").to_dict(orient="records")
LETTER_PATHS = [os.path.join("letter_templates", "letter_1.txt"), os.path.join("letter_templates", "letter_2.txt"),
                os.path.join("letter_templates", "letter_3.txt")]

day = dt.date.today().day
month = dt.date.today().month
birthday_children = [friend for friend in FRIENDS if friend["day"] == day and friend["month"] == month]

if birthday_children:
    with smtplib.SMTP(host=MY_EMAIL_HOST) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for friend in birthday_children:
            with open(random.choice(LETTER_PATHS), "r") as f:
                letter = f.read().replace("[NAME]", friend["name"])
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=friend["email"],
                                    msg="Subject:Happy Birthday!\n\n" + letter)
