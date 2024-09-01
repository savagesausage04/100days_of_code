from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

#----------------------------------------BEAUTIFUL SOUP--------------------------------------------#
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66150047215739%2C%22north%22%3A37.888907562841936%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers={"Accept-Language": "en-US,en;q=0.9",
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
         }

response = requests.get(URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
###########Find all the property links########################
all_links = soup.find_all(name="a", tabindex="-1")
formatted_links = []
for link in all_links[0:8]:
    formatted_link = link["href"]
    if "https://www.zillow.com" not in formatted_link:
       formatted_link = "https://www.zillow.com" + formatted_link
    formatted_links.append(formatted_link)

#############Find all the property prices#######################
all_prices = soup.find_all(name="div", class_="list-card-price")
prices = []
for price in all_prices:
    price_text = price.getText()[0:6]
    prices.append(price_text)

#############Find all the property addresses####################
all_addresses = soup.find_all(name="address", class_="list-card-addr")
addresses = []
for address in all_addresses:
    address_text = address.getText()
    addresses.append(address_text)


#-----------------------------------------------SELENIUM-----------------------------------------#
chrome_driver_path = "/Users/kylehan/Development/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)

for i in range(len(formatted_links)):
    driver.get("https://forms.gle/BuoQTQp2E4Cr56Z38")

    time.sleep(5)
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[i])
    time.sleep(1)


    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices[i])
    time.sleep(1)

    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(formatted_links[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()



