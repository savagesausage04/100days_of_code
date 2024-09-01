from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/kylehan/Development/chromedriver"
options = webdriver.ChromeOptions()
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://tinder.com/")
main_page = driver.current_window_handle

time.sleep(5)

sign_in = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
sign_in.click()

time.sleep(5)

facebook_button = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
facebook_button.click()

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        driver.switch_to.window(login_page)


time.sleep(5)

email = driver.find_element(By.NAME, "email")
email.send_keys("kyleh1104@gmail.com")

time.sleep(1)

password = driver.find_element(By.NAME, "pass")
password.send_keys("Sangjun04!")

time.sleep(1)

login = driver.find_element(By.NAME, "login")
login.click()

driver.switch_to.window(main_page)

time.sleep(10)

cookies = driver.find_element(By.XPATH, '//*[@id="q-996647900"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

location = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[1]/span')
location.click()

notifs = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div/div/div[3]/button[2]/span')
notifs.click()

time.sleep(5)

for _ in range(100):
    try:
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    except ElementClickInterceptedException:
        match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
        match_popup.click()




