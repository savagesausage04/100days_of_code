from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWN = 100
PROMISED_UP = 10
chrome_driver_path = "/Users/kylehan/Development/chromedriver"
TWITTER_EMAIL = "kyleh1104@gmail.com"
TWITTER_PASSWORD = "Sangjun04!"

service = Service(chrome_driver_path)

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.go.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Down: {self.down}")
        print(f"Up: {self.up}")
        time.sleep(5)



    def tweet_at_provider(self, TWITTER_EMAIL, TWITTER_PASSWORD):

        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        login_input = self.driver.find_element(By.NAME, 'text')
        login_input.send_keys(TWITTER_EMAIL)
        login_input.send_keys(Keys.ENTER)
        time.sleep(2)

        username = self.driver.find_element(by=By.XPATH, value='// *[ @ id = "layers"] / div / div / div / div / div / div / div[2] / div[2] / div / div / div[2] / div[2] / \
                                 div[1] / div / div[2] / label / div / div[2] / div / input')
        username.send_keys("Kylie58277387")

        next_again = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next_again.click()

        time.sleep(3)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

        print("You logged in!")
        time.sleep(5)
        tweet_compose = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='.DraftEditor-editorContainer div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? "
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(
            by=By.XPATH,
            value=
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div['
            '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()

        self.driver.quit()




tw_bot = InternetSpeedTwitterBot()

tw_bot.get_internet_speed()

tw_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)


