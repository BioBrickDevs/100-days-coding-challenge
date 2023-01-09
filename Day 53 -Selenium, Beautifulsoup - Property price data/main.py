from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
form_url = "https://forms.gle/igYDT3uLKLfGyNuTA"
chromedriver_path = "./chromedriver"
browser = webdriver.Chrome(chromedriver_path)

url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-125.36049929980469%2C%22east%22%3A-122.14699832324219%2C%22south%22%3A37.1947471332448%2C%22north%22%3A38.267800825026384%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D"
# browser.get(url)
# pageSource = browser.page_source
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 15236.35.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
           "Accept-Language":  "en,fi;q=0.9,fi-FI;q=0.8",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           }
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
lista = soup.select("#grid-search-results > ul > li")
prices = []
links = []
addresses = []
for x in lista:
    try:
        result = x.find_next(attrs={"data-test": "property-card-link"})
        price = x.find_next(attrs={"data-test": "property-card-price"})
        price = price.text.replace(",", "").split("+")[0]

        link = "https://zillow.com" + result["href"]
        address = result.text
        prices.append(price)
        links.append(link)
        addresses.append(address)
    except:
        break
# grid-search-results > ul > li:nth-child(5)
browser.get(form_url)
for index in range(0, len(links)):

    address_input = browser.find_element(
        By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    address_input.click()
    address_input.send_keys(addresses[index])
    price_input = browser.find_element(
        By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    price_input.click()
    price_input.send_keys(prices[index])

    link_input = browser.find_element(
        By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    link_input.click()
    link_input.send_keys(links[index])

    submit = browser.find_element(
        By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span")
    submit.click()
    link = browser.find_element(
        By.CSS_SELECTOR, "body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a")
    link.click()
