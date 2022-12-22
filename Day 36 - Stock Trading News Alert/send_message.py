
import yagmail
import os
import dotenv
dotenv.load_dotenv()
username = os.environ.get("USER_NAME")
password = os.environ.get("password")


def send_message(message, subject):
    the_message = message
    yag = yagmail.SMTP(username, password)
    yag.send(username, subject + " Alert!", the_message)
