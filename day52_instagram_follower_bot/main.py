from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "/Users/kylehan/Development/chromedriver"
service = Service(CHROME_DRIVER_PATH)



SIMILAR_ACCOUNT = "ashlee.y_"
USERNAME = "han.k04"
PASSWORD = "Sangjun04!"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        time.sleep(2)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        time.sleep(1)

        password.send_keys(Keys.ENTER)


        # login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        # login.click()





    def find_followers(self):
        time.sleep(3)
        self.driver.get("https://www.instagram.com/ashlee.y_/")
        time.sleep(3)
        follower_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        follower_link.click()
        time.sleep(5)

        for i in range(100):
            button = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas')
            button.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)




    def follow(self):
        follows = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for follow in follows:
            if follow.text == "Follow":
                follow.click()
                time.sleep(1)





bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()









