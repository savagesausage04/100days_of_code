from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/kylehan/Downloads/chromedriver"
options = webdriver.ChromeOptions()
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
game_over = time.time() + 300
interval = time.time() + 5
upgrades = driver.find_elements(By.CLASS_NAME, "grayed")
upgrade_id = [upgrade.get_attribute("id") for upgrade in upgrades]
while True:
    cookie.click()
    if time.time() > interval:
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        print(len(prices))
        cost_list = []
        for price in prices:
            if price.text != "": #extra values added to prices list, random "" elements in prices
                cost = int(price.text.split("-")[1].strip().replace(",", ""))
                cost_list.append(cost)

        #join cost and item upgrade with value:pair dict
        cost_id_dictionary = {}
        for _ in range(len(cost_list)):
            cost_id_dictionary[cost_list[_]] = upgrade_id[_]

        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money.replace(",", "")
        money_int = int(money)

        affordable_upgrades = {}
        for cost, id in cost_id_dictionary.items():
            if money_int > cost:
                affordable_upgrades[cost] = id

        most_expensive = max(affordable_upgrades)
        most_expensive_id = affordable_upgrades[most_expensive]

        upgrade_to_buy = driver.find_element(By.ID, most_expensive_id)
        upgrade_to_buy.click()

        interval += 8

    if time.time() > game_over:
        cps = driver.find_element(By.ID, "cps")
        print(cps.text)
        break







