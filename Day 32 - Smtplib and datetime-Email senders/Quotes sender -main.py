import datetime
import smtplib
import random


SMTP_USER = "youremail@gmail.com"
SMTP_PASSWORD = "yourpassword"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


current_time = datetime.datetime.now()
today = current_time.weekday()
sunday = 6


# print(all_quotes)
if today == sunday:

    with open("quotes.txt", "r") as file:
        all_quotes = file.read()
        quotes_list = all_quotes.splitlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

        connection.starttls()
        connection.login(SMTP_USER, SMTP_PASSWORD)
        connection.sendmail(SMTP_USER, SMTP_USER,
                            msg=f"Subject:{random_quote}\n\n{random_quote}")
