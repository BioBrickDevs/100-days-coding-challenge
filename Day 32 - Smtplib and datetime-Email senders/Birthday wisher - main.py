
import datetime as dt
import smtplib
import pandas
import random
import os


username = "yourusername@gmail.com"
password = "yourpassword"

LETTERS_PATH = os.getcwd() + "/letter_templates/"


birthdays = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
day = now.day
month = now.month


for brthday in birthdays.itertuples():
    if brthday.day == day and brthday.month == month:
        random_letter = random.choice(os.listdir("./letter_templates/"))

        with open(LETTERS_PATH+random_letter) as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", brthday.name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(username, password)
            connection.sendmail(username, brthday.email,
                                msg=f"Subject:Happy Birthday!\n\n{letter}")
