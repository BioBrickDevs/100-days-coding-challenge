from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chromedriver_path = "./chromedrive"


browser = webdriver.Chrome(chromedriver_path)
browser.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = browser.find_element(By.XPATH, "/html/body/div[3]/div[6]/div[9]")
money = browser.find_element(By.ID, "money")


buy_cursor = browser.find_element(By.ID, "buyCursor")


buy_grandma = browser.find_element(By.ID, "buyGrandma")

buy_factory = browser.find_element(By.ID, "buyFactory")

buy_mine = browser.find_element(By.ID, "buyMine")

buy_shipment = browser.find_element(By.ID, "buyShipment")

buy_alchemy_lab = browser.find_element(By.ID, "buyAlchemy lab")

buy_portal = browser.find_element(By.ID, "buyPortal")

buy_time_machine = browser.find_element(By.ID, "buyTime machine")


timeout = time.time() + 5
while True:

    cookie.click()

    cookie = browser.find_element(By.XPATH, "/html/body/div[3]/div[6]/div[9]")
    money = browser.find_element(By.ID, "money")

    buy_cursor = browser.find_element(By.ID, "buyCursor")

    buy_grandma = browser.find_element(By.ID, "buyGrandma")

    buy_factory = browser.find_element(By.ID, "buyFactory")

    buy_mine = browser.find_element(By.ID, "buyMine")

    buy_shipment = browser.find_element(By.ID, "buyShipment")

    buy_alchemy_lab = browser.find_element(By.ID, "buyAlchemy lab")

    buy_portal = browser.find_element(By.ID, "buyPortal")

    buy_time_machine = browser.find_element(By.ID, "buyTime machine")

    money_amount = int(money.text.replace(",", ""))
    cursor_price = int(buy_cursor.text.split(
        " ")[2].split("\n")[0].replace(",", ""))
    grandma_price = int(buy_grandma.text.split(
        " ")[2].split("\n")[0].replace(",", ""))
    factory_price = int(buy_factory.text.split(
        " ")[2].split("\n")[0].replace(",", ""))
    mine_price = int(buy_mine.text.split(
        " ")[2].split("\n")[0].replace(",", ""))
    shipment_price = int(buy_shipment.text.split(
        " ")[2].split("\n")[0].replace(",", ""))
    alchemy_lab_price = int(buy_alchemy_lab.text.replace(
        ",", "").split("-")[1].strip().split("\n")[0])
    portal_price = int(buy_portal.text.split(
        " ")[2].split("\n")[0].replace(",", ""))
    time_machine_price = int(buy_time_machine.text.replace(
        ",", "").split("-")[1].strip().split("\n")[0])

    if time.time() >= timeout:
        if money_amount >= time_machine_price:
            buy_time_machine.click()
        elif money_amount >= portal_price:
            buy_portal.click()
        elif money_amount >= alchemy_lab_price:
            buy_alchemy_lab.click()
        elif money_amount >= shipment_price:
            shipment_price.click()
        elif money_amount >= mine_price:
            buy_mine.click()
        elif money_amount >= factory_price:
            buy_factory.click()
        elif money_amount >= grandma_price:
            buy_grandma.click()
        else:
            buy_cursor.click()
            browser.implicitly_wait(1)
        timeout = time.time() + 5
