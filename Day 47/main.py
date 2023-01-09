from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "./chromedriver"

browser = webdriver.Chrome(chrome_driver_path)
browser.get("http://www.python.org")
list_items = browser.find_elements(
    By.XPATH, value='/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li')

happenings = {}
for i,x in enumerate(list_items):
    try:
        # print(x.get_attribute("innerHTML"))
        # print(x.get_attribute("outerHTML"))
        link = x.find_element(By.TAG_NAME, "a")
        date = x.find_element(By.TAG_NAME, "time")
        url = link.get_attribute("href")
        happenings[i] = {
            "date": date.text,
            "happening": link.text,
            "link": url,
            
        }
        #happenings.append(happening)
    except:
        pass

print(happenings)